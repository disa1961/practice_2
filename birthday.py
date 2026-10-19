import random
def birthday_probability(people):
    if people > 365:
        return 1.0
    p = 1.0
    for i in range(people):
        p *= (365 - i) / 365
    return 1 - p

def simulate_birthday(people, trials):
    hits = 0
    for _ in range(trials):
        days = [random.randint(1, 365) for _ in range(people)]
        if len(set(days)) < people:
            hits += 1
    return hits / trials

if __name__ == "__main__":
    print("people  exact     simulated")
    for people in range(5, 61, 5):
        exact = birthday_probability(people)
        sim = simulate_birthday(people, 10000)
        print(f"{people:6}  {exact:.6f}  {sim:.6f}")

    for people in range(1, 366):
        if birthday_probability(people) > 0.5:
            print("Наименьшее число людей:", people)
            break
