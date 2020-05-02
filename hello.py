# -*- coding:utf-8 -*-

from random import randint


def play():
    random_init = randint(0, 100)

    while True:
        user_guess = int(input("What number did we guess (0-100)?"))

        if user_guess == random_init:
            print(f"You found the number ({random_init}). Congrats!")
            break

        if user_guess < random_init:
            print("Your number is less than the number we guessed.")
            continue

        if user_guess > random_init:
            print("Your number is more than the number we guessed.")
            continue


if __name__ == '__main__':
    play()
