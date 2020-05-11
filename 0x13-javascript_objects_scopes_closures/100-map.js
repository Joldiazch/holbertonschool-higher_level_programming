#!/usr/bin/node

/* function that converts a number
from base 10 to another base passed as argument */

const list = require('./100-data.js').list;
console.log(list);
let index = -1;
console.log(list.map(num => {
  index += 1;
  return num * index;
}));
