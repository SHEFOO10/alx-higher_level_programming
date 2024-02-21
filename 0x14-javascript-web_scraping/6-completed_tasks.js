#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, 'utf-8', (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const obj = {};
    const todos = JSON.parse(body);
    for (const todo of todos) {
      const userId = todo.userId.toString();
      if (todo.completed === false) { continue; }
      if (userId in obj) { obj[userId]++; } else { obj[userId] = 1; }
    }
    console.log(obj);
  }
});
