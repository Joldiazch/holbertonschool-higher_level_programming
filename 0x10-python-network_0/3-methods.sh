#!/bin/bash
# script that displays the method
curl -sI 0.0.0.0:5000/route_4 | grep 'Allow: ' | cut -d " " -f2-
