const take = (l, iter) => {
  let res = [];
  for (const a of iter) {
    res.push(a);
    if (res.length == l) return res;
  }

  return res;
};

console.log(take(5, range(100)));
console.log(take(5, L.range(100)));

/* range */
const range = (l) => {
  let i = -1;
  let res = [];
  while (++i < l) {
    res.push(i);
  }

  return res;
};
/* 느긋한 L.range */
const L = {};
L.range = function* (l) {
  let i = -1;
  while (++i < l) {
    yield i;
  }

  //   return res;
};
