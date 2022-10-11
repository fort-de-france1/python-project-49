import random
from brain_games.scripts.main_logic import is_correct, welcome_user


def progression():
    f_num = random.randint(1, 100)
    prog_list = [i for i in range(f_num, f_num + 30, 3)]
    ran_idx = random.randint(0, 9)
    answer = prog_list[ran_idx]
    prog_list[ran_idx] = ".."
    print("Question:", end=" ")
    for i in prog_list:
        print(i, end=" ")
    print()
    return answer


def main():
    name = welcome_user()
    count = 0
    print("What number is missing in the progression?")
    while count < 3:
        answer = progression()
        t_or_f = is_correct(answer, name)
        if t_or_f:
            count += 1
        else:
            break

    if count == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
