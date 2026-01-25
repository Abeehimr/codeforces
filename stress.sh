#! /bin/bash

while true; do
    python t.py > input.txt

    brute=$(python $1 < input.txt)
    actual=$(python $2 < input.txt)

    if [ "$brute" != "$actual" ]; then
        echo "Outputs not match:"
        echo "Brute force output:"
        echo "$brute"
        echo "Actual output:"
        echo "$actual"
        break
    fi
done
