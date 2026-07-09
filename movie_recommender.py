import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")

cv = CountVectorizer()
count_matrix = cv.fit_transform(movies["genre"])

similarity = cosine_similarity(count_matrix)

def recommend(movie):

    movie = movie.lower()

    if movie not in movies["title"].str.lower().values:
        print("Movie not found!")
        return

    index = movies[movies["title"].str.lower() == movie].index[0]

    scores = list(enumerate(similarity[index]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:\n")

    count = 0

    for i in scores:
        if i[0] != index and i[1] > 0:
            print(movies.iloc[i[0]]["title"])
            count += 1

        if count == 5:
            break

movie_name = input("Enter Movie Name: ")

recommend(movie_name)