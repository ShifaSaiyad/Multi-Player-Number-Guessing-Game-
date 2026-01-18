**Multi-Player Number Guessing Game**
A **simple**, **interactive** command-line interface (CLI) game built with **Python**. This game **challenges two players** to guess a **randomly generated number** between 1 and 100, competing for the lowest number of attempts.

<pre>
🚀 Features
Random Number Generation: Uses the random module to ensure a unique target number for each game session.

Interactive Feedback: Provides "Higher" or "Lower" hints to guide players toward the correct answer.

Multiplayer Competition: Tracks attempts for two separate players and compares scores.

Win/Tie Logic: Automatically calculates the winner based on the efficiency of their guesses.
</pre>

<pre>
🛠️ How It Works
The program generates a secret number between 1 and 100.

Player 1 guesses until they find the number; the program tracks their total attempts.

Player 2 then attempts to guess the same secret number.

The game compares the scores: the player with the fewer attempts is declared the winner.
</pre>
<pre>
💻 Tech Stack
Language: Python 3.x

Modules: random
</pre>
<pre>
📝 Future Improvements
Add a difficulty setting (e.g., Easy: 1-50, Hard: 1-500).

Implement a high-score system saved to a local file.

Allow for more than two players.
</pre>
