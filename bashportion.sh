#!/bin/bash
fn=$1
if [ "$fn" == '' ] || [ ${fn##*.} != 'pbd' ]
then
echo "please provide filename argument"
else
grep ^ATOM $fn > temp
#echo $res
awk -F ' ' '{print $7,$8,$9}' temp
rm temp
fi
