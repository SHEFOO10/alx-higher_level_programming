#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

try {
  request.get(url)
    .on('response', function (response) {
      console.log(`code: ${response.statusCode}`);
    });
} catch (err) {
  console.error(err);
}
