#!/usr/bin/node
// Script that Writes a string to a file.

const fs = require('fs');

fs.writeFile(`${process.argv[2]}`, `${process.argv[3]}`, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
