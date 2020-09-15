#!/usr/bin/node
const j = process.argv[2];
const string = 'C is fun';
if (isNaN(j)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < j; x++) {
    console.log(string);
  }
}
