import { useState } from 'react'

function TodoForm({ onAdd }) {
  const [title, setTitle] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    const trimmed = title.trim()
    if (!trimmed) return
    onAdd(trimmed)
    setTitle('')
  }

  return (
    <form className="todo-form" onSubmit={handleSubmit}>
      <div className="input-wrapper">
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="یه کار جدید اضافه کن..."
          className="todo-input"
          autoFocus
        />
        <button type="submit" className="add-btn" disabled={!title.trim()}>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
            <line x1="12" y1="5" x2="12" y2="19" />
            <line x1="5" y1="12" x2="19" y2="12" />
          </svg>
        </button>
      </div>
    </form>
  )
}

export default TodoForm
