N = int(input())

word = [input() for i in range(N)]
word_sort={}
for i in range(N):
    word_sort[word[i]]=len(word[i])
word_sort.items()
clear=sorted(word_sort.items(), key=lambda x: (x[1],x[0]))

for i,j in clear:
    print(i)
