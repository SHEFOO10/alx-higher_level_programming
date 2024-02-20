#!/usr/bin/node

const request = require('request');

request.get('https://swapi-api.alx-tools.com/api/films/', (err, response, body) => {
  if (err) {
	  console.error(err);
  } else {
	  res = JSON.parse(body).results;
	  let number_of_movies = 0;
	  res.forEach((movie) => {
      number_of_movies += movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
	  });
	  console.log(number_of_movies);
  }
});
