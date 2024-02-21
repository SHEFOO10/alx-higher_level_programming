#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], (err, response, body) => {
  let numberOfMovies = 0;
  if (err) {
    console.error(err);
  } else {
    const res = JSON.parse(body).results;
    for (const movie of res) {
      if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18') || movie.characters.includes('http://swapi.co/api/people/18/')) { numberOfMovies++; }
    }
    console.log(numberOfMovies);
  }
});
