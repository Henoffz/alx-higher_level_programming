#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

let arg1 = process.argv[2];
let arg2 = process.argv[3];

arg1 = parseInt(arg1);
arg2 = parseInt(arg2);

add(arg1, arg2);
