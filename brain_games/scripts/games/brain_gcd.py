from math import gcd
from brain_games.scripts.main_logic import is_correct, rand_num, welcome_user



def my_gcd(num):
    print(f"Question: {num[0]} {num[1]}")
    answer_gcd = gcd(num[0], num[1])
    return answer_gcd


def main():
    name = welcome_user()
    count = 0
    print("Find the greatest common divisor of given numbers.")
    while count < 3:
        numbers = rand_num()
        answer = my_gcd(numbers)
        t_or_f = is_correct(answer, name)
        if t_or_f:
            count += 1
        else:
            break

    if count == 3:
        print(f"Congratulations, {name}")


if __name__ == "__main__":
    main()
