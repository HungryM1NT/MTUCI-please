import { useState, useEffect } from 'react';
import './App.css';
import React, { Component } from 'react';

 

export default function App() {
/*
  const [newItem, setNewItem] = useState("")
  const [todos, setTodos] = useState([])

  function handleSubmit(e) {
    e.preventDefault()

    setTodos(currentTodos => {
      return [
        ...currentTodos,
        { id: crypto.randomUUID(), title: newItem, completed:
        false },
      ]
    })

    setNewItem("")
  }

  function toggleTodo(id,completed) {
    setTodos(currentTodos => {
      return currentTodos.map(todo => {
        if (todo.id === id) {
          return { ...todo, completed}
        }

        return todo
      })
    })
  }

  function deleteTodo(id) {
    setTodos(currentTodos => {
      return currentTodos.filter(todo => todo.id !== id)
    })
  }
*/
  return (
  <>
  <div className='game'>
    <div className='header'></div>
    <div className='gameArea'>
      <div className='window'>
        <div className='person'></div>
      </div>
      <div className='table'>
        <div className='docs'>
          <div className='pass'></div>
          <div className='uniID'></div>
          <div className='passport'></div>
        </div>
        <div className='buttons'>
          <button className='btnY'>Approve</button>
          <button className='btnN'>Deny</button>
        </div>
      </div>
    </div>
  </div>
  </>
  )
} 

/* 

   <form onSubmit={handleSubmit} className="new-item-form">
    <div className="form-row">
    </div>

  </form>
<ul className='list'>
{todos.length === 0 && "No Todos"}
{todos.map(todo => {
  return (
    <li kewy={todo.id}>
    <label>
      <input type='checkbox' checked={todo.completed}
      onChange={e => toggleTodo(todo.id, e.target.checked)} />
      {todo.title}
    </label>
    <button onClick={() => deleteTodo(todo.id)} className='btn btn-danger'>Delete</button>
  </li>
)
})}
</ul>*/