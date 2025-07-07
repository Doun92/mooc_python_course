# Write your solution here
import random

def play(die1: str, die2: str, times: int):
    i = 0
    p1_wins = 0
    p2_wins = 0
    ties = 0

    while i < times:
        re1 = roll(die1)
        re2 = roll(die2)

        if re1 > re2:
            p1_wins += 1
        elif re1 < re2:
            p2_wins += 1
        else:
            ties +=1

        i+= 1

    return (p1_wins, p2_wins, ties)

def roll(die: str):
    if die == "A":
        sides = [3, 3, 3, 3, 3, 6]

    if die == "B":
        sides = [2, 2, 2, 5, 5, 5]

    if die == "C":
        sides = [1, 4, 4, 4, 4, 4]

    return random.choice(sides)

if __name__ == "__main__":   
    # for i in range(20):
    #     print(roll("A"), " ", end="")
    # print()
    # for i in range(20):
    #     print(roll("B"), " ", end="")
    # print()
    # for i in range(20):
    #     print(roll("C"), " ", end="")

    result = play("A", "C", 1000)
    print(result)