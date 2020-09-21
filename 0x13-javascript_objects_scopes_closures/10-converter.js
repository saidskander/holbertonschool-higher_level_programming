#!/usr/bin/node

exports.converter = function (base) {
  return function (output) {
    return output.toString(base);
  };
};
