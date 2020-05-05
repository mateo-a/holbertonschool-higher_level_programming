#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
const num = process.argv.slice(2);
if (num.length < 2) {
  console.log(0);
} else {
  num.sort((a, b) => a - b);
  num.pop();
  console.log(num.pop());
}
