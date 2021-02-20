"""1) A number of n coins are given, with values of 𝑎1, …, 𝑎𝑛 and a value s. Display all payment modalities
for the sum s. If no payment modality exists print a message"""


ok = [False]
while True:
    elemente = []
    try:
        SUMA = int(input("Give sum of money: "))
        n = int(input("How many type of coins do you want to use? "))
        for i in range(n):
            elemente.append(int(input("Give value of coin: ")))
        break
    except:
        pass


def backRecursiv(list):
    list.append(0)
    for el in elemente:
        list[len(list) - 1] = el
        if consistent(list):
            if solution(list):
                printList(list)
            backRecursiv(list)
    list.pop()


def consistent(list):
    for i in range(0, len(list)-1):
        if list[i] > list[i + 1]:
            return False

    if sum(list) > SUMA:
        return False
    return True


def solution(list):
    if not sum(list) == SUMA:
        return False
    return True


def printList(list):
    print(list)
    ok.append(True)


backRecursiv([])
if not ok[-1]:
    print("The sum cannot be paid!!!")

