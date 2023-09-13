#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const numbers = args.map(num => parseInt(num));
  const sortedNumbers = numbers.sort((a, b) => b - a);
  const secondLargest = sortedNumbers[1];
  console.log(secondLargest || 0);
}
