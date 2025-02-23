import random


def sortuj(_list: list) -> list:
    return sorted(_list)

def policz(looking_for: int, _list: list) -> int:
    return _list.count(looking_for)


if __name__ == "__main__":
    rand_list = []
    for _ in range(20):
        rand_list.append(random.randint(0, 5))

    i = 0
    while i <= 5:
        print(f"\"{i}\" {policz(i, rand_list)}")
        i += 1
