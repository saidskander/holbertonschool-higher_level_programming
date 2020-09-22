#!/usr/bin/node
// display the status code of a GET request.

const request = require('request');

const urlrequest = `${process.argv[2]}`;
request(urlrequest, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
