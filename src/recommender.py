from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored_songs = []

        for song in self.songs:
            score = 0.0

            if song.genre.lower() == user.favorite_genre.lower():
                score += 2.0

            if song.mood.lower() == user.favorite_mood.lower():
                score += 1.0

            energy_gap = abs(song.energy - user.target_energy)
            score += max(0, 2.0 - (energy_gap * 2.0))

            if user.likes_acoustic:
                if song.acousticness >= 0.5:
                    score += 1.0
            else:
                if song.acousticness < 0.5:
                    score += 1.0

            scored_songs.append((song, score))

        scored_songs.sort(key=lambda x: x[1], reverse=True)
        return [song for song, score in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []

        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append("genre matches your preference")

        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append("mood matches your preference")

        if abs(song.energy - user.target_energy) < 0.2:
            reasons.append("energy is close to your target")

        if user.likes_acoustic and song.acousticness >= 0.5:
            reasons.append("it matches your acoustic preference")
        elif not user.likes_acoustic and song.acousticness < 0.5:
            reasons.append("it matches your non-acoustic preference")

        if reasons:
            return "Recommended because " + ", ".join(reasons) + "."
        return "Recommended based on overall similarity."

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    if song["genre"].lower() == user_prefs["favorite_genre"].lower():
        score += 1.0
        reasons.append("genre match (+2.0)")

    if song["mood"].lower() == user_prefs["favorite_mood"].lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_gap = abs(song["energy"] - user_prefs["target_energy"])
    energy_score = max(0, 2.0 - (energy_gap * 2.0))
    score += energy_score
    reasons.append(f"energy similarity (+{energy_score:.2f})")

    tempo_gap = abs(song["tempo_bpm"] - user_prefs["target_tempo"])
    tempo_score = max(0, 1.0 - (tempo_gap / 100.0))
    score += tempo_score
    reasons.append(f"tempo similarity (+{tempo_score:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    recommendations = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        recommendations.append((song, score, explanation))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations[:k]
