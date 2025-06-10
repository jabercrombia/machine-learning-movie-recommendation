// app/recommend/page.tsx

'use client'

import { useState } from 'react'

export default function RecommendPage() {
  const [movie, setMovie] = useState('')
  const [recs, setRecs] = useState([])

  async function getRecommendations() {
    const res = await fetch(`http://localhost:8000/recommend?title=${encodeURIComponent(movie)}`)
    const data = await res.json()
    console.log(data);
    setRecs(data.recommendations || [])
  }


  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">Movie Recommendations</h1>
      <input
        type="text"
        value={movie}
        onChange={(e) => setMovie(e.target.value)}
        placeholder="Enter a movie title"
        className="border p-2 mt-2 w-full"
      />
      <button
        onClick={getRecommendations}
        className="bg-blue-600 text-white px-4 py-2 mt-2"
      >
        Get Recommendations
      </button>

      <ul className="mt-4">
        {recs.map((rec: any, idx: number) => (
          <li key={idx} className="mb-2">
            <strong>{rec.title}</strong> — {rec.genres}
          </li>
        ))}
      </ul>
    </div>
  )
}
