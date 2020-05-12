#!/usr/bin/node

/* a script that reads and prints the content of a file */
const myArgs = process.argv.slice(2);
const fs = require('fs');
const fileName = myArgs[0];
fs.readFile(fileName, 'utf-8', (err, data) => {
  console.log(err || data.toString());
});
