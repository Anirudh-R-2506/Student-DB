import csv
import stdiomask
def login():
    tries = 5
    m = "_"*40
    page =m +"\n" +"LOGIN PLEASE..." +"\n" +m
    while tries>0:
        print(page)
        uname = input("ENTER USERNAME: ")
        pword = stdiomask.getpass(prompt='ENTER PASSWORD:')
        if uname=='cv' and pword == 'pass' :
            return True
        else:
            print("INCORRECT USERNAME OR PASSWORD!!TRY AGAIN!!!")
            print('TRIES LEFT:',tries,"\n"*3)
            tries-=1
        if tries==-1:
            input("\n" +m +"PROGRAM TERMINATED DUE TO EXCESSIVE INCORRECT ATTEMPTS"+"\n" +m+"\n"+"PRESS ANY KEY TO EXIT....")
            return False
def prinnt(readindata):
    with open('STUDENTS.csv','r+') as file:
        reader=csv.reader(file)
        readindata=list(reader)
        c=''
        for i in readindata:
            c+='\t'.join(i)+'\n'
        return c
def write(newdata):
    with open('STUDENTS.csv','r+') as file:
        newdata=str(input('ENTER THE RECORD SEPERATED WITH COMMAS'))
        while True:
            if len(newdata)==0:
                q=input('PLEASE ENTER A VALID RECORD!!PRESS 1 TO ENTER AGAIN OR 0 FOR MENU!!')
                if q==1:
                    pass
                else:
                    break
            else:
                thefile = csv.writer(file, delimiter=',')
                newdata=newdata.split()
                thefile.writerow(newdata)
                break
def search(substring):
    with open('STUDENTS.csv','r+') as file:
        reader=csv.reader(file)
        readindata=list(reader)
        substring = substring.upper()
        d='\t'.join(readindata[0])
        c=''
        for i in readindata:
            if substring in i:
                c+='\t'.join(i)
        if c in '':
            return 'RECORD NOT FOUND!!!'
        else:
            e=d+'\n'+c
            return e
def edit(edit):
    edit=edit.upper()
    with open('STUDENTS.csv','r+') as file:
        reader=csv.reader(file)
        readindata=list(reader)
        ed=[]
        f=[]
        for i in readindata:
            for j in i:
                if edit.upper() == j:
                    ed=i
                    ed2=readindata.index(i)
        if ed!=[]:
            d='\t'.join(readindata[0])
            ed1='\t'.join(ed)
            ef=d+'\n'+ed1
            print(ef)
            ch=str(input('ENTER THE RECORD HEAD YOU WANT TO EDIT'))
            ind=readindata[0].index(ch.upper())
            newval=str(input('PLEASE ENTER THE NEW VALUE'))
            readindata[ed2][ind]=newval
            with open('STUDENTS.csv','w+') as filenew:
                thefile = csv.writer(filenew, delimiter=',')
                thefile.writerows(readindata)
        else:
            return "RECORD NOT FOUND!!"
def exit():
    print("\n"*31+"!!!!THANK YOU FOR USING OUR SEVICE!!!!" )
    input("PRESS ANY KEY TO TERMINATE PROGRAM...."+"\n"*3)
def delete(delete):
    delete=delete.upper()
    with open('STUDENTS.csv','r+') as file:
        reader=csv.reader(file)
        readindata=list(reader)
        for i in readindata:
            if delete.upper() in i:
                readindata.remove(i)
                c=1
        if c==1:
            with open('STUDENTS.csv','w+') as f:
                thefile = csv.writer(f,delimiter=',')
                thefile.writerows(readindata)
        else:
            return 'RECORD NOT FOUND!!'
'''def ascendno():
	with open('STUDENTS.csv','r+') as file:
		reader=csv.reader(file)
		readindata=list(reader)
		for i in range(len(readindata)):
			for j in range(len(readindata)-i-1):
				if readindata[j][0]>readindata[j+1][0]:
					readindata[j],readindata[j+1]=readindata[j+1],readindata[j]
		readfinal=''
        for i in readindata:
            readfinal+='\t'.join(i)+'\n'
		return readfinal'''
'''def ascendname():
	with open('STUDENTS.csv','r+') as file:
        reader=csv.reader(file)
        data=list(reader)
        for i in range(1,len(data)-1):
            for j in range(len(data)-i-3):
                if data[j][1]>data[j+1][1]:
                    data[j],data[j+1]=data[j+!],data[j]
        final=''
        for i in data:
            final+='\t'.join(i)+'\n'
        return final'''
def ranking():
    with open('STUDENTS.csv','r+') as file:
        reader=csv.reader(file)
        data=list(reader)
        data[0].append('RANK')
        for i in range(1,len(data)-1):
            for j in range(len(data)-i-3):
                if data[j][6]<data[j+1][6]:
                    data[j],data[j+1]=data[j+1],data[j]
        final='\t'.join(data[0])+'\n'
        for u in range(1,len(data)):
            data[u].append(str(u))
            final+='\t'.join(data[u])+'\n'
        return final
def failiure():
    with open('STUDENTS.csv','r+') as file:
        reader=csv.reader(file)
        data=list(reader)
        fail=[data[0]]
        for i in range(1,len(data)):
            if data[i][6]<'40':
                fail.append(data[i])
        final=''
        for i in fail:
            final+='\t'.join(i)+'\n'
        if final not in '':
            return 'NO FAILIURES!!'
        return final
