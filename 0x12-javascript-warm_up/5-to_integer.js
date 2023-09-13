#!/usr/bin/node
let arg1 = process.argv[2];
if (!arg1 || isNaN(arg1)) {
  console.log('Not a number');
} else {
  arg1 = parseInt(arg1);
  console.log('My number: ' + arg1);
}
