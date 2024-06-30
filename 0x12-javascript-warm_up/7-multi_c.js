#!/usr/bin/node
const message = 'C is fun';
const x = Math.floor(Number(process.argv[2]));
let i;
if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (i = 0; i < x; i++) {
    console.log(message);
  }
}
