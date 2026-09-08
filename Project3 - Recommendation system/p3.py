# Project 3: AI Recommendation Logic

movies = [
    {
        "title": "Interstellar",
        "genres": ["sci-fi", "adventure", "drama"]
    },
    {
        "title": "The Matrix",
        "genres": ["sci-fi", "action"]
    },
    {
        "title": "Inception",
        "genres": ["sci-fi", "action", "thriller"]
    },
    {
        "title": "The Dark Knight",
        "genres": ["action", "crime", "drama"]
    },
    {
        "title": "Avengers: Endgame",
        "genres": ["action", "adventure", "sci-fi"]
    },
    {
        "title": "The Hangover",
        "genres": ["comedy"]
    },
    {
        "title": "Titanic",
        "genres": ["romance", "drama"]
    },
    {
        "title": "The Conjuring",
        "genres": ["horror", "thriller"]
    }
]

all_genres = sorted(
    set(genre for movie in movies for genre in movie["genres"])
)

print("Available genres:")
print(", ".join(all_genres))


user_input = input("\nEnter your favorite genres (separated by commas): ")

user_preferences = [
    genre.strip().lower()
    for genre in user_input.split(",")
]


def calculate_similarity(user_preferences, movie_genres):
    matching_genres = set(user_preferences) & set(movie_genres)

    if len(user_preferences) == 0:
        return 0

    score = len(matching_genres) / len(user_preferences)

    return score


recommendations = []

for movie in movies:
    score = calculate_similarity(
        user_preferences,
        movie["genres"]
    )

    if score > 0:
        recommendations.append(
            (movie["title"], score)
        )



recommendations.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\nRecommended Movies:")

if recommendations:
    for title, score in recommendations:
        print(f"{title} - Similarity: {score * 100:.0f}%")
else:
    print("Sorry, no matching movies were found.")