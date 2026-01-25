#!/bin/bash


g++ -std=c++17 -O2 "$1" -o generator
g++ -std=c++17 -O2 "$2" -o brute
g++ -std=c++17 -O2 "$3" -o actual


while true; do
    
    ./generator > input.txt

    brute_out=$(./brute < input.txt)
    actual_out=$(./actual < input.txt)

    if [ "$brute_out" != "$actual_out" ]; then
        echo "❌ Outputs do not match!"
        echo
        echo "Brute force output:"
        echo "$brute_out"
        echo
        echo "Actual output:"
        echo "$actual_out"
        break
    fi
done
