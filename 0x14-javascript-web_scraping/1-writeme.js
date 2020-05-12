#!/usr/bin/node

/*  a script that writes a string to a file. */
const myArgs = process.argv.slice(2);
const fs = require('fs');
const [fileName, stringToWrite] = myArgs;
fs.writeFile(fileName, stringToWrite, 'utf-8', (err) => {
  if (err) console.log(err);
});
