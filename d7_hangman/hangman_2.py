#!/usr/bin/env python3
"""Small-footprint Hangman in plain Python (no external graphics)."""

import random
import sys
from pathlib import Path
from typing import Set

# ---------- data -------------------------------------------------------------

# Load once, keep only easy lower-case words 5-12 chars, alphabetic only
def _load_words() -> list[str]:
    try:
        from nltk.corpus import words as nltk_words
    except LookupError:          # first run ⇒ auto-download corpus
        import nltk
        nltk.download("words")
        from nltk.corpus import words as nltk_words
    return [
        w.lower()
        for w in nltk_words.words()
        if w.isalpha() and 5 <= len(w) <= 12
    ]


WORD_POOL: list[str] = _load_words()


# ---------- game logic -------------------------------------------------------

MAX_LIVES = 6
HANGMAN_PICS = [
    "",  # 0 wrong
    " O ",
    " O \n | ",
    " O \n/| ",
    " O \n/|\\",
    " O \n/|\\\n/  ",
    " O \n/|\\\n/ \\",
]


def pick_word() -> str:
    return random.choice(WORD_POOL)


def render(word: str, guessed: Set[str]) -> str:
    return " ".join(c if c in guessed else "_" for c in word)


def prompt_letter(guessed: Set[str]) -> str:
    while True:
        guess = input("Guess a letter (or word): ").lower().strip()
        if not guess:
            continue
        if len(guess) > 1:           # whole-word attempt
            return guess
        if guess.isalpha() and guess not in guessed:
            return guess
        print("⚠️  Invalid / repeated, try again.")


def play_once() -> None:
    word = pick_word()
    guessed: Set[str] = set()
    lives = MAX_LIVES

    print("\n🎮  New game!  Type the full word if you feel lucky.\n")
    while lives and set(word) - guessed:
        print(HANGMAN_PICS[MAX_LIVES - lives])
        print("Word:", render(word, guessed))
        print(f"Misses left: {lives}\n")

        g = prompt_letter(guessed)
        if len(g) > 1:                      # word guess
            if g == word:
                guessed.update(word)
            else:
                lives -= 1
        else:                               # single letter
            if g in word:
                guessed.add(g)
            else:
                lives -= 1

    # -------- outcome --------------------------------------------------------
    if set(word) - guessed:
        print(HANGMAN_PICS[-1])
        print(f"💀  You lost. The word was '{word}'.")
    else:
        print(f"✅  Correct! You guessed '{word}'. Great job!")

# ---------- entry-point -------------------------------------------------------

def main() -> None:
    while True:
        play_once()
        if input("\nPlay again? [y/N] ").lower() != "y":
            print("Bye!")
            break


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        sys.exit("\n\n👋  Exiting Hangman.")
