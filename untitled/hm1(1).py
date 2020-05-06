s = input()
l: int = len(s)
for i in range(l // 2):
    if s[i] != s[-1 - i]:
    print("Это не палиндром")
quit()

print("Это палиндром")