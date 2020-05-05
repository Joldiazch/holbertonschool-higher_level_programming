#!/usr/bin/node

/* script that prints x times “C is fun" */
const myArgs = process.argv.slice(2);
const x = myArgs[0];
if (x) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
