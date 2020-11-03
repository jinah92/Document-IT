function* gen() {
  yield 1;
  yield 2;
  yield 3;
  return 100;
}

let iter = gen();
console.log(iter[Symbol.iterator]() == iter);
console.log(iter.next());
console.log(iter.next());
console.log(iter.next());
console.log(iter.next());

for (const a of gen()) console.log(a);

/*
제너레이터를 이용하여,
홀수만 순회하기
*/
// 하드 코딩
function* odds() {
  yield 1;
  yield 3;
  yield 5;
  yield 7;
}

//  사용자 입력값에 따라 자동화
function* odds2(l) {
  for (let i = 0; i < l; i++) {
    if (i % 2) yield i;
  }
}

let iter2 = odds(10);
for (const a of odds(10)) console.log(a);
for (const a of odds2(10)) console.log(a);
