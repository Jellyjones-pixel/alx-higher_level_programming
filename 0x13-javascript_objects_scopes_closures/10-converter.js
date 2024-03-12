#!/usr/bin/node

exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
/*
John Mbithi Mutave
jellyjones-pixel
johnmbithimutave@gmail.com
*/