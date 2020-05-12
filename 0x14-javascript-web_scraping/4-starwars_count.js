#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    let count = 0;
    for (const response of JSON.parse(body).results) {
      for (const character of response.characters) {
        if (character.includes('18')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
