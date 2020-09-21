#!/usr/bin/node

exports.esrever = function (list) {
  let leftreverse = 0;
  let rightreverse = list.length - 1;
  while (leftreverse <= rightreverse) {
    const temp = list[rightreverse];
    list[rightreverse] = list[leftreverse];
    list[leftreverse] = temp;
    leftreverse++;
    rightreverse--;
  }
  return (list);
};
