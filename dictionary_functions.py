# Mini Dictionary Project
# Author: Khanh (personal practice)
# Purpose: Learn Python, practice data structures, file handling, and simple CLI UX
# dictionary_functions.py

import os
import sys
import json
import random
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")


def get_current_datetime() -> str:
    """Return current date and time as string in format YYYY-MM-DD HH:MM:SS."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def load_dictionary(file_path: str = DATA_FILE) -> dict:
    """
    Load dictionary from JSON file.
    Converts list of dicts to a dict with 'word' as key.
    Exits if file is missing.
    """
    if not os.path.exists(file_path):
        print(f"File {file_path} not found. Please provide it.")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return {item["word"]: {"type": item["type"], "meaning": item["meaning"]} for item in data}


def translate_word(dictionary: dict):
    """CLI to look up a single word."""
    while True:
        word = input("Enter word to translate (exit to quit): ").strip().lower()
        if word == "exit":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        if word in dictionary:
            print(f"{word} ({dictionary[word]['type']}) : {dictionary[word]['meaning']}")
        else:
            print("Word not found.")
            if input("Add it? (y/n): ").strip().lower() == 'y':
                meaning = input(f"Meaning of '{word}': ").strip()
                word_type = input(f"Type of '{word}': ").strip()
                dictionary[word] = {"type": word_type, "meaning": meaning}
                with open(DATA_FILE, "w", encoding="utf-8") as f:
                    json.dump([{"word": k, **v} for k, v in dictionary.items()], f, ensure_ascii=False, indent=2)
                print("Dictionary updated!")


def translate_sentence(dictionary: dict):
    """CLI to translate a sentence word by word."""
    while True:
        sentence = input("Enter sentence (exit to quit): ").strip().lower()
        if sentence == "exit":
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        words = sentence.split()
        unknown = [w for w in words if w not in dictionary]
        if unknown:
            print(f"Words not found: {', '.join(unknown)}")
            if input("Add them? (y/n): ").strip().lower() == 'y':
                for w in unknown:
                    meaning = input(f"Meaning of '{w}': ").strip()
                    word_type = input(f"Type of '{w}': ").strip()
                    dictionary[w] = {"type": word_type, "meaning": meaning}
                with open(DATA_FILE, "w", encoding="utf-8") as f:
                    json.dump([{"word": k, **v} for k, v in dictionary.items()],
                              f, ensure_ascii=False, indent=2)
                print("Dictionary updated!")

        full_translation = [dictionary[w]['meaning'] for w in words if w in dictionary]
        print(f"Full translation: {' '.join(full_translation)}")


def quiz_vocabulary(dictionary: dict):
    """CLI vocabulary quiz with no repeats in a session."""
    used = set()
    all_words = list(dictionary.keys())

    while True:
        if len(used) == len(all_words):
            print("Congrats! All words completed.")
            break

        word = random.choice([w for w in all_words if w not in used])
        used.add(word)

        answer = input(f"What is the meaning of '{word}'? (exit to quit): ").strip().lower()
        if answer == "exit":
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        correct = dictionary[word]['meaning'].lower()
        print("Correct!" if answer == correct else f"Wrong. Correct meaning: {correct}")

