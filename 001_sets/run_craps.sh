#!/bin/bash

for i in $(seq -s' ' 1000); do
  python craps.py > /dev/null
  if [ $? == 0 ]; then
    echo 'won'
  else
    echo 'lost'
  fi
done | grep -c won
