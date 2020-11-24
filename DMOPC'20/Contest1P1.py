n = int(input())

words = []
for i in range(n):
    words.append(input())

for word in words:
    if 'M' in word and 'C' in word:
        print("NEGATIVE MARKS")
        continue
    if 'M' in word or 'C' in word:
        print("FAIL")
        continue
    print("PASS")
    

