#!/usr/bin/env bash

s3_files=$(aws s3 ls s3://syapse-performance-results/Test_Upload/ | grep )