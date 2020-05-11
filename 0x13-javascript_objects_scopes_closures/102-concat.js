#!/usr/bin/node

/*  script that concats 2 files.

The first argument is the file path of the first source file
The second argument is the file path of the second source file
The third argument is the file path of the destination */
const myArgs = process.argv.slice(2);
const fs = require('fs');

fs.readFile(myArgs[0], 'utf-8', (err, datafileA) => {
  if (err) console.log(err);
  fs.readFile(myArgs[1], 'utf-8', (err, datafileB) => {
    if (err) console.log(err);
    fs.writeFile(myArgs[2], datafileA + datafileB, (err) => {
      if (err) console.log(err);
    });
  });
});
