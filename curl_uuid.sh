#!/usr/bin/env bash

echo "Param \$1: $1"
echo "Param \$2: $2"
echo "Param \$3: $3"

curl -X POST "$1" -H "accept: */*" -H "Content-Type: application/json" -d "$2" | jq $3 | tr -d \" 
