#!/usr/bin/node
// script that prints x times “C is fun”
if (!isNaN(parseInt(process.argv[2]))) {
  let n = process.argv[2];
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
