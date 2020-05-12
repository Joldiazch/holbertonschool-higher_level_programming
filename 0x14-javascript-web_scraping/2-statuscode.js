#!/usr/bin/node

/* script that display the status code of a GET request */
const request = require('request');
const myArgs = process.argv.slice(2);
const urlToRequest = myArgs[0];
request
  .get(urlToRequest)
  .on('response', function (response) {
    console.log(`code: ${response.statusCode}`);
  });
