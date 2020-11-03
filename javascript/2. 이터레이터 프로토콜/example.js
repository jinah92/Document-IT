// 기존의 순회방식
const list = [1, 2, 3];
for (var i = 0; i < list.length; i++) {
  console.log(list[i]);
}

const str = "abc";
for (var i = 0; i < str.length; i++) {
  console.log(str[i]);
}

// ES6
for (const a of list) {
  console.log(a);
}

for (const a of str) {
  console.log(a);
}

/* Array, Set, Map을 통한 리스트 순회*/
console.log("Arr--------");
const arr = [1, 2, 3];
for (const a of arr) console.log(a);

console.log("Set--------");
const set = new Set([1, 2, 3]);
for (const a of set) console.log(a);

console.log("Map--------");
const map = new Map([
  ["a", 1],
  ["b", 2],
  ["c", 3],
]);
for (const a of map) console.log(a);

// key 값만 순회
for (const a of map.keys()) console.log(a);
// value 값만 순회 (iterator)
for (const a of map.values()) console.log(a);
// key, values 모두 순회
for (const a of map.entries()) console.log(a);
