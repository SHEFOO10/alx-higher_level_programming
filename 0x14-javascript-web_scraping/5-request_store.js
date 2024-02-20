#!/usr/bin/node
const fs = require('fs');

const url = process.argv[2];
const request = require('request');

try {
  request.get(url, (err, response, body) => {
    if (err) {
      console.error(err);
    } else {
      fs.writeFileSync(process.argv[3], body, 'utf-8');
    }
  });
} catch (err) {
  console.error(err);
}
