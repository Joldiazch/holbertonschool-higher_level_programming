#!/bin/bash
# script that displays the http status
curl -s -o res/dev/null -w "%{http_code}" $1
