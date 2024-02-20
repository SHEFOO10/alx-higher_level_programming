#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const res = JSON.parse(body).results;
    let numberOfMovies = 0;
    res.forEach((movie) => {
      numberOfMovies += movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
    });
    console.log(numberOfMovies);
  }
});
