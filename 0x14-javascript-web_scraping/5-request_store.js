#!/usr/bin/node

/*  a script that writes a string to a file. */
const myArgs = process.argv.slice(2);
const fs = require('fs');
const request = require('request');
const [url, fileName] = myArgs;

request(
  url,
  function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      fs.writeFile(fileName, body, 'utf-8', (err) => {
        if (err) console.log(err);
      });
    }
  });
