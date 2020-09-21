#!/usr/bin/node

const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c == null) {
      c = 'X';
    }
    for (let x = 0; x < this.height; x++) {
      for (let y = 0; y < this.width; y++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
};
