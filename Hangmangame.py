word = input("Enter the secret word: ").lower()

print("\n" * 50)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

hidden_word = ["_"] * len(word)

print("🎮 Welcome to Hangman!")

while wrong_guesses < max_wrong_guesses and "_" in hidden_word:
    print("\nWord:", " ".join(hidden_word))
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        print("❌ Wrong guess!")
        wrong_guesses += 1

if "_" not in hidden_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)