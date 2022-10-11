import random
from brain_games.scripts.main_logic import is_correct, rand_num, welcome_user


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
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
