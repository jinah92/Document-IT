const curry = (f) => (a, ..._) => (_.length ? f(a, ..._) : (..._) => f(a, ..._));
// 인자가 2개 이상이면, 즉시 실행
// 2개보다 작다면 다시 함수를 리턴해서 이후에 받은 인자를 합쳐서 함수를 실행

const mult = curry((a, b) => a * b);
console.log(mult(3)(2)); //6

const mult3 = mult(3);
console.log(mult3(10)); //3*10
console.log(mult3(5)); //3*5
