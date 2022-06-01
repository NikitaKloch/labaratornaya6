print("Введите очки команд в чемпионате:")
a = tuple(map(int, input().split()))

for i, x in enumerate(a):
    if a[i] != a[-1]:
        if a[i] <= a[i+1]:
            print("Команда распаложены не в соответсвии")
            break
    else:
        print("Команды расположены в соответствии")