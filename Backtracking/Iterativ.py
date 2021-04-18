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

def backIterativ(list):
    ok = False
    list.append(-1)
    while len(list) > 0:
        found = False
        while not found and list[-1] < elemente[-1]:
            list[-1] += 1
            found = consistent(list)
        if found:
            if solution(list):
                printList(list)
                ok = True
            list.append(-1)
        else:
            list.pop()
    return ok

    
def consistent(list):
    for i in range(0,len(list)-1):
        if list[i] > list[i+1]:
            return False
    for el in list:
        if not el in elemente:
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
    
ok = backIterativ([])
if not ok:
    print("The sum cannot be paid!!!")