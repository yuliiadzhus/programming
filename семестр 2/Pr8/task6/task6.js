const btn = document.getElementById('colorBtn');
const text = document.getElementById('text');

btn.addEventListener('click', () => {
    const randomColor = () => `#${Math.floor(Math.random()*16777215).toString(16)}`;
    
    document.body.style.backgroundColor = randomColor();
    text.style.color = randomColor();
});