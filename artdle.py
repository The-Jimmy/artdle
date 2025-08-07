import copy
import os
import sys
from colorama import init, Fore, Back, Style

init()

# Get the folder where the current Python file is located
base_dir = os.path.dirname(__file__)

# Build the full path to the file
file_path = os.path.join(base_dir, 'valid-wordle-words.txt')

# Open and read the file
with open(file_path, 'r', encoding='utf-8') as f:
    words = [line.strip() for line in f]  # strip() removes \n and spaces


def get_answer():
    while True:
        try:
            answer = input("Today Wordle('x' to close the program): ").lower()
            
            if answer == "x":
                sys.exit()

            elif len(answer) != 5 or answer not in words:
                raise ValueError
            
        except ValueError:
            print("Invalid word, Please try again.")
            continue
        return answer

def get_art():
    arts = []
    n = 0
    print("\nPlease input the art you want to recreate line by line (c = colored | b = blank)")
    print("Type 'x' to end early")
    while n < 6:
        try:
            a = input(f"Art line {n + 1}: ").lower()

            # Allow early exit
            if a == 'x':
                break

            # Check length and allowed characters
            if len(a) != 5 or not all(ch in ('c', 'b') for ch in a):
                raise ValueError

            # If valid, add to arts
            arts.append(a)
            n += 1

        except ValueError:
            print("Invalid art. Please enter exactly 5 characters containing only 'c' or 'b'.")
            continue

    return arts

def check_art(check_word, check_answer, check_art):
    for i in range(len(check_art)):
        if (check_art[i] == "c" and check_word[i] != check_answer[i]) or (check_art[i] == "b" and check_word[i] in check_answer):
            return False
    
    return True
# check_art("sword", "sword", "ccccb") False
# check_art("sward", "sword", "cbccb") False
# check_art("sdorn", "sword", "cbccb") True

def find_art(words:list, answer:str, arts:list):
    result = []
    for art in arts:
        copy_words = copy.deepcopy(words)

        copy_words = filter(lambda w: check_art(w, answer, art), copy_words)
        copy_words = list(copy_words)
        if len(copy_words) == 0:
            result.append("-")
        else:
            result.append(copy_words[0])
    return result

def show_result(result: list, arts: list):
    print("====ANSWER====")
    for i, res in enumerate(result):
        print(f"Word {i+1}:", end=' ')
        
        if res == "-":
            print(f"Not possible, art: {arts[i]}")
            continue
        
        art = arts[i]  # Corresponding art for this result
        for r_char, a_char in zip(res, art):
            if a_char == 'c':
                print(Back.GREEN + Fore.BLACK + r_char + Style.RESET_ALL, end='')
            elif a_char == 'b':
                print(Back.BLACK + Fore.BLACK + r_char + Style.RESET_ALL, end='')
            else:
                # Optional: handle unexpected characters
                print(r_char, end='')
        print()  # New line after each word


def main():
    answer = get_answer()
    arts = get_art()

    print()
    result = find_art(words, answer, arts)
    show_result(result, arts)

if __name__ == "__main__":
      main()
