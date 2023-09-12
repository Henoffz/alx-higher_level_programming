#!/usr/bin/node
exports.esrever = function (list) {
  const updatedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    updatedList.push(list[i]);
  }
  return updatedList;
};
