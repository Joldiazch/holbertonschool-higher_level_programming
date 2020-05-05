#!/usr/bin/node

/* script that prints
the first argument passed to it */

const myArgs = process.argv.slice(2);

console.log(myArgs[0] ? myArgs[0] : 'Argument found');
