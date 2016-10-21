#!/bin/script

myssid=$(iwgetid -r)
echo $myssid > Essid.txt
