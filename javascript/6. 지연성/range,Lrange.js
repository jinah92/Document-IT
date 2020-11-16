const add = (a, b) => {
  return a + b;
};

/* range */
const range = (l) => {
  let i = -1;
  let res = [];
  while (++i < l) {
    res.push(i);
  }

  return res;
};

console.log(range(5));
// [0, 1, 2, 3, 4]

console.log(range(2));
//  [0,1]

var list = range(4);

console.log(list.reduce(add));
// 0+1+2+3

/* 느긋한 L.range */
const L = {};
L.range = function* (l) {
  let i = -1;
  while (++i < l) {
    yield i;
  }

  //   return res;
};

var list2 = L.range(4);
console.log(list2);
// console.log(list2.reduce(add));
// console.log(list2.reduce(add));

/* test (효율성 테스트)*/
function test(name, time, f) {
  console.time(name);
  while (time--) f();
  console.timeEnd(name);
}

test("range", 10, () => range(10000000).reduce(add));
