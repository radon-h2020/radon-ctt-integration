#!/usr/bin/env bash

echo $(curl -X POST "$1" -H 'accept: */*' -H 'Content-Type: application/json' -d "$2" | jq .uuid)
