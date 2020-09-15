#!/usr/bin/node
const j = process.argv[2];
if (isNaN(j)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < j; x++) {
    console.log('X'.repeat(j));
  }
}
