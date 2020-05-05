#!/usr/bin/node

/* script that searches the second
biggest integer in the list of arguments */
var myArgs = process.argv.slice(2);

if (myArgs.length > 1) {
  myArgs.sort(function (a, b) {
    return b - a;
  });
  console.log(myArgs[1]);
} else {
  console.log(0);
}
