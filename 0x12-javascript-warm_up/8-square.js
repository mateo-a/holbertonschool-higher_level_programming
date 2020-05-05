#!/usr/bin/node
// script that prints a square
const n = parseInt(process.argv[2], 10);
if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i += 1) {
    console.log('X'.repeat(n));
  }
}
