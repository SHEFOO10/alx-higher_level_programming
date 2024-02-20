#!/usr/bin/node
const fs = require('fs');
const process = require('process');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (data) {
    console.log(data);
  } else {
    console.log(err);
  }
});
