#!/usr/bin/node

let login = 0;
exports.logMe = function (item) {
  console.log(`${login}: ${item}`);
  login++;
};
