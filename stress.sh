#! /bin/bash

while true; do
    python $1 > input.txt

    brute=$(python $2 < input.txt)
    actual=$(python $3 < input.txt)

    if [ "$brute" != "$actual" ]; then
        echo "Outputs not match:"
        echo "Brute force output:"
        echo "$brute"
        echo "Actual output:"
        echo "$actual"
        break
    fi
done
