#!/usr/bin/node
const fs = require('fs');

const filename = process.argv[2] ? process.argv[2] : '' 
fs.readFile(filename, 'utf8', (err, data) => {
  if (data) {
    console.log(data);
  } else {
    console.log(err);
  }
});
