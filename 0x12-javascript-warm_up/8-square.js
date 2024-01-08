#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (x) {
  let row = '';
  for (let i = 0; i < x; i++) {
    row += 'X';
  }
  for (let i = 0; i < x; i++) {
    console.log(row);
  }
} else {
  console.log('Missing size');
}
