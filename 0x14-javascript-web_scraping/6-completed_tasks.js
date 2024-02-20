#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request('https://jsonplaceholder.typicode.com/users', 'utf-8', (err, response, body) => {
  let users, todos;
  if (err) {
    console.error(err);
  } else {
    users = JSON.parse(body);
    todos = {};
    users.forEach((user) => {
      request(url + `?userId=${user.id}`, (err, response, body) => {
        if (err) { console.error(err); } else { todos = JSON.parse(body); console.log(todos); }
      });
    });
  }
});
