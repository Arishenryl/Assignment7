#!/bin/bash
#Atomcoordinates-Assignment7
#Liann Aris-Henry-04/04/2023
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
