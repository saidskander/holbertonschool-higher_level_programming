#!/usr/bin/node
//  prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const urlrequests = "http://swapi.co/api/vehicles/${process.argv[2]}";
request(urlrequests, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
