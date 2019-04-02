#!/bin/sh

django-admin datagenerator tumorassessment -a "Aurora Health Care" -c 10000
django-admin datagenerator tumorstaging -a "Aurora Health Care" -c 10000
django-admin datagenerator encounter -a "Aurora Health Care" -c 10000
django-admin datagenerator patient -a "Aurora Health Care" -c 10000
django-admin datagenerator careprovider -a "Aurora Health Care" -c 10000
