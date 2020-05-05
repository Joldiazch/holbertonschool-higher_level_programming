#!/usr/bin/node

/* script that prints the addition of 2 integers */
const myArgs = process.argv.slice(2);

function add (a, b) {
  console.log(a + b);
}

add(parseInt(myArgs[0], 10), parseInt(myArgs[1], 10));
