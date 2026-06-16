import random

words = ["python", "computer", "program", "laptop", "github"]
word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 6

print("🎮 Welcome to Hangman Game!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("✅ Correct!")
    else:
        attempts -= 1
        print("❌ Wrong! Attempts left:", attempts)

if "_" not in guessed:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)

