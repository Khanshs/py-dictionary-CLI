# Mini Dictionary CLI

A simple Python-based mini dictionary project for self-learning and practice.  
Users can translate words, translate sentences, take vocabulary quizzes, and automatically save unknown words for later review.  
All dictionary entries are stored in a JSON file.  

---

## Features
- Translate words and sentences at basic level
- Vocabulary quiz mode  
- Dictionary entries stored in `data.json`  
- **Auto-save unknown words** for later review  
- Currently supports **English → Vietnamese** word and sentence translation  

---

## Installation & Usage

Clone the repository and run the program:

```bash

git clone https://github.com/Khanshs/py-dictionary-CLI.git
cd py-dictionary-CLI
python main.py

```
## Demo
```bash
$ python main.py
2025-08-31 15:42:10
------------------------------------------------------------
********************* MINI DICTIONARY **********************
------------------------------------------------------------
    1. Translate a word
    2. Translate a sentence
    3. Vocabulary quiz
    0. Exit program
Your choice:1
Enter word: hello
Result: xin chào

```
## Notes

- All dictionary data is stored in `data.json`  
- This project is experimental, built mainly for learning and portfolio showcase.
- Unknown words are logged for later review and can be added to the dictionary.


## Future Improvements

- Add support for more languages
- Enhance AI-powered translation
- Expand vocabulary quizzes with difficulty level

