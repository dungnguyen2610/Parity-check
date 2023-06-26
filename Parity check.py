
from itertools import count
from ntpath import join


def ngovao(dang):
    Ngovao = []
    if dang == "bit":
        n = int(input("số bit của ngõ vào: "))
        for i in range (0,n):
            print("bit thứ ",i+1,': ',end='')
            x= int(input())
            Ngovao.append(x)
        for i in range (0,n):
            if Ngovao[i+1] != 1 and Ngovao[i+1] != 0:
                print("chuỗi bit của bạn không phù hợp!")
                print("Hãy nhập lại chuỗi khác!")
                return (ngovao(dang))
            else:
                return (Ngovao,n)
    else:
        n = int(input("số ký tự của ngõ vào: "))
        for i in range (0,n):
            print("ký tự thứ ",i+1,': ',end='')
            x= input()
            Ngovao.append(x)
        return (Ngovao,n)
def kiemtra(Ngovao,n,z):
    dem = 0
    for i in range (0,n):
        for j in range (0,z):
            if Ngovao[i] == nonprintcharacter[j]:
                dem += 1
    if dem == 0:
        kieukytu = 'induoc'
    else:
        kieukytu = 'khonginduoc'
    return (kieukytu)
def asynchronous(dang,n,z,vao):
    chuoi_truyen_di=[]
    if dang == 'bit':
        start_bit = [0]
        stop_bit = [1]
        parity = Parity_check(n,vao)
        chuoi_truyen_di = start_bit + vao + parity + stop_bit
    else:
        kieukytu = kiemtra(vao,n,z)
        if kieukytu == 'induoc':
            chuoi_truyen_di = ['STX'] + vao + ['ETX']
        else:
            for i in range (0,n):
                if vao[i] == 'DLE':
                    vao[i] = 'DLE DLE'
            chuoi_truyen_di =['DLE']+['STX'] + vao + ['DLE']+['ETX']
    return(chuoi_truyen_di)
def synchronous(dang,z,vao,n):
    chuoi_truyen_di=[]
    if dang == 'bit':
        open_flag = ['01111110']
        close_flag = ['01111110']
        strngovao ="".join(map(str,vao))
        strngovao = strngovao.replace('11111', '111110')
        parity = Parity_check(n,vao)
        chuoi_truyen_di = open_flag + list(strngovao) + parity + close_flag
    else:
        kieukytu = kiemtra(vao,n,z)
        if kieukytu == 'induoc':
            chuoi_truyen_di = 'SYN SYN STX'+ ''.join(vao) + ' ETX'
        else:
            chuoi_truyen_di = 'SYN SYN DLE STX'
            for char in vao:
                if char == 'DLE':
                    chuoi_truyen_di += ' DLE'
                chuoi_truyen_di += ' ' + char
            chuoi_truyen_di += ' DLE ETX'
            chuoi_truyen_di= list(chuoi_truyen_di)
    return(chuoi_truyen_di)
def Parity_check(n,vao):
    count = 0
    for i in range (n):
        if vao[i] == 1:
            count += 1
    if count % 2 == 0:
        P=[0]
    else:
        P=[1]
    return (P)
#--------------------------------------
nonprintcharacter = ['DLE','ETX','ACK','BEL','EM','CAN','ESC','DC1','DC2','DC3','DC4','DEL','NUL','SI','SO','SUB','EQN','EOT','ETB','NAK','SOH','STX','SYN','BS','CR','FF','HT','LF','VT','FS','GS','RS','US']
z = len(nonprintcharacter)
dang = input("ngõ vào dạng: ")
vao,n = ngovao(dang)
kieutruyen = input("kiểu truyền của khối dữ liệu: ")
if kieutruyen == "asynchronous":
    chuoi_truyen_di= asynchronous(dang,n,z,vao)
else:
    chuoi_truyen_di = synchronous(dang,nonprintcharacter,vao,n)
khung_truyen = " ".join(map(str,chuoi_truyen_di))
print(khung_truyen)