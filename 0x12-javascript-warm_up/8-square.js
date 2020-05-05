#!/usr/bin/node

/* script that prints a square */
const myArgs = process.argv.slice(2);
const size = parseInt(myArgs[0], 10);

if (size) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
