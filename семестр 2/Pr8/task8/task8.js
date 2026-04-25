const btn = document.querySelector('button');
const text = document.getElementById('text');

btn.onclick = () => {
    if (text.style.visibility === "hidden") {
        text.style.visibility = "visible";
    } else {
        text.style.visibility = "hidden";
    }
};