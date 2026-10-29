function division(arr) {
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] % 3 == 0) {
      console.log(arr[i]);
    } else {
      continue;
    }
  }
}

var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
division(arr);

