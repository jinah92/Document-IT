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
