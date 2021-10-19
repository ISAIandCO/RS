
# coding: utf8
#-----------------------------------------------------------------------
# Программа предназначена для расчета фаз сна с целью при подъеме
# попасть в середину быстрой фазы длительностью 20 минут
#-----------------------------------------------------------------------
# Сокращения, пояснения и абревиатуры:
#   "#off " - Выключенная часть кода, заменяется на '' при включении;
#   "#1:53PM 11/03/17 " - Время и дата внесения правки выше;
#   "# Основной код " - Пояснения к части ниже;
#-----------------------------------------------------------------------

import os
# Импорт и отображение времени и даты ----------------------------------
from datetime import datetime
now_time=datetime.now()
hour=now_time.hour
minute=now_time.minute
day=now_time.day
month=now_time.month
if 0<=int(minute)<10:
    minute=str('0'+str(minute))
if 0<=int(day)<10:
    day=str('0'+str(day))
if 0<=int(month)<10:
    month=str('0'+str(month))
print('-------------------------------------------------')
print('Дата и Время: ',now_time.year,'/',month,'/',
day,'  ',now_time.hour,':',minute,sep='')
print('-------------------------------------------------')
#1:53PM 11/03/17 -------------------------------------------------------

# Основной код ---------------------------------------------------------
v=1
bk=1
u='AM'
m='PM'
while bk!=0:
    k24=0
    print('Введите время')
    #off print(' ')
    print('Часы: ',sep='',end='')
    a=input()
    
# Показать код ---------------------------------------------------------
    if (a=='дбс' or a=='l,c'or a=='L,c'or a=='L<C' 
    or a=='ДБС'or a=='Дбс'):
        x='rs.py'
        f=open(x, encoding='utf8')
        s=f.read()
        print(s)
        input()
        break
#12:15PM 11/03/17 ------------------------------------------------------

    if a=='':
        a=int(hour)
        print(hour)
    elif int(a)==24:
        a=0
        k24=1
    else:
        a=int(a)
    print('Минуты: ',sep='',end='')
    b=input()
    if b=='':
        b=int(minute)
        print(minute)
    else:
        b=int(b)
    if a>=24:
        print('Неверные данные')
    else:
        if b>=60:
            print('Неверные данные')
        else:
            if a>=12:
                r=m
            elif k24==1:
                r=u
            else:
                print('-------------------------------------------------')
                print('Утра? ',sep='',end='')
                k12=input()
                if (k12=='0' or k12=='no' or k12=='No' or k12=='NO' 
                or k12=='' or k12=='нет' or k12=='Нет' or k12=='НЕТ' 
                or k12=='ytn' or k12=='YTN' or k12=='Ytn' or k12=='тщ' 
                or k12=='Тщ' or k12=='ТЩ'):
                    if k12=='':
                        print('Нет')
                    else:
                        print(' ')
                    k1=0
                else:
                    k1=1
                if k1==1:
                    r=u
                else:
                    r=m
            if a>=12:
                a=a-12
            print('-------------------------------------------------')
            if a<10:
                print('Время: ','0',a,':',sep='',end=''),
            else:
                print('Время: ',a,':',sep='',end=''),
            if b<10:
                print('0',b,' ',r,sep='')
            else:
                print(b,' ',r,sep='')
#1:32AM 11/03/17 -------------------------------------------------------
    # 10 минут ---------------------------------------------------------
            d=(b+10)%60
            c=(a+((b+10)//60))%12
            if c<a:
                if r==m:
                    ra=u
                else:
                    ra=m
            else:
                ra=r
    # 2 часа -----------------------------------------------------------
            e=a+2;
            if e>=12:
                e=e-12
            if e<c:
                if ra==m:
                    rs=u
                else:
                    rs=m
            else:
                rs=ra
    # 3 часа 50 минут --------------------------------------------------
            g=(b+50)%60
            f=(a+3+((b+50)//60))%12
            if f<e:
                if rs==m:
                    rd=u
                else:
                    rd=m
            else:
                rd=rs
    # 5 часов 40 минут -------------------------------------------------
            y=(b+40)%60
            x=(a+5+((b+40)//60))%12
            if x<f:
                if rd==m:
                    rf=u
                else:
                    rf=m
            else:
                rf=rd
    # 7 часов 30 минут -------------------------------------------------
            n=(b+30)%60
            z=(a+7+((b+30)//60))%12
            if z<x:
                if rf==m:
                    rg=u
                else:
                    rg=m
            else:
                rg=rf
    # 9 часов 20 минут -------------------------------------------------
            l=(b+20)%60
            k=(a+9+((b+20)//60))%12
            if k<z:
                if rg==m:
                    rh=u
                else:
                    rh=m
            else:
                rh=rg
    # 11 часов 10 минут ------------------------------------------------
            w=(b+10)%60
            s=(a+11+((b+10)//60))%12
            if s<k:
                if rh==m:
                    rj=u
                else:
                    rj=m
            else:
                rj=rh
    # 13 часов ---------------------------------------------------------
            t=(b+0)%60
            q=(a+13+((b+0)//60))%12
            if q<s:
                if rj==m:
                    rk=u
                else:
                    rk=m
            else:
                rk=rj
            
            print('-------------------------------------------------')
            print('Время пробуждения \ Продолжительность сна')
    # 10 минут ---------------------------------------------------------
            print(' ')
            if c<10:
                print('0',c,':',sep='',end='')
            else:
                print(c,':',sep='',end='')
            if d<10:
                print('0',d,' ',ra,' \ 0:10',sep='')
            else:
                print(d,' ',ra,' \ 0:10',sep='')
    # 2 часа -----------------------------------------------------------
            if e<10:
                print('0',e,':',sep='',end='')
            else:
                print(e,':',sep='',end='')
            if b<10:
                print('0',b,' ',rs,' \ 2:00',sep='')
            else:
                print(b,' ',rs,' \ 2:00',sep='')
    # 3 часа 50 минут --------------------------------------------------
            if f<10:
                print('0',f,':',sep='',end='')
            else:
                print(f,':',sep='',end='')
            if g<10:
                print('0',g,' ',rd,' \ 3:50',sep='')
            else:
                print(g,' ',rd,' \ 3:50',sep='')
    # 5 часов 40 минут -------------------------------------------------
            if x<10:
                print('0',x,':',sep='',end='')
            else:
                print(x,':',sep='',end='')
            if y<10:
                print('0',y,' ',rf,' \ 5:40',sep='')
            else:
                print(y,' ',rf,' \ 5:40',sep='')
    # 7 часов 30 минут -------------------------------------------------
            if z<10:
                print('0',z,':',sep='',end='')
            else:
                print(z,':',sep='',end='')
            if n<10:
                print('0',n,' ',rg,' \ 7:30',sep='')
            else:
                print(n,' ',rg,' \ 7:30',sep='')
    # 9 часов 20 минут -------------------------------------------------
            if k<10:
                print('0',k,':',sep='',end=''),
            else:
                print(k,':',sep='',end=''),
            if l<10:
                print('0',l,' ',rh,' \ 9:20',sep='')
            else:
                print(l,' ',rh,' \ 9:20',sep='')
    # 11 часов 10 минут ------------------------------------------------
            if s<10:
                print('0',s,':',sep='',end='')
            else:
                print(s,':',sep='',end='')
            if w<10:
                print('0',w,' ',rj,' \ 11:10',sep='')
            else:
                print(w,' ',rj,' \ 11:10',sep='')
    # 13 часов ---------------------------------------------------------
            if q<10:
                print('0',q,':',sep='',end='')
            else:
                print(q,':',sep='',end='')
            if t<10:
                print('0',t,' ',rk,' \ 13:00',sep='')
            else:
                print(t,' ',rk,' \ 13:00',sep='')
            print('-------------------------------------------------')
            print('P.S: Если поставить будильник на 10 минут позже,')
            print('     то будет больше времени чтобы заснуть.')
    print('-------------------------------------------------')
    
# Будильник в планировщике из CMD --------------------------------------
    bkbud=0
    print('Установить будильник? ',sep='',end='')
    bud=input()
    if (bud=='0' or bud=='no' or bud=='No' or bud=='NO' or bud=='' 
    or bud=='нет' or bud=='Нет' or bud=='НЕТ' or bud=='ytn' 
    or bud=='YTN' or bud=='Ytn' or bud=='тщ' or bud=='Тщ' or bud=='ТЩ'):
        if bud=='':
            print('Нет')
        else:
            print(' ')
    else:
        bkbud=1
    if bkbud==1:
    # Получение местоположения -----------------------------------------
        print('-------------------------------------------------')
        folder='folder.bat'
        os.system(folder)
        folder1='folder.log'
        f=open(folder1, encoding='cp1251')
        folder3=f.read()
        folder2=folder3.rstrip()
        folder=str(folder2)
        print('')
        print('-------------------------------------------------')
        print('')
        print(folder)
        print('')
    #10:53 14/03/17 ----------------------------------------------------
        print('-------------------------------------------------')
        print('Дата и Время: ',now_time.year,'/',month,'/',
        day,'  ',now_time.hour,':',minute,sep='')
        print('-------------------------------------------------')
        print('В какое время? (24-ти часовой формат)')
        print('Часы ',sep='',end='')
        twuh=str(input())
        if 0<=int(twuh)<10:
            twuh=str('0'+str(twuh))
        print('Минуты ',sep='',end='')
        twum=str(input())
        if 0<=int(twum)<10:
            twum=str('0'+str(twum))
        twu=str(twuh+':'+twum)
        print('Какое число это будет? ',sep='',end='')
        dwu=str(input())
        months=month
        years=now_time.year
        if 0<=int(dwu)<10:
            dwu=str('0'+str(dwu))
        print('Выберите мелодию:')
        print('     1) 28 days later')
        print('     2) An End, Once And For All')
        print('     3) We falling down')
        print('     4) Heller')
        print('Ответ: ',sep='',end='')
        ptemp=input()
        if ptemp=='':
            ptemp=int(2)
        else:
            ptemp=int(ptemp)
        if ptemp==1:
            program1=str(str(folder))
            program2=str('\MF\28dayslater.mp3')
        elif ptemp==2:
            program1=str(str(folder))
            program2=str('\MF\AnEndOnceAndForAll.mp3')
        elif ptemp==3:
            program1=str(str(folder))
            program2=str('\MF\Wefallingdown.mp3')
        elif ptemp==4:
            program1=str(str(folder))
            program2=str('\MF\Heller.mp3')
        else:
            program1=str(folder)
            program2=str('\MF\AnEndOnceAndForAll.mp3')
        program=program1+program2
        bcmd=(
        'SCHTASKS /Create /SC once /F /TN Будильник /ST '+str(twu)
        +' /SD '+str(dwu)+'/'+str(month)+'/'+str(years)
        +' /TR '+program)
        os.system(bcmd)
        print('-------------------------------------------------')
#6:25PM 13/03/17 -------------------------------------------------------

    print('Желаете продолжить? ',sep='',end='')
    v=input()
    if (v=='0' or v=='no' or v=='No' or v=='NO' or v=='' or v=='нет' or 
    v=='Нет' or v=='НЕТ' or v=='ytn' or v=='YTN' or v=='Ytn' or 
    v=='тщ' or v=='Тщ' or v=='ТЩ'):
        if v=='':
            print('Нет')
        else:
            print(' ')
        bk=0
    if bk==1:
        print('-------------------------------------------------')
        print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
        print('-------------------------------------------------')
#12:20PM 15/03/17 ------------------------------------------------------
#2:02PM 14/03/17 -------------------------------------------------------
#5:32PM 12/03/17 -------------------------------------------------------
#8:47PM 11/03/17 -------------------------------------------------------
#1:21PM 11/03/17 -------------------------------------------------------
#5:11AM 11/03/17 -------------------------------------------------------

# MADE BY IVAN SYSANIN
# PORT TO PYTHON3: 11 MARTH, YEAR 2017, UFA UGNTU
