#!/usr/bin/node

/* function that prints the number of
arguments already printed and the new argument value */
var numArgPrinted = 0;
exports.logMe = function (item) {
  console.log(numArgPrinted + ': ' + item);
  numArgPrinted++;
};
