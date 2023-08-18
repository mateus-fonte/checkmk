#!/usr/bin/bash

interface_count=$(ls /sys/class/net | wc -l)

echo "P \"Number of network interfaces\" nets=$interface_count;2;5 O numero total de interfaces e $interface_count \n Essa linha e apenas para efeitos ilustrativos"
