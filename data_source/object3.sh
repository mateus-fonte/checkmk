#!/usr/bin/bash

metrics_json=$(curl -s http://localhost:9001/get_metrics/object3)

size=$(echo "$metrics_json" | jq -r ".size")
weight=$(echo "$metrics_json" | jq -r ".weight")
status=$(echo "$metrics_json" | jq -r ".status")
quantity=$(echo "$metrics_json" | jq -r ".quantity")


echo "<<<local>>>"
echo "$status Object3 size=$size|weight=$weight|quatity=$quantity Description for the Object3"
