n = int(input("Enter the number of bulbs: "))
def Bulbs(n):
    bulbs = [0] * n
    for i in range(1, n + 1):
        for j in range(i - 1, n, i):
            bulbs[j] = 1 - bulbs[j]
    bulbs = [index + 1 for index, state in enumerate(bulbs) if state == 1]
    return bulbs
bulbs = Bulbs(n)
print("Bulbs that remain ON:", bulbs)