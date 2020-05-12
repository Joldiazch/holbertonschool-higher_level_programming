#!/usr/bin/node

/* script that prints the title of a Star Wars movie
where the episode number matches a given integer. */

const request = require('request');

const myArgs = process.argv.slice(2);
const movieId = myArgs[0];
request(
  `https://swapi-api.hbtn.io/api/films/${movieId}`,
  function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const filmObj = JSON.parse(body);
      console.log(filmObj.title);
    }
  });
