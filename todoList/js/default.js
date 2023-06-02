var todoArr = []
var todoArr2 = []

function getTodo() {
//로컬 스토리지에서 todoArr2을 불러와 보여주고 싶다.
    var note = localStorage.getItem('todoArr2');
    var noteSplit = note?.split(',') || [];
    noteSplit.forEach((noteText) => {
        renderItem(noteText);
    });
}

function setTodo() {
    var listValue = document.getElementById('todoList').innerHTML;
    todoArr.push(listValue);
    todoArr2 = JSON.stringify(todoArr);
    //전역 array로 localStorage 저장
    localStorage.setItem('todoArr2', todoArr2);
}

function removeTodo(text) {
    console.log('remove Todo');
    localStorage.removeItem('todo');
    var removeOne = text.target.parentElement;
    removeOne.remove();
}

function allClear() {
    console.log('All CLEAR');
    localStorage.clear();
    document.getElementById('todoList').innerHTML = '';
    document.getElementById('addTodoList').innerHTML = '';
}

function renderItem(todoText) {
    var addList = document.getElementById('addTodoList');
    var item = document.createElement('li');

    item.innerText = todoText;
    item.classList.add('list-group-item');

    var removeButton = document.createElement('button');
    removeButton.innerText = 'Remove';
    removeButton.classList.add('btn', 'btn-danger', 'btn-sm');
    removeButton.addEventListener('click', removeTodo);

    item.appendChild(removeButton);
    //List에 아이템 추가
    addList.appendChild(item);
}

function addTodo() {
    var todoText = document.getElementById('todoList').innerHTML;

    if (todoText !== '') {
        //Todo localStorage 저장
        setTodo();
        renderItem(todoText);

        //입력창 초기화
        document.getElementById('todoList').innerHTML = '';
    }
}