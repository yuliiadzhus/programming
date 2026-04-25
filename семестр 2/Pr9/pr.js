const taskForm = document.getElementById('task-form');
const tasksContainer = document.getElementById('tasks-container');

// Завантаження даних з LocalStorage
let tasks = JSON.parse(localStorage.getItem('myTasks')) || [];
renderTasks();

taskForm.onsubmit = (e) => {
    e.preventDefault();

    const now = new Date();
    const timeString = `${now.getHours()}:${now.getMinutes().toString().padStart(2, '0')}`;

    const newTask = {
        id: Date.now(),
        name: document.getElementById('task-name').value,
        category: document.getElementById('task-category').value,
        time: timeString
    };

    tasks.push(newTask);
    saveAndRender();
    taskForm.reset();
};

function saveAndRender() {
    localStorage.setItem('myTasks', JSON.stringify(tasks));
    renderTasks();
}

function renderTasks() {
    tasksContainer.innerHTML = '';
    tasks.forEach(task => {
        const card = document.createElement('div');
        card.className = 'task-card';
        card.innerHTML = `
            <h3>${task.name}</h3>
            <p>Категорія: ${task.category}</p>
            <p><small>Створено: ${task.time}</small></p>
            <button class="delete-btn" onclick="deleteTask(${task.id})">Видалити</button>
        `;
        tasksContainer.appendChild(card);
    });
}

window.deleteTask = (id) => {
    tasks = tasks.filter(task => task.id !== id);
    saveAndRender();
};