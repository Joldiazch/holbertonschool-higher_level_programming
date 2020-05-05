#!/usr/bin/node

/* script that prints the addition of 2 integers */
const myArgs = process.argv.slice(2);

function fact (n) {
  if (!n && n <= 1) {
    return 1;
  } else {
    return fact(n - 1) * n;
  }
}
const firstArg = parseInt(myArgs[0], 10);
if (firstArg) { console.log(fact(firstArg)); } else { console.log(1); }
