#!/bin/bash
# Foobar Teleprompter

env | grep NOTIFY_ | sort > $OMD_ROOT/tmp/foobar.out
echo "Succesfully written $OMD_ROOT/tmp/foobar.out"
exit 0
