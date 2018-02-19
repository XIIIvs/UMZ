import random


def roll(goal, exacly=0):
    if exacly > 0:
        rolled = exacly
    else:
        rolled = random.randint(1, 100)

    if rolled <= 5:
        luck = 6 - rolled
        fail = 0
    elif rolled >= 96:
        luck = 0
        fail = rolled - 95
    else:
        luck = 0
        fail = 0

    if rolled <= goal:
        tmp = goal - rolled + 1
        success = 1
        while tmp > 10:
            success += 1
            tmp -= 10
    else:
        tmp = rolled - goal
        success = -1
        while tmp > 10:
            success -= 1
            tmp -= 10
    diff = goal - rolled

    return {
        "goal": goal,
        "success": success,
        "diff": diff,
        "roll": rolled,
        "luck": luck,
        "fail": fail
    }


def test_rolls():
    print(roll(35, 100))
    print(roll(35, 99))
    print(roll(35, 98))
    print(roll(35, 97))
    print(roll(35, 96))
    print(roll(35, 95))
    print(roll(35, 94))
    print(roll(35, 86))
    print(roll(35, 85))
    print(roll(35, 84))
    print(roll(35, 76))
    print(roll(35, 75))
    print(roll(35, 74))
    print(roll(35, 66))
    print(roll(35, 65))
    print(roll(35, 64))
    print(roll(35, 56))
    print(roll(35, 55))
    print(roll(35, 54))
    print(roll(35, 46))
    print(roll(35, 45))
    print(roll(35, 44))
    print(roll(35, 36))
    print(roll(35, 35))
    print(roll(35, 34))
    print(roll(35, 26))
    print(roll(35, 25))
    print(roll(35, 24))
    print(roll(35, 16))
    print(roll(35, 15))
    print(roll(35, 14))
    print(roll(35, 6))
    print(roll(35, 5))
    print(roll(35, 4))
    print(roll(35, 3))
    print(roll(35, 2))
    print(roll(35, 1))
    print(roll(36, 1))


def opposite_test(p1, p2):
    p1_roll = roll(p1)
    p2_roll = roll(p2)

    print("P1", p1_roll)
    print("P2", p2_roll)

    p1s = p1_roll["success"]
    p2s = p2_roll["success"]

    if p1s == p2s:
        print("DRAW")
        return opposite_test(p1, p2)

    if p1s > p2s:
        return "P1", p1s - p2s
    if p2s > p1s:
        return "P2", p2s - p1s


def test_opposite_tests():
    print(opposite_test(30, 30))
    print(opposite_test(20, 40))
    print(opposite_test(10, 50))
    print(opposite_test(50, 50))
    print(opposite_test(40, 20))
    print(opposite_test(50, 10))


if __name__ == "__main__":
    test_rolls()
    # test_opposite_tests()