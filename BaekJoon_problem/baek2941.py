cro_alpha=input()
org_len=len(cro_alpha)

a=0

while a < len(cro_alpha):
    if a+1 > len(cro_alpha)-1:
        break
    elif cro_alpha[a] =='d' and cro_alpha[a+1] =='z' and a+2 > len(cro_alpha)-1:
        break
    
    if cro_alpha[a]=='c' and cro_alpha[a+1]=='=':
        org_len-=1
        a+=2

    elif cro_alpha[a]=='c' and cro_alpha[a+1]=='-':
        org_len-=1
        a+=2

    elif cro_alpha[a]=='d' and cro_alpha[a+1]=='z' and cro_alpha[a+2]=='=':
        org_len-=2
        a+=3

    elif cro_alpha[a]=='d' and cro_alpha[a+1]=='-':
        org_len-=1
        a+=2

    elif cro_alpha[a]=='l' and cro_alpha[a+1]=='j':
        org_len-=1
        a+=2

    elif cro_alpha[a]=='n' and cro_alpha[a+1]=='j':
        org_len-=1
        a+=2

    elif cro_alpha[a]=='s' and cro_alpha[a+1]=='=':
        org_len-=1
        a+=2

    elif cro_alpha[a]=='z' and cro_alpha[a+1]=='=':
        org_len-=1
        a+=2
    else:
        a+=1
    

print(org_len)