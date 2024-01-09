#!/usr/bin/node

const oldSquare = require('./5-square');

class Square extends oldSquare {
  charPrint (c) {
    let text = '';

    for (let j = 0; j < this.width; j++) {
      text += c ?? 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(text);
    }
  }
}

module.exports = Square;
