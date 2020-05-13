#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  const info = {};
  console.log(typeof info);
  if (!error) {
    for (const task of JSON.parse(body)) {
      if (task.completed === true) {
        if (!Object.hasOwnProperty.call(info, task.userId)) {
          info[task.userId] = 1;
        } else {
          info[task.userId]++;
        }
      }
    }
    console.log(info);
  }
});
