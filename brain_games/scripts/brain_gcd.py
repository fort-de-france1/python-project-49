from math import gcd
from brain_calc import welcome_user, rand_num, is_correct


def _gcd(num):
    print(f"Question: {num[0]} {num[1]}")
    answer_gcd = gcd(num[0], num[1])
    return answer_gcd


def main():
    name = welcome_user()
    count = 0
    print("Find the greatest common divisor of given numbers.")
    while count < 3:
        numbers = rand_num()
        answer = _gcd(numbers)
        t_or_f = is_correct(answer, name)
        if t_or_f:
            count += 1
        else:
            break

    if count == 3:
        print(f"Congratulations, {name}")


if __name__ == "__main__":
    main()
