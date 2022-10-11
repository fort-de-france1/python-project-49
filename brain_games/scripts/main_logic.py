import prompt
import random


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def rand_num():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return (num1, num2)


def is_correct(answer, name):
    u_an = input("Your answer: ")
    if answer == int(u_an):
        print("Correct!")
        return True
    else:
        print(f"'{u_an}' is wrong answer ;(. Correct answer was '{answer}'.")
        print(f"Let's try again, {name}!")
        return False
