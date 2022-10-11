import random

from brain_games.scripts.main_logic import welcome_user


def is_even(num):
    print(f"Question: {num}")
    if num % 2 == 0:
        answer = "yes"
        return answer
    else:
        answer = "no"
        return answer


def is_correct(answer, name):
    u_an = input("Your answer: ")
    if answer == u_an.lower():
        print("Correct!")
        return True
    else:
        print(f"'{u_an}' is wrong answer ;(. Correct answer was '{answer}'.")
        print(f"Let's try again, {name}!")
        return False


def main():
    name = welcome_user()
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count < 3:
        num = random.randint(1, 100)
        answer = is_even(num)
        t_or_f = is_correct(answer, name)
        if t_or_f:
            count += 1
        else:
            break

    if count == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
