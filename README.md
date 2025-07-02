# 🥊 FIGHTINTEL – AI-Based Fighting Game with Machine Learning

FIGHTINTEL is a 2D fighting game where the enemy isn’t just tough — it’s smart.  
Built using Python, Pygame, and Machine Learning (KNN), this project features an AI opponent that learns the player's attack patterns in real-time and uses them against the player.

> “You fight, it learns. You combo, it counters.”


## 🚀 Features

- 🎮 Player vs AI Fighting Game**
- 🧠 AI learns your attack patterns using KNN**
- 💥 Punch, Kick, and Jump actions with collision-based combat
- 📉 Health bars and Game Over screen
- 🔁 Replay or Quit after every match
- 🧾 Real-time move logging to JSON
- ⚙️ Simple ML logic that's explainable and expandable


## 🧠 How the AI Works

- The enemy AI uses a **K-Nearest Neighbors (KNN)** model from `scikit-learn`.
- It tracks your last 3–4 moves and learns what usually follows.
- It saves your combos to `training_data.json` like this:

📁 Project Structure

FIGHTINTEL/
├── main.py             # Main game loop
├── player_module.py    # Player controls and actions
├── enemy_ai.py         # AI logic, learning, and combat
├── ai_model.py         # ML model: KNN train/predict
├── utils.py            # (Optional) Helper functions
├── training_data.json  # Player move history (for ML)
├── assets/             # (Optional) Sprites/sounds
├── README.md           # You're here!

📈 Future Improvements
	•	Replace rectangles with animated character sprites
	•	Add background music and attack sound effects
	•	Use RNN/LSTM to learn more complex patterns
	•	Convert the game into a 3D version using Unity
	•	Add a multiplayer mode or online player-vs-AI

👨‍💻 Author
Aryan Bhardwaj

🧠 “Train smarter enemies, not harder ones.” – FIGHTINTEL
