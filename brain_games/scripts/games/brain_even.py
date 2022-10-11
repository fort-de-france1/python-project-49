import random

import prompt


def is_even():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    answer = ["no", "yes"]
    counter = 0
    while counter < 3:
        random_num = random.randint(1, 100)
        print(f"Question: {random_num}")
        u = input("Your answer: ").lower()

        if random_num % 2 == 0:
            even = "yes"
            if u not in answer:
                print(f"'{u}' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}")
                break
            if u == even:
                print("Correct!")
                counter += 1
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}")
                break
        else:
            odd = "no"
            if u not in answer:
                print(f"'{u}' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}")
                break
            if u == odd:
                print("Correct!")
                counter += 1
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}")
                break
    if counter == 3:
        print(f"Congratulations, {name}")


def main():
    is_even()


if __name__ == "__main__":
    main()
