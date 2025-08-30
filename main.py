from dictionary_functions import load_dictionary, get_current_datetime, translate_word, translate_sentence, quiz_vocabulary
import os

def main():
    dictionary = load_dictionary()

    while True:
        print(get_current_datetime())
        print('-' * 120)
        print('MINI DICTIONARY'.center(120, '*'))
        print('-' * 120)
        print("\t1. Translate a word")
        print("\t2. Translate a sentence")
        print("\t3. Vocabulary quiz")
        print("\t0. Exit program")
        choice = input("Your choice: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            translate_word(dictionary)
        elif choice == "2":
            translate_sentence(dictionary)
        elif choice == "3":
            quiz_vocabulary(dictionary)
        else:
            print("Invalid choice. Please choose 0, 1, 2, or 3.")

if __name__ == "__main__":
    main()
