for _ in range(input()):
    n = input()
    arr = map(int, raw_input().split())
    count = 0 # Stores the count of the number of lazy people
    for i in arr:
        if i == -1 :
            count += 1
    count -= 1 # to exclude Gennady
    print (1+float(count)/2)
