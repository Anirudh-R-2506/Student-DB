import mysql.connector
import stdiomask
import __teacher__
def login():
    tries = 5
    m = "*"*50
    page =m +"\n" +"PLEASE LOGIN TO CONTINUE....." +"\n" +m
    print(page)
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        auth_plugin='mysql_native_password',
        database='master'
    )
    mycursor=mydb.cursor()
    mycursor.execute("select * from student")
    result=mycursor.fetchall()
    result=list(result)
    for a in range(len(result)):
        b=list(result[a])
        result.pop(a)
        result.insert(a,b)
        passwdchoice = input('PRESS 1 FOR STAFF LOGIN OR 0 FOR STUDENT LOGIN:  ')
        if passwdchoice == '0':
            uname = input('\n'*31 + "\n\nENTER USERNAME: ")
            userapprove=0
            for a in result:
                if uname == str(a[0]):
                    userapprove=1
            if userapprove==1:
                while True:
                    pword = stdiomask.getpass(prompt='ENTER PASSWORD: ')
                    passwd=0
                    for a in result:
                        if pword == a[1]:
                            passwd=1
                    if passwd==1:
                        return pword
                    else:
                        print("INCORRECT PASSWORD!!!TRY AGAIN!!!")
                        print('TRIES LEFT:',tries,"\n"*3)
                        tries-=1
                        if tries==-1:
                            input("\n" +m +"\nPROGRAM TERMINATED DUE TO EXCESSIVE INCORRECT ATTEMPTS!!!!\nPRESS ANY KEY TO EXIT......\n" + m)
                            return False
            else:
                input('*'*50 + '\nRECORD DOES NOT EXIST IN OUR DATABASE!!!PLEADE CONTACT THE ADMINISTRATION\n' + '*'*50 + '\nPRESS ANY KEY TO EXIT....\n')
                return False
        elif passwdchoice == '1':
            rez = __teacher__.__staff__()
            if rez == 1:
                return True
            elif rez == 0:
                input('*'*50 + '\nINCORRECT OTP!!!PRESS ANY KEY TO EXIT....\n' + '*'*50)
                return '1'
            elif rez == 2:
                return '1'
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
def fail(subchoice):
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        auth_plugin='mysql_native_password',
        database='master'
        )
    mycursor=mydb.cursor()
    head='ROLL\tNAME\tCT1\tCT2\tPRA\tTERM\tTOTAL\n'
    temp=''
    for a in choice(subchoice):
        mycursor.execute("select * from %s where tot<40"%(a))
        temp+='TERM'+a[-1]+':'+'\n\n'+head+mycursor.fetchall()
    nofail='THERE ARE NO FAILIURES!!!'
    if temp == '':
        return nofail
    return temp
def edit(subchoice):
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        auth_plugin='mysql_native_password',
        database='master'
        )
    mycursor=mydb.cursor()
    sub=choice(subchoice)
    head='ROLL\tNAME\tCT1\tCT2\tPRA\tTERM\tTOTAL\n'
    e1=str(input('ENTER THE NAME OF THE RECORD THAT YOU WANT TO EDIT: '))
    while True:
        term=str(input('ENTER THE TERM: '))
        if term in ('1','2','3'):
            for a in sub:
                if a[-1]==term:
                    te=a
                    mycursor.execute("select * from %s where name=%s"%(a,e1))
                    rec=mycursor.fetchall()
                    for b in rec:
                        for c in b:
                            head+=str(c).upper()+'\t'
        else:
            print('ENTER A VALID TERM.......')
            continue
    print(head)
    f=str(input('ENTER THE FIELD YOU WANT TO EDIT: '))
    dict={'ROLL':0,'NAME':1,'CT1':2,'CT2':3,'PRA':4,'TERM':5,'TOTAL':6}
    field=dict[f.upper()]
    val=str(input('ENTER THE NEW VALUE: '))
    rec[0][field]=val.upper()
    mycursor.execute("delete from %s where name=%s"%(te,e1))
    mycursor.execute('insert into %s values%s'%(te,rec[0]))
