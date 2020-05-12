#!/usr/bin/node
exports.esrever = function (list) {
  return list.map((value, key) => list[list.length - 1 - key]);
};
