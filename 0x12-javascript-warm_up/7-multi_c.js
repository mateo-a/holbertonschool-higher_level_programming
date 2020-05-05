#!/usr/bin/node
// script that prints x times “C is fun”
const n = parseInt(process.argv[2], 10);
if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < n; i += 1) {
    console.log('C is fun');
  }
}
