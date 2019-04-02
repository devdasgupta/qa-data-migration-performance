#!/usr/bin/env bash

logfile="process_id"
for i in $(cat $logfile)
do
	echo "killing process $i"
	kill -9 $i
done

echo > $logfile
rm $logfile

prpid=$(ps -fe | grep -i run | awk '{print $2}')
echo "killing process $prpid"
kill -9 $prpid
ps -fe | grep -v grep | grep -i run
