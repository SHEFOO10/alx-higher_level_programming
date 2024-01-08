#!/usr/bin/node

const arr = process.argv.slice(2).map(element => parseInt(element));
if (arr.length > 1) {
  const newArray = arr.filter(element => element !== Math.max(...arr));
  console.log(Math.max(...newArray));
} else {
  console.log(0);
}
