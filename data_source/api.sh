#!/usr/bin/bash

metrics_json=$(curl -s http://localhost:9001/get_metrics/object1)

size=$(echo "$metrics_json" | jq -r ".size")
weight=$(echo "$metrics_json" | jq -r ".weight")
status=$(echo "$metrics_json" | jq -r ".status")
quantity=$(echo "$metrics_json" | jq -r ".quantity")

echo "<<<http>>>"
echo "HTTP OK: Object1 metrics retrieved | size=$size; weight=$weight; status=$status; quatity=$quantity"
