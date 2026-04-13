"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def print_recommendations(profile_name, user_prefs, songs, k=5):
    print("\n" + "=" * 50)
    print(profile_name)
    print("=" * 50)

    recommendations = recommend_songs(user_prefs, songs, k=k)

    for song, score, explanation in recommendations:
        print(f"{song['title']} - {song['artist']}")
        print(f"Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    high_energy_pop = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "target_tempo": 120
    }

    chill_lofi = {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.35,
        "target_tempo": 75
    }

    intense_rock = {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.9,
        "target_tempo": 145
    }

    print_recommendations("High-Energy Pop", high_energy_pop, songs)
    print_recommendations("Chill Lofi", chill_lofi, songs)
    print_recommendations("Intense Rock", intense_rock, songs)


if __name__ == "__main__":
    main()