const counterText = document.getElementById('counter');
const btnMinus = document.getElementById('btn-minus');
const btnPlus = document.getElementById('btn-plus');

let count = 0;

btnPlus.onclick = function() {
    count++;
    counterText.innerText = count;
};

btnMinus.onclick = function() {
    count--;
    counterText.innerText = count;
};