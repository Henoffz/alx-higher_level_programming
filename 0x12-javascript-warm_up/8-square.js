#!/usr/bin/node
let arg1 = process.argv[2];
if (!arg1 || isNaN(arg1)) {
  console.log('Missing size');
} else {
  arg1 = parseInt(arg1);
  for (let i = 0; i < arg1; i++) {
    console.log('X'.repeat(arg1));
  }
}
