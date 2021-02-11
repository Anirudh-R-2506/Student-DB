import __fn__
import __stu__
homeinitial='*'*50 + '\n' +'''WELCOME TO THE STUDENT DATABASE!!!'''
print(homeinitial)
m='*'*50
page_2a=m+"""
SELECT THE SUBJECT TO VIEW YOUR MARKSHEET:
1.CSC
2.PHY
3.CHEM
4.ENG
5.MATH
6.PT
7.QUIT"""+'\n'+m
page_2 =m+"""
WELCOME TO THE INTERFACE:
1.DISPLAY ALL RECORDS
2.ENTER A NEW RECORD
3.SEARCH FOR A RECORD
4.EDIT A RECORD
5.DELETE A RECORD
6.FAILIURES LIST
7.QUIT"""+"\n"+m
subpage=m+"""
SELECT SUBJECT:
1.CSC
2.PHY
3.CHEM
4.ENG
5.MATH
6.PT
7.BACK TO MAIN MENU"""
log=__fn__.login()
if log is True:
    while True:
        print(page_2)
        choice=int(input('ENTER YOUR CHOICE: '))
        a=1
        if choice == 1:
            print(subpage)
            subchoice= int(input('ENTER YOUR CHOICE: '))
            if subchoice != 7:
                print(__stu__.display(a,subchoice))
        if choice == 6:
            print(subpage)
            subchoice= int(input('ENTER YOUR CHOICE: '))
            if subchoice != 7:
                print(__fn__.fail(subchoice))
if log.isalpha() :
    print(__stu__.bio(log))
    while True:
        print(page_2a)
        choic=int(input('ENTER YOUR CHOICE: '))
        if choic == 7:
            print(__stu__.quit())
            break
        else:
            print(__stu__.display(log,choic))
