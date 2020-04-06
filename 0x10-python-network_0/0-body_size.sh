#!/bin/bash
# script that displays the size of the body of the response
curl -sI $1 | grep Content-Length | grep -o '[0-9]*'
