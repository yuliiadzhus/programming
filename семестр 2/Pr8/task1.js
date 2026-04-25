const targetNumber = Math.floor(Math.random() * 100) + 1;
let guess = null;
let attempts = 0;

console.log("Гра 'Вгадай число' розпочата!");

while (guess !== targetNumber) {
    guess = parseInt(prompt("Вгадайте число від 1 до 100:"));
    attempts++;

    if (isNaN(guess)) {
        alert("Будь ласка, введіть число!");
    } else if (guess < targetNumber) {
        alert("Загадане число більше.");
    } else if (guess > targetNumber) {
        alert("Загадане число менше.");
    } else {
        alert(`Вітаю! Ви вгадали число ${targetNumber} за ${attempts} спроб.`);
    }
}