from random import randint

def gen_random(num, min, max):
    yield from (randint(min, max) for _ in range(num))

def main():
    for i in gen_random(5, 1, 3):
        print(i)

if __name__ == "__main__":
    main()