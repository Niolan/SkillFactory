def show_field(f):
    num ='  0 1 2'
    print(num)
    
    for row,i in zip(f,num.split()):
        print (f"{i} {' '.join(str(j) for j in row)}")

def users_input(f,user):
    while True:
        place=input(f"����� {user}: ������� ����������:").split()
        if len(place)!=2:
            print('������� ��� ����������')
            continue
        #is digit str
        if not(place[0].isdigit() and place[1].isdigit()):
            print('������� �����')
            continue
        x, y = map(int, place)
        if not(x>=0 and x<3 and y>=0 and  y<3):
            print('����� �� ���������')
            continue
        if f[x][y]!='-':
            print('������ ������')
            continue
        break
    return x,y

def win_position(f,user):
    f_list=[]
    print(f)
    for l in f:
        f_list+=l
    print(f_list)
    positions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])

    for p in positions:
        if len(indices.intersection(set(p)))==3:
            return True
    return False

def start(field):

    count=0
    while True:
        show_field(field)
        if count%2==0:
            user='x'
        else:
            user = 'o'
        if count<9:
            x, y = users_input(field,user)
            field[x][y] = user

        elif count==9:
            print ('�����')
            break
        if win_position(field,user):
            print(f"������� {user}")
            break
        count+=1


field = [['-'] * 3 for _ in range(3)]

start(field)
