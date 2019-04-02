#!/usr/bin/env bash

logfile="process_id"

function execute_python(){
    python send_data_graphite.py
    sleep 1
    python send_di_data.py
}

# Code to execute the python script again and again
while [ true ]; do
    execute_python &
    p_id=$!
    echo $p_id > $logfile
    sleep 9
done
