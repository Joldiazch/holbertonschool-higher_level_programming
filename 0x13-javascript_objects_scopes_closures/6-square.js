#!/usr/bin/node

/* class Square that defines a square
and inherits from Rectangle of 4-rectangle.js */

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
