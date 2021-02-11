def __staff__():
    import smtplib, ssl
    import string
    import secrets
    import mysql.connector
    import stdiomask
    import time
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "cvstudentdatabase@gmail.com"
    password = 'anirudhnfs01'
    print('\n'*33)

    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        auth_plugin='mysql_native_password',
        database='master'
    )
    mycursor=mydb.cursor()
    mycursor.execute("select * from login")
    result=mycursor.fetchall()
    result=list(result)
    for a in range(len(result)):
        b=list(result[a])
        result.pop(a)
        result.insert(a,b)
    alphabet = string.ascii_letters + string.digits
    while True:
        otps = ''.join(secrets.choice(alphabet) for i in range(7))
        if (any(c.islower() for c in otps)
                and any(c.isupper() for c in otps)
                and sum(c.isdigit() for c in otps) >= 3):
            break
    message = """
    Your OTP for database login: """ + str(otps)
    print('*'*50 + '''\nSELECT YOUR CHOICE:
1)LOGIN WITH SMS
2)LOGIN WITH EMAIL\n''' + '*'*50)
    ch=int(input())
    if ch == 2:
        receiver_email = str(input('ENTER YOUR E-MAIL ADDRESS: '))
        fail=0
        for a in result:
            if receiver_email in a:
                fail+=1
        if fail == 1:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            import time
            for i in range(10,-1,-1):
                time.sleep(1)
                print('ENTER THE OTP' + '(' + str(i)+'seconds left): ',end='\r'+'\b'*37)

            otp=stdiomask.getpass(prompt=for i in range(10,-1,-1):
                                        time.sleep(1)
                print('ENTER THE OTP' + '(' + str(i)+'seconds left): ',end='\r'+'\b'*37))
            if otp == otps:
                return 1
            elif otp!=otps:
                input('*'*50 + '\nUNAUTHORISED ACCES....\n' +'*'*50 + '\nPRESS ANY KEY TO EXIT.....')
                return 2
        else:
            input('*'*50 + '\nYOUR EMAIL ID IS NOT IN OUR DATABASE!!!!PLEASE CONTACT THE ADMINISTRATION.....\n' + '*'*50 + '\nPRESS ANY KEY TO EXIT.....')
            return 2
    elif ch == 1:
        no=str(input('ENTER YOUR MOILE NUMBER: '))
        from twilio.rest import Client

        account_sid = 'ACd1e7b2d74f3e8b534e8ea60c3ad906c2'
        auth_token = '4c24ead6ef720b7209a57bab789b90ba'

        client = Client(account_sid, auth_token)
        fail=0
        for a in result:
            if no in a:
                fail+=1
        if fail == 1:
            message = client.messages.create(
                                          from_='+12565983085',
                                          body =otps,
                                          to ='+91'+no
                                            )
            otp=stdiomask.getpass(prompt=prompt())
            if otp == otps:
                return 1
            elif otp!=otps:
                input('*'*50 + '\nUNAUTHORISED ACCES....\n' +'*'*50 + '\nPRESS ANY KEY TO EXIT.....')
                return 2
        else:
            input('*'*50 + '\nYOUR MOBILE NUMBER IS NOT IN OUR DATABASE!!!!PLEASE CONTACT THE ADMINISTRATION.....\n' + '*'*50 + '\nPRESS ANY KEY TO EXIT.....')
            return 2
