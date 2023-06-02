
<!--    function getTodo(){-->
<!--        var note = localStorage.getItem('todo');-->
<!--        document.getElementById('todoList').innerHTML = note;-->
<!--    }-->
    function saveTodo(){
        var todo = document.getElementById("todoList").innerHTML;
        localStorage.setItem('todo', todo);
        <!--localStorage.setItem(키,값)-->
    }

    function removeTodo(text){
        console.log('remove Todo');
        localStorage.removeItem('todo');
        var removeOne = text.target.parentElement;
        removeOne.remove();
    }
    function allClear(){
        console.log('All CLEAR');
        localStorage.clear();
        document.getElementById('todoList').innerHTML = '';
        document.getElementById('addTodoList').innerHTML = '';
    }
    function addTodo() {
        var listValue = document.getElementById('todoList').innerHTML;
        var addList = document.getElementById('addTodoList');
        var item = document.createElement('li');

        item.innerText = listValue;
        item.classList.add('list-group-item');

        var removeButton = document.createElement('button');
        removeButton.innerText = 'Remove';
        removeButton.classList.add('btn', 'btn-danger', 'btn-sm');
        removeButton.addEventListener('click', removeTodo);

        item.appendChild(removeButton);
        addList.appendChild(item);
    }