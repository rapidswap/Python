word = input()
cnt_list=[]
alphabet_dict = {chr(i):0 for i in range(ord('A'),ord('Z')+1)}

for i in range(len(word)):
    alphabet_dict[word[i].upper()] += 1

max_count = 0
max_alphabet = ''

for alpha in alphabet_dict:
    if max_count < alphabet_dict[alpha]:
        max_alphabet=alpha
        max_count=alphabet_dict[alpha]
    elif max_count == alphabet_dict[alpha]:
        max_alphabet='?'

print(max_alphabet)