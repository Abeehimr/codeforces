#!/bin/bash

src="tem.py"
[ "$1" == "ac" ] && src="ac.py"

for f in {A..F}; do
    cp "$src" "$f.py"
done