#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const count = [...list].filter(x => x === searchElement).length;
  return count;
};
