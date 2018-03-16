from collections import Counter
myliste = open('res.txt').read().split()
res = Counter(myliste)
print(res)
