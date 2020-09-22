#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles”
const request = require('request');

request(process.argv[2], function (err, res, body) {
  let i = 0;
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  for (let x = 0; json.results[x] !== undefined; x++) {
    if (json.results[x].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      i++;
    }
  }
  console.log(i);
});
