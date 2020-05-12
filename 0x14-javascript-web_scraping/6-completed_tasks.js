#!/usr/bin/node

/* script that prints the title of a Star Wars movie
where the episode number matches a given integer. */

const request = require('request');

const myArgs = process.argv.slice(2);
const apiUrl = myArgs[0];
request(
  apiUrl,
  function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const allObjects = JSON.parse(body);
      const info = {};
      allObjects.forEach(obj => {
        if (info[obj.userId]) {
          obj.completed ? info[obj.userId] += 1 : info[obj.userId] += 0;
        } else if (obj.completed) {
          info[obj.userId] = 1;
        }
      });
      console.log(info);
    }
  });
