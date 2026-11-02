# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

**Purpose:** A Streamlit number guessing game. The player picks a difficulty (Easy 1–20, Normal 1–100, Hard 1–50), then tries to guess a secret number within a limited number of attempts. Each guess gets a "Go Higher" or "Go Lower" hint, and the score depends on how quickly the player wins.

**Bugs found:**
1. **Wrong hints:** Guessing 34 when the secret was 60 said "Go Lower". On every even-numbered attempt, the app turned the secret into a string, so the comparison fell into a fallback that compared text instead of numbers (`"9" > "60"` is True) and used swapped hint messages.
2. **Missing attempt:** A new game on Normal showed 7 attempts left instead of 8, because the attempt counter started at 1 instead of 0.
3. **New Game didn't reset:** After winning, clicking New Game still blocked every guess. The button never reset the game's `status`, so the app still thought the game was over.

**Fixes applied:**
1. `check_guess` now always compares integers, with the correct hint for each case, and the string fallback was removed. The app always passes the secret as an int.
2. The attempt counter now starts at 0.
3. New Game now resets `status`, `history`, and `score`, and picks the new secret from the current difficulty's range instead of always 1–100.
4. The game logic moved from `app.py` into `logic_utils.py`, and `tests/test_game_logic.py` was updated to check both the outcome and the hint message, including regression tests for 34 vs 60 and 9 vs 60.

## 📸 Demo Walkthrough

A sample game on Normal difficulty (range 1–100, 8 attempts) where the secret number is 55:

1. User starts the game. The banner shows "Attempts left: 8", matching the sidebar.
2. User enters a guess of 40, and the game shows "📈 Go HIGHER!" (Too Low). Score goes to -5.
3. User enters a guess of 70, and the game shows "📉 Go LOWER!" (Too High). Score goes to 0.
4. User enters a guess of 55, and the game shows "🎉 Correct!" with balloons and "You won! The secret was 55. Final score: 60".
5. User tries to guess again, and the game blocks it with "You already won. Start a new game to play again."
6. User clicks "New Game 🔁". Attempts, score, and history reset, the banner shows "Attempts left: 8" again, and guessing works.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ pytest tests/ -v
============================= test session starts ==============================
collected 5 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 20%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 40%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 60%]
tests/test_game_logic.py::test_bug_log_34_vs_60 PASSED                   [ 80%]
tests/test_game_logic.py::test_single_digit_vs_two_digit PASSED          [100%]

============================== 5 passed in 0.02s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
