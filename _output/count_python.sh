#!/bin/bash
count=0
for file in *.csv; do
    file_count=$(grep -i "python" "$file" | wc -l)
    count=$((count + file_count))
done
echo "Number of lines containing 'python' in CSV files: $count"
