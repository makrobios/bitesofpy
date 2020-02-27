#!/bin/bash
file=$1
if [ ! -f $file ];then
	touch $file test/test_$file;
fi;
