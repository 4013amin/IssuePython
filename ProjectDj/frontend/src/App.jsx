import { useState, useEffect } from 'react'
import TodoForm from './components/TodoForm'
import TodoList from './components/TodoList'
import FilterButtons from './components/FilterButtons'
import { getTodos, createTodo, updateTodo, deleteTodo } from './services/api'
import './App.css'

function App() {
  const [todos, setTodos] = useState([])
  const [filter, setFilter] = useState('all')
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetchTodos()
  }, [])

  const fetchTodos = async () => {
    try {
      setLoading(true)
      const data = await getTodos()
      setTodos(data)
      setError(null)
    } catch (err) {
      setError('خطا در دریافت تسک‌ها')
    } finally {
      setLoading(false)
    }
  }

  const handleAdd = async (title) => {
    try {
      const newTodo = await createTodo({ title, completed: false })
      setTodos(prev => [newTodo, ...prev])
    } catch (err) {
      setError('خطا در ایجاد تسک')
    }
  }

  const handleToggle = async (id) => {
    const todo = todos.find(t => t.id === id)
    try {
      const updated = await updateTodo(id, { completed: !todo.completed })
      setTodos(prev => prev.map(t => t.id === id ? updated : t))
    } catch (err) {
      setError('خطا در بروزرسانی تسک')
    }
  }

  const handleDelete = async (id) => {
    try {
      await deleteTodo(id)
      setTodos(prev => prev.filter(t => t.id !== id))
    } catch (err) {
      setError('خطا در حذف تسک')
    }
  }

  const handleEdit = async (id, title) => {
    try {
      const updated = await updateTodo(id, { title })
      setTodos(prev => prev.map(t => t.id === id ? updated : t))
    } catch (err) {
      setError('خطا در ویرایش تسک')
    }
  }

  const filteredTodos = todos.filter(todo => {
    if (filter === 'active') return !todo.completed
    if (filter === 'completed') return todo.completed
    return true
  })

  const stats = {
    total: todos.length,
    active: todos.filter(t => !t.completed).length,
    completed: todos.filter(t => t.completed).length,
  }

  return (
    <div className="app">
      <div className="container">
        <header className="header">
          <div className="header-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M9 11l3 3L22 4" />
              <path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11" />
            </svg>
          </div>
          <h1>لیست کارها</h1>
          <p className="subtitle">کارهاتو مدیریت کن، عالی پیش برو</p>
        </header>

        {error && (
          <div className="error-toast" onClick={() => setError(null)}>
            <span>{error}</span>
            <button>&times;</button>
          </div>
        )}

        <TodoForm onAdd={handleAdd} />

        <div className="stats">
          <div className="stat-item">
            <span className="stat-number">{stats.total}</span>
            <span className="stat-label">همه</span>
          </div>
          <div className="stat-item active">
            <span className="stat-number">{stats.active}</span>
            <span className="stat-label">فعال</span>
          </div>
          <div className="stat-item completed">
            <span className="stat-number">{stats.completed}</span>
            <span className="stat-label">انجام شده</span>
          </div>
        </div>

        <FilterButtons current={filter} onChange={setFilter} />

        {loading ? (
          <div className="loading">
            <div className="spinner"></div>
            <p>در حال بارگذاری...</p>
          </div>
        ) : (
          <TodoList
            todos={filteredTodos}
            onToggle={handleToggle}
            onDelete={handleDelete}
            onEdit={handleEdit}
          />
        )}

        <footer className="footer">
          <p>sazman ToDo &copy; 2026</p>
        </footer>
      </div>
    </div>
  )
}

export default App
