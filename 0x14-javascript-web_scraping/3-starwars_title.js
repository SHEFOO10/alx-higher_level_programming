#!/usr/bin/node

const request = require('request');

request.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (err, response, body) => {
  if (err) { console.error(err); } else { console.log(JSON.parse(body).title); }
});
