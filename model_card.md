# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

VibeFinder 1.0

---

## 2. Intended Use

This recommender is designed to generate song recommendations from a small catalog based on a user’s preferred genre, mood, energy, and tempo. It assumes that users have a clear taste profile that can be represented through a few simple preferences. This system is intended for classroom exploration and learning about how recommendation systems work, not for real-world users.

---

## 3. How the Model Works

The model uses a simple weighted scoring system. It compares each song’s genre and mood to the user’s favorite genre and mood, then adds more points when the song’s energy and tempo are close to the user’s target values. Songs with the highest total scores are ranked at the top and recommended first. Compared to the starter logic, I added clearer weighting for genre, mood, energy similarity, and tempo similarity so the recommendations feel more personalized.

---

## 4. Data

The dataset contains 10 songs in the catalog. It includes genres and moods such as pop, lofi, rock, jazz, ambient, chill, happy, focused, and intense. I did not add or remove songs from the original starter dataset. One limitation is that the dataset is very small, so many styles of music and more complex listening preferences are missing.

---

## 5. Strengths

The system works well for clear user profiles, such as happy pop listeners, chill lofi listeners, or intense rock listeners. It captures the relationship between energy, tempo, and vibe fairly well, so the top recommendations often matched my intuition. For example, upbeat songs ranked highly for the pop profile, while slower and calmer songs ranked higher for the lofi profile.

---

## 6. Limitations and Bias

The system only considers a few song features and ignores lyrics, listening history, and more detailed user behavior. Because the dataset is small, some genres are underrepresented and may not be recommended as often. The scoring logic can also over-prioritize genre, which may cause the model to repeatedly recommend similar songs and reduce diversity. This could unintentionally favor users whose taste matches the most common genres in the dataset.

---

## 7. Evaluation

I tested the recommender with multiple user profiles, including High-Energy Pop, Chill Lofi, and Intense Rock. I checked whether the top songs matched the intended vibe of each profile. I also experimented with lowering the genre weight to see how much it changed the ranking. What surprised me most was how much small changes in scoring weights affected which songs appeared in the top results.

---

## 8. Future Work

If I continued this project, I would add more songs and more user preference features, such as danceability or acousticness. I would also improve the explanations so the reasons feel more natural and readable. Another improvement would be adding diversity logic so the top recommendations are not always very similar to one another.

---

## 9. Personal Reflection

This project helped me understand how recommendation systems turn data into personalized predictions. I learned that even a simple scoring formula can make the output feel smart when it matches the user’s taste. Something interesting I discovered was how easily bias can appear if one feature, like genre, is weighted too strongly. It made me think more critically about how real music apps may shape what users keep listening to.