let number = 5674;

function calculateSum(num) {
    let strNum = num.toString();
    let sum = 0;
    for (let i = 0; i < strNum.length; i++) {
        sum += Number(strNum[i]);
    }
    return sum;
}

console.log(`Сума цифр числа ${number} дорівнює: ${calculateSum(number)}`);