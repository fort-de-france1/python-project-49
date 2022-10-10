import random
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    return name


def sum(num):
    print(f"Question: {num[0]} + {num[1]}")
    answer_sum = num[0] + num[1]
    return answer_sum


def minus(num):
    print(f"Question: {num[0]} - {num[1]}")
    answer_min = num[0] - num[1]
    return answer_min


def multi(num):
    print(f"Question: {num[0]} * {num[1]}")
    answer_multi = num[0] * num[1]
    return answer_multi


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


def main():
    name = welcome_user()
    count = 0
    while count < 3:
        numbers = rand_num()
        ran_opr = random.choice((sum, minus, multi))
        answer = ran_opr(numbers)
        t_or_f = is_correct(answer, name)
        if t_or_f:
            count += 1
        else:
            break
    if count == 3:
        print(f"Congratulations, {name}")


if __name__ == "__main__":
    main()
