#!/usr/bin/node

/* function that converts a number
from base 10 to another base passed as argument */

const dict = require('./101-data').dict;
const listValues = Object.values(dict);
const listKeys = Object.keys(dict);
const dictOut = {};
listValues.map(value => {
  dictOut[value] = listKeys.filter(key => dict[key] === value);
});
console.log(dictOut);
