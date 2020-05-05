#!/usr/bin/node

/* script that prints
My number: <first argument converted in integer> */

const myArgs = process.argv.slice(2);
const firstArg = parseInt(myArgs[0], 10);
console.log(firstArg ? 'My number: ' + firstArg : 'Not a number');
