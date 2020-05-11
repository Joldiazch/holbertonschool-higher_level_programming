#!/usr/bin/node

/* function that returns the reversed version of a list */

exports.esrever = function (list) {
  const litsOut = [];
  for (let i = list.length - 1; i >= 0; i--) {
    litsOut.push(list[i]);
  }
  return litsOut;
};
