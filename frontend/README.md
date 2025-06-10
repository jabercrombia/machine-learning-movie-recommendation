# 🎬 Movie Recommendation System

A full-stack machine learning project that provides movie recommendations using **content-based filtering**. It features a FastAPI backend for serving recommendations and a Next.js frontend for interacting with the system.

---

## 🚀 Features

* Recommend similar movies based on genre similarity
* Uses **TF-IDF vectorization** and **cosine similarity**
* Built with:

  * 📦 FastAPI (Python backend)
  * 🌐 Next.js (React frontend)
  * 📊 MovieLens dataset (movies.csv)

---

## 🧠 How It Works

1. **Preprocessing**
   Movie genres are treated as pseudo-sentences by replacing `|` with spaces.

2. **Feature Extraction**
   TF-IDF vectorization converts genre text into numeric vectors.

3. **Similarity Computation**
   Cosine similarity scores the closeness of movies based on genre vectors.

4. **API Endpoint**
   `/recommend?title=Toy Story (1995)` returns a list of similar movies.

---

## 🗂️ Project Structure

```
.
├── src/
│   └── movies.csv         # MovieLens metadata (title, genres)
├── frontend/              # Next.js frontend (optional setup)
├── backend/               # Next.js frontend (optional setup)
│   └── main.py            # fastAPI app with recommendation logic
└── README.md
```

---

## 🧪 Example API Usage

**Endpoint**: `/recommend`

**Request**:

```bash
GET /recommend?title=Toy Story (1995)&num_recommendations=5
```

**Response**:

```json
{
  "recommendations": [
    {"title": "A Bug's Life (1998)", "genres": "Animation|Children|Comedy"},
    {"title": "Monsters, Inc. (2001)", "genres": "Animation|Children|Comedy"},
    ...
  ]
}
```

---

## ⚙️ Getting Started

### 🔧 Backend (FastAPI)

1. **Install dependencies**:

   ```bash
   pip install fastapi uvicorn scikit-learn pandas
   ```

2. **Run API**:

   ```bash
   uvicorn recommender:app --reload
   ```

### 💻 Frontend (Next.js) \[Optional]

1. Go to the `frontend/` directory
2. Start the development server:

   ```bash
   npm install
   npm run dev
   ```

---

## 📁 Data

Uses the `movies.csv` file from the [MovieLens](https://grouplens.org/datasets/movielens/) dataset:

* Must include `title` and `genres` columns

---

## 📌 TODOs / Enhancements

* Add fuzzy matching or autocomplete for partial titles
* Add user-based or hybrid recommendations
* Deploy to Vercel (frontend) and Render or Railway (backend)

---

## 🧑‍💻 Author

Justin Abercrombia — [jabercrombia.com](https://jabercrombia.com)
GitHub: [@jabercrombia](https://github.com/jabercrombia)

---

## 📄 License

MIT License
