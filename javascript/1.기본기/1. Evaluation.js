const a = 10;
const add10 = (a) => a + 10;
const r = add10(a);

console.log(r);

/* 일급함수 */
const add5 = (a) => a + 5;
console.log(add5);
console.log(add5(5));

const f1 = () => () => 1;
console.log(f1());

const f2 = f1();
console.log(f2);
console.log(f2());

/* 고차 함수 */
// 함수를 인자로 받아서 실행하는 함수
const apply1 = (f) => f(1);
const add2 = (a) => a + 2;
console.log(apply1(add2));
console.log(apply1((a) => a - 1));

const times = (f, n) => {
  let i = -1;
  while (++i < n) f(i);
};

times(console.log, 3);
times((a) => console.log(a + 10), 3);

// 함수를 만들어 리턴하는 함수
// (클로저를 만들어 리턴하는 함수)
const addMaker = (a) => (b) => a + b;
const add3 = addMaker(10);
console.log(add3(5));
