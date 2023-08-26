// Step 3: Get references to the elements in the HTML
const newTaskInput = document.getElementById('newTask');
const addTaskButton = document.getElementById('addTaskButton');
const taskList = document.getElementById('taskList');
const radioClear = document.getElementById('clear');
const taskRadio = document.getElementById('newRadio')
// Step 4: Create an event listener for the "Add Task" button
addTaskButton.addEventListener('click', addTask);
radioClear.addEventListener("click",resetRadio)
// Step 5: Define the addTask function
function addTask() {
  const taskText = newTaskInput.value.trim();

  if (taskText !== '') {
    const taskItem = createTaskItem(taskText);
    taskList.appendChild(taskItem);
    newTaskInput.value = '';
  }
}

// Step 6: Define the createTaskItem function
function createTaskItem(taskText) {
  const taskItem = document.createElement('li');
  const taskTextElement = document.createElement('span');
  const deleteButton = document.createElement('button');

  taskTextElement.innerText = taskText;
  deleteButton.innerText = 'Delete';
  deleteButton.classList.add('delete-button');

  // Step 7: Add event listener for the delete button
  deleteButton.addEventListener('click', () => {
    taskItem.remove();
  });

  // Step 8: Add event listener for marking task as completed
  taskTextElement.addEventListener('click', () => {
    taskTextElement.classList.toggle('completed');
  });

  taskItem.appendChild(taskTextElement);
  taskItem.appendChild(deleteButton);

  return taskItem;
}
function resetRadio(){
	taskRadio.checked=false;
}