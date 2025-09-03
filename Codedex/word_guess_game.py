import random

words_bank = ["apple", "banana", "mango", "peach", "orange"]
word = random.choice(words_bank)
# guessedWord = "_" * len(word) # 字符串不可变：guessedWord[i] = guess 会报错
guessedWord = ["_"] * len(word) # 改为列表，因为列表是可变的
attempts = 10

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))
    guess = input("Guess a letter: ").lower().strip()

    # 检查输入是否有效
    if len(guess) == 0:
        print("Please enter a letter!")
        continue
    elif len(guess) > 1:
        print("Please enter only one letter!")
        continue
    elif not guess.isalpha():
        print("Please enter a valid letter!")
        continue

    if guess in word:
        for i in range (len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print("Great guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

    if '_' not in guessedWord:
        print('\nCongratulations!! You guessed the word: ' + word)
        break

if attempts == 0 and '_' in guessedWord:
    print('\nYou\'ve run out of attempts! The word was: ' + word)

#这是一个新改动吗？