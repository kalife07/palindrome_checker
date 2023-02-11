def pal(n):
    pal = False
    x = 0
    if len(n)%2==0:
        for i in range(len(n)):
            if n[i]==n[-i-1] and i<len(n)/2:
                x += 1
        if x==len(n)/2:
            pal = True
    else:
        for i in range(len(n)):
            if n[i]==n[-i-1] and i<=(len(n)/2)-1:
                x += 1
        if x==len(n)//2:
            pal = True
    return pal

while True:
    n = input("Write a word: ")
    if pal(n):
        print("The word is a palindrome")
    else:
        print("The word is not a palindrome")