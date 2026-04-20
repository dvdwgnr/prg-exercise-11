class Vysledky:
    def __init__(self, body):
        self.body = body

    def get_grade(self, index):
        pocet_bodu = self.body[index]
        if pocet_bodu >= 90:
            return "A"
        elif pocet_bodu >= 80:
            return "B"
        elif pocet_bodu >= 70:
            return "C"
        elif pocet_bodu >= 60:
            return "D"
        elif pocet_bodu >= 50:
            return "E"
        else:
            return "F"

    def find(self, hledane_body):
        vysledky = []
        for i in range(len(self.body)):
            if self.body[i] == hledane_body:
                vysledky.append(i)
        return vysledky

    def get_sorted(self):
        scores = self.body[:]
        n = len(scores)

        for i in range(n):
            for j in range(0, n - i - 1):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]

        return scores
