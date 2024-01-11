import random


def play():
    user = input("Whats your choice 'r' for rock, 'p' for paper, 's' for scissor \n")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "It's a Tie"

    if u_win(user, computer):
        return "You Won !"

    return "You Lost !"


def u_win(player, opponent):
    if (
        (player == "r" and opponent == "p")
        or (player == "p" and opponent == "s")
        or (player == "s" and opponent == "r")
    ):
        return "True"


print(play())
