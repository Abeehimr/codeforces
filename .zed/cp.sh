#!/usr/bin/env bash

set -e

FILE="$1"
TIME_LIMIT="${2:-}"

case "${FILE##*.}" in
    cpp)
        OUT="a.out"

        g++ "$FILE" \
            -std=c++17 \
            -O0 \
            -g \
            -pipe \
            -Wall \
            -Wextra \
            -Wshadow \
            -fsanitize=address,undefined \
            -DLOCAL \
            -o "$OUT"

        if [[ -n "$TIME_LIMIT" ]]; then
            timeout "$TIME_LIMIT" "./$OUT" < input.txt > output.txt
        else
            "./$OUT" < input.txt > output.txt
        fi
        ;;

    py)
        if [[ -n "$TIME_LIMIT" ]]; then
            timeout "$TIME_LIMIT" python3 "$FILE" < input.txt > output.txt
        else
            python3 "$FILE" < input.txt > output.txt
        fi
        ;;

    *)
        echo "Unsupported file type: $FILE" >&2
        exit 1
        ;;
esac