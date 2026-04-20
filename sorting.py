import random
import matplotlib.pyplot as plt

def random_numbers(pocet, minimum=0, maximum=100):
    return [random.randint(minimum, maximum) for _ in range(pocet)]

def bubble_sort(seznam):
    hodnoty = seznam[:]
    n = len(hodnoty)

    plt.ion()
    plt.show()

    for i in range(n):
        for j in range(0, n - i - 1):

            if hodnoty[j] > hodnoty[j + 1]:
                hodnoty[j], hodnoty[j + 1] = hodnoty[j + 1], hodnoty[j]

            barvy = ["steelblue"] * len(hodnoty)
            barvy[j] = "tomato"
            barvy[j + 1] = "tomato"
            plt.clf()
            plt.bar(range(len(hodnoty)), hodnoty, color=barvy)
            plt.title("Bubble Sort")
            plt.pause(0.1)
    plt.ioff()
    plt.show()
    return hodnoty

def main():
    data = random_numbers(10)
    print("puvodni:", data)
    print("serazene:", bubble_sort(data))

if __name__ == "__main__":
    main()