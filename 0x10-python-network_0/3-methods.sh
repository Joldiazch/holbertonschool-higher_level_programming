#!/bin/bash
# script that displays the method
curl -sI $1 | grep 'Allow: ' | cut -d " " -f2-
