#!/usr/bin/node

/* script that prints a message
depending of the number of arguments passed */

const myArgs = process.argv.slice(2);

console.log(myArgs.length ? 'Argument found' : 'No argument');
