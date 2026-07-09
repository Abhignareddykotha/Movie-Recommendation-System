# 🎬 Movie Recommendation System

A simple **content-based Movie Recommendation System** developed using **Python**, **Pandas**, and **Scikit-learn**. The system recommends movies based on genre similarity using the **Cosine Similarity** algorithm.

---

## 🚀 Features

- Recommends similar movies based on genre
- Uses Machine Learning concepts
- Simple command-line interface
- Fast and easy to use

---

## 🛠 Technologies Used

- Python
- Pandas
- Scikit-learn

---

## 📁 Project Structure

```
Movie-Recommendation-System/
│── movie_recommender.py
│── movies.csv
│── requirements.txt
│── README.md
└── output.png
```

---

## 📂 Dataset

The dataset contains movie titles along with their genres.

| Title | Genre |
|--------|--------|
| Avengers | Action |
| Iron Man | Action |
| Titanic | Romance |
| Interstellar | Sci-Fi |

---

## ▶️ How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the program:

```bash
python movie_recommender.py
```

---

## 📸 Sample Output

![Sample Output](output.png)

---

## 🧠 How It Works

1. Reads movie data using Pandas.
2. Converts movie genres into vectors using CountVectorizer.
3. Calculates similarity using Cosine Similarity.
4. Recommends the most similar movies.

---

## 📦 Requirements

- pandas
- scikit-learn

---

## 👩‍💻 Author

**Abhigna Reddy**

AI Internship Project – Codec Technologies
