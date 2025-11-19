import { useState } from 'react'

export default function Pagination() {
  const [currentPage, setCurrentPage] = useState(1)
  const totalPages = 10

  return (
    <nav className="pagination">
      <button
        onClick={() => setCurrentPage(Math.max(1, currentPage - 1))}
        disabled={currentPage === 1}
      >
        Previous
      </button>
      <span>Page {currentPage} of {totalPages}</span>
      <button
        onClick={() => setCurrentPage(Math.min(totalPages, currentPage + 1))}
        disabled={currentPage === totalPages}
      >
        Next
      </button>
    </nav>
  )
}