from sorting import random_numbers
from student_grades import Vysledky


def main():
    results = Vysledky([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print("Počet studentů:", len(results.body))
    print()

    for i in range(len(results.body)):
        points = results.body[i]
        grade = results.get_grade(i)
        print(f"Student {i}: {points} points – {grade}")

    print()

    full_score_indexes = results.find(100)
    print("Indexy studentů s 100 body:", full_score_indexes)

    print()

    sorted_results = results.get_sorted()
    print("Seřazené výsledky:")
    print(sorted_results)

    random_results = Vysledky(random_numbers(30, 0, 100))

    print("Počet studentů:", len(random_results.body))
    print()
    for i in range(len(random_results.body)):
        points = random_results.body[i]
        print(f"Student {i}: {points} points – {random_results.get_grade(i)}")
    print()
    print("Seřazené výsledky:")
    print(random_results.get_sorted())
if __name__ == "__main__":
    main()