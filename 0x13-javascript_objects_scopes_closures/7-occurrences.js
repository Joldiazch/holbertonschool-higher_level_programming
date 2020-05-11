#!/usr/bin/node

/*  function that returns the number of occurrences in a list */

exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  list.map(num => {
    if (num === searchElement) {
      occurences++;
    }
  });
  return occurences;
};
