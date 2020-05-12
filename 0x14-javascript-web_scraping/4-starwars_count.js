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
      const movies = JSON.parse(body).results;
      const filmsWithWedgeAntilles = [];
      movies.forEach(movie => {
        const characters = movie.characters;
        characters.forEach(urlCharacter => {
          if (urlCharacter === 'https://swapi-api.hbtn.io/api/people/18/') {
            filmsWithWedgeAntilles.push(movie);
          }
        });
      });
      console.log(filmsWithWedgeAntilles.length);
    }
  });
