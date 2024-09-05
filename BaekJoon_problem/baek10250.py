Hotel=int(input())
 
rows=0
cols=1
rooms=[]
for i in range (Hotel):
    HotelNHW=list(map(int,input().split()))
    for j in range(HotelNHW[2]):
        if rows == HotelNHW[0]:
            cols+=1
            rows=1
            if cols > HotelNHW[1]:
                cols=1
        else:
            rows+=1
    room=(rows*100)+cols
    rooms.append(room)
    room=0
    rows=0
    cols=1      

for i in range(Hotel):
    print(rooms[i])