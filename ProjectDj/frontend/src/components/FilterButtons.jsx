function FilterButtons({ current, onChange }) {
  const filters = [
    { key: 'all', label: 'همه' },
    { key: 'active', label: 'فعال' },
    { key: 'completed', label: 'انجام شده' },
  ]

  return (
    <div className="filter-buttons">
      {filters.map(f => (
        <button
          key={f.key}
          className={`filter-btn ${current === f.key ? 'active' : ''}`}
          onClick={() => onChange(f.key)}
        >
          {f.label}
        </button>
      ))}
    </div>
  )
}

export default FilterButtons
