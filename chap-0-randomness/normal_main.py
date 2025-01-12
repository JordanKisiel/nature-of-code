from numpy import random

def main():
    generate_splatter()

def generate_splatter(context, num_dots):
    for n in range(num_dots):
        x = random.normal()
        y = random.normal()

        context.circle()

if __name__ == "__main__":
    main()