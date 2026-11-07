
//E1
for (var i =1; i<=20; i++) {
    console.log(i);
}

//E2
for(var i=1; i<100; i++) {
    if(i % 3 == 0) {
        console.log(i);
    }
}
//3
var arr = [4, 2.5, 1, -0.5, -2, -3.5];

for(var i=1; i<arr.length; i++) {
    console.log(arr[i]);
}


//4
var sum = 0;

for (var i = 1; i <= 100; i++) {
    sum += i;
}

console.log(sum);

//5
var product=1;
for(var i =1; i<=12; i++) {
    product = product * i;
}
console.log(product); 