# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

This project uses a **content-based recommendation system**, which means it recommends songs based on the features of the songs themselves instead of comparing users to other users.

### Song Features
Each song in the system uses:
- title
- artist
- genre
- mood
- energy
- tempo

### User Profile
The `UserProfile` stores:
- favorite genre
- favorite mood
- target energy
- target tempo

### Scoring Logic
The `Recommender` gives each song a weighted score:
- +2 points for a matching genre
- +1 point for a matching mood
- up to +2 points if the song’s energy is close to the user’s target
- up to +1 point if the song’s tempo is close to the user’s target

### Ranking Rule
After every song is scored, the system sorts the songs from highest score to lowest score and recommends the top 3–5 songs.

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

I tested the recommender with multiple profiles, including High-Energy Pop, Chill Lofi, and Intense Rock. I also ran a small experiment by lowering the genre weight from 2.0 to 1.0. This made the system more flexible because songs from different genres could rank higher if they matched energy and tempo well, but it also made some recommendations feel less intuitive.


## Limitations and Risks

This recommender only works on a very small catalog of songs, so its suggestions are limited. It may also over-favor certain genres or moods if they appear more often in the dataset. Because it uses only a few song features, it does not understand lyrics, personal history, or more complex listening behavior.

## Reflection

This project helped me understand how recommendation systems turn data into predictions by converting user preferences and song features into scores. By comparing things like genre, mood, energy, and tempo, the recommender was able to rank songs in a way that often felt personalized. I learned that even a simple scoring formula can still produce useful recommendations when the chosen features match what the user cares about.

I also learned how bias and unfairness can show up very easily in systems like this. Because my recommender gives strong weight to genre, it may over-recommend songs from one genre while ignoring songs that still match the user’s mood or energy. The small dataset can also create bias because some genres and moods are represented more than others. In a real-world app, this could limit diversity and repeatedly push users toward the same kind of music instead of helping them discover something new.


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

This system is designed to recommend 3 to 5 songs from a small music catalog based on a user’s preferred genre, mood, energy, and tempo. It is meant for classroom exploration and learning how recommendation systems work, not for real-world users.
---

## 3. How It Works (Short Explanation)

The recommender looks at each song’s genre, mood, energy, and tempo. It compares those features to the user’s favorite genre, favorite mood, target energy, and target tempo.

Songs receive points when their genre and mood match the user’s preferences. They also receive additional similarity points when their energy and tempo are close to the user’s target values.

After every song is scored, the system ranks the songs from highest score to lowest score and returns the top recommendations.

## 4. Data

The dataset contains 10 songs in `data/songs.csv`. I did not add or remove any songs from the starter dataset.

The catalog includes a variety of genres and moods such as pop, lofi, rock, jazz, ambient, synthwave, chill, happy, intense, focused, and relaxed.

Because the dataset is small, it mostly reflects a limited range of music tastes and simplified listening styles rather than the diversity of real-world music preferences.

## 5. Strengths

The recommender works well when the user profile is clear and specific. It gave strong results for profiles like High-Energy Pop, Chill Lofi, and Intense Rock because the top songs usually matched the expected vibe.

One strength of the system is that the scoring logic is simple and transparent. It is easy to understand why a song was recommended because the explanation clearly shows whether genre, mood, energy, and tempo contributed to the score.

## 6. Limitations and Bias

The recommender struggles because it only considers a few simple features, mainly genre, mood, energy, and tempo. It does not account for lyrics, listening history, or more detailed music preferences.

Because genre is weighted strongly, the model may over-recommend songs from one genre and ignore songs that still match the user’s mood or energy. The small dataset also means some genres and moods are represented more than others, which can bias the system toward the most common styles.

If used in a real product, this could be unfair because users might repeatedly see the same type of music and have fewer chances to discover different genres or new artists.

## 7. Evaluation

I evaluated the recommender by testing it with multiple user profiles, including High-Energy Pop, Chill Lofi, and Intense Rock. I checked whether the top recommendations matched the expected vibe for each profile.

I also ran the provided tests to make sure the scoring logic and recommendation functions worked correctly. In addition, I experimented with lowering the genre weight to see how much it changed the ranking order. This helped me understand how sensitive the recommender is to small scoring changes.

## 8. Future Work

If I had more time, I would improve the recommender by adding more songs and a wider range of genres and moods. A larger dataset would make the recommendations feel more realistic and fair.

I would also add more features, such as danceability, acousticness, and lyric themes, so the recommendations capture more of the song’s vibe. Another improvement would be adding diversity logic so the top results are not always very similar and users can discover different artists and genres.

## 9. Personal Reflection

One thing that surprised me was how a simple scoring formula could still make the recommendations feel personalized. Even though the logic was straightforward, changing just one weight, like genre, noticeably changed the ranking results.

Building this project changed how I think about real music recommenders because it showed me that personalization often starts with simple feature comparisons and ranking. At the same time, it reminded me that human judgment still matters when deciding what features to prioritize, how much variety users should see, and how to reduce bias in the results.

