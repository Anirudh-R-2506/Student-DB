import mysql.connector
def choice(variable):
    temp=()
    if variable == 1:
        temp=('csct1','csct2','csct3')
    elif variable == 2:
        temp=('phyt1','phyt2','phyt3')
    elif variable == 3:
        temp=('chemt1','chemt2','chemt3')
    elif variable == 4:
        temp=('engt1','engt2','engt3')
    elif variable == 5:
        temp=('matht1','matht2','matht3')
    else:
        temp=('ptt1','ptt2','ptt3')
    return temp
def display(variable1,variable2):
    mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    auth_plugin='mysql_native_password',
    database='master'
    )
    mycursor = mydb.cursor()
    finals=finalt=''
    bloc1='ROLL\tNAME\tCT\tCT\tPRA\tTERM\tTOTAL\n'
    for a in choice(variable2):
        mycursor.execute('select * from %s order by roll;'%(a))
        for b in mycursor.fetchall():
            temps=tempt=''
            if b != ():
                if variable1 == b[1]:
                    for c in b:
                        temps+=str(c) + '\t'
                    finals+='TERM'+a[-1]+':\n\n' +bloc1+ temps + '\n\n'
                for c in b:
                    tempt+=str(c) + '\t'
        finalt+='TERM'+a[-1]+':\n\n'+bloc1 + tempt + '\n\n'
    if variable1 == 1:
        return finalt
    return finals
def quit():
    print("\n"*30+"!!!!THANK YOU FOR USING OUR SEVICE!!!!" )
    input("PRESS ANY KEY TO TERMINATE PROGRAM...."+"\n"*3)
def bio(variable):
    mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    auth_plugin='mysql_native_password',
    database='master'
    )
    mycursor = mydb.cursor()
    mycursor.execute('select * from student where name="%s"'%(variable))
    res=mycursor.fetchall()
    stubio=''
    j='\n\n'
    enroll='ENROLLMENT NUMBER: ' + str(res[0][0]) + j + j
    name='NAME: ' + str(res[0][1]) + j + j
    classe='CLASS: ' + str(res[0][5]) + j + j
    sec='SECTION: ' + str(res[0][6]) + j + j
    dob='DATE OF BIRTH: ' + res[0][4] + j + j
    mobile='MOBILE: ' + str(res[0][2]) + j + j
    addresh=''
    for a in res[0][3]:
        addresh+=a
        if a == ',':
            addresh+='\n\t\t     '
    address='RESIDENTIAL ADDRESS: ' + addresh + j + j
    FINAL='\n'*33 + '\t\t\t\t\tSTUDENT BIODATA\n\n\n' + enroll + name + classe + sec + dob + mobile + address + j
    return FINAL
