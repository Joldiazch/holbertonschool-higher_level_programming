#!/usr/bin/node

/* script that prints a message
depending of the number of arguments passed */

const myArgs = process.argv.slice(2).length;

console.log(myArgs === 0 ? 'No argument' : myArgs === 1 ? 'Argument found' : 'Arguments found');
