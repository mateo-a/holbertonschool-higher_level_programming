#!/usr/bin/node
const fs = require('fs');
function readWrite (Origin, Dest) {
  fs.readFile(Origin, 'utf8', function (err, data) {
    if (err) {
      return console.log(err);
    }
    fs.appendFile(Dest, data + '\n', 'utf8', function (err) {
      if (err) {
        return console.log(err);
      }
    });
  });
}

readWrite(process.argv[2], process.argv[4]);
readWrite(process.argv[3], process.argv[4]);
