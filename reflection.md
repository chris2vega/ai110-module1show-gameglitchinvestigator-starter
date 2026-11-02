# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game looked pretty normal at first. There's a little sidebar on the left that allows you to change the difficulty of the game. That seems to work as intended as the difficulty change updates the main screen's attempts, though it does showcase 1 less attempt at the initial start than what is said on the left sidebar. The game's hints are also in reverse. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input       | Expected Behavior | Actual Behavior  | Console Output / Error   |
|-------------|-------------------|------------------|--------------------------|
| Enter 34 when secret number is 60 | Displays Go Higher | Displays Go Lower | no error |
| Start a new game on Normal difficulty | Display 8 attempts remaining | Displays only 7 attempts before making a guess | no error |
| Win the game, then click reset | Reset the game and allow guessing again | Game prevents any new guesses | "Game over. Start a new game to try again." |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | 

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?: Claude Code in VS Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).: On every even-numbered attempt, the app turned the secret into a string. That made 34 > "60" raise a TypeError and fall into an except block that compared strings, and that block's hints were swapped too. The fix was to always compare ints and delete the fallback. Strings compare letter by letter, so "9" > "60" comes out True. The pytest tests for 34 vs 60 and 9 vs 60 now pass.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.: Claude suggested changing the "between 1 and 100" banner to use each difficulty's range. I didn't apply it, and it's still in app.py.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?: I decided whether a bug was really fixed when the exact input I was looking for from my bug log gave an expected result. 
- Describe at least one test you ran (manual or using pytest)and what it showed you about your code.: I used pytest to check the hint logic and played the game myself to check things like the attempt counter and the New Game button. The pytest tests showed that the guessing logic now gives the right hint whether the guess is too high, too low or correct. Playing the game covered what tests couldn't easily reach, like how the screen updates after a click. Using both together gave me more confidence than either one alone.
- Did AI help you design or understand any tests? How?: I would answer yes, and that's because Claude helped me think of edge cases I wouldn't have thought of trying on my own. It also honestly helped me understand why some of the starter tests weren't working, which helped me see that tests can have bugs too.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?: In Streamlit, whenever you click a button or enter something, the program runs again from the beginning. Regular variables don't remember their previous values, which can be a problem if you want to keep track of information. Session state helps solve this by saving certain values so they don't disappear every time the program runs again. However, you still need to make sure those values are updated or reset when necessary, or the app might end up showing incorrect information.  

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?: I want to keep documenting bugs before fixing them. Writing down what I did, what I expected and what actually happened made it easier to explain problems to the AI and to tell when something was really fixed.
- What is one thing you would do differently next time you work with AI on a coding task?: I would practice making different chats for different tasks I'm trying to implement to my project, as well as making sure to slow down and read the AI-generated code fully before adding it to my project.
- In one or two sentences, describe how this project changed the way you think about AI generated code.: AI can be really efficient, but it can also set you back if you choose to not double check the accuracy of your code, especially if it is appears to be fully correct but is only 80-90% there. It's still my job to understand, test, and verify what it suggests me.
