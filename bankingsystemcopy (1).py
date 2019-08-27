def Create(i): 
    print("1.Personal Acc")
    print("2.loan Acount")
    ch=int(input())
    f=1
    while(f):
        fnme=input("enter  First name:")
        lnme=input("enter last name:")
        if fnme.isalpha() and lnme.isalpha():
            name.append(fnme+" "+lnme)
            f=0
        else:
            if not fnme.isalpha():
                while(f):
                    print("Invalid first name format")
                    fnme=input("enter first name correctly:")
                    if fnme.isalpha():
                        f=0
            if not lnme.isalpha():
                f1=1
                while(f1):
                    print("Invalid last name format")
                    lnme=input("enter last name correctly:")
                    if lnme.isalpha():
                        f1=0
    f=1
    while(f==1):
        dob=input("Enter date of Birth in dd/mm/yyyy format:")
        if dob[len(dob)-4:]<='2000' and dob[:2]<='31' and dob[3:5]<='12':
            Dob.append(dob)
            f=0
        else:
           if dob[:2]>'31':
               print("invalid date.")
           elif dob[3:5]>'12':
               print("invalid month.")
           elif dob[len(dob)-4:]>'2000':
               print("below 18")
               br=input("DOB is wrong....press y to re-enter:")
               if br=='y':
                   continue
               else:
                   name.pop()
                   login()
                   break
    address.append(input("Enter  address:"))
    f=1
    while(f):
        aa=int(input("enter Aadhar:"))
        while len(str(aa))!=12 or not str(aa).isnumeric():
            print("Enter valid Aadhar number")
            aa=int(input("enter Aadhar number:"))
        if aa not in Aadhar:
            Aadhar.append(aa)
            f=0
        elif ch!=2:
            print("Aadhar number already linked with another Account")
    f=1
    while(f):
        cel=input("Enter Mobile number:")
        if len(str(cel))==10 and str(cel).isnumeric():
            cell.append(int(cel))
            f=0
        else:
            print("Invalid mobile number")
    Acc.append(328601494500+i)
    if ch==2:
        Typ.append("loan")
        lt.append(Acc[-1])
        lt.append(input("Enter Loan Name:"))
        loan.append(lt)
        bal.append(-float(input("Enter Amount to be Sanctioned:")))
        print("............",lt[-1],"LOAN SANCTIONED SUCESSFULLY...........")
    else:
        while f!=1:
            ch3=int(input('''enter what type of persnal Account
            1.savings
            2.current
            '''))
            if ch3==1:
                Typ.append("savings")
                f=1
            elif ch3==2:
                Typ.append("current")
                f=1
            else:
                print("Enter Valid option")
        
        bal.append(0.00)
        print(".........",Typ[-1],"ACCOUNT SUCCESSFULLY CREATED.........")
    print()
    print("***************** Passbook as follows ***********")
    print()
    Cdisplay(ch)
def Cdisplay(chois):
    print("                 STATE BANK OF INDIA")
    print("                                    BRANCH: Vidyanikethan")
    print("NAME            :",name[-1])
    print("DOB             :",Dob[-1])
    print("ADDRESS         :",address[-1])
    print("ACCOUNT NUMBER  :",Acc[-1])
    print("AADHAR NUMBER   :",Aadhar[-1])
    print("TYPE OF ACC     :",Typ[-1])
    print("MOBILE NUMBER   :",cell[-1])
    if chois==2:
        print("TYPE OF LOAN    :",lt[-1])
        print("SanctionedAmount: ",-(bal[-1]))
    else:
       print("BALANCE         : ",bal[-1]) 
    print()
def Balance(count):
    print("1.Acc number")
    print("2.Aadhar")
    xx=int(input())
    if xx==1:
        a=int(input("Enter Acc.Number:"))
        if a in Acc:
            ind=Acc.index(a)
            print("Name:",name[ind])
            if Typ[ind]=='loan':
                print("Payable amount:",-(bal[ind]))
            else:
                print("balance:",bal[ind])
            count=0
            print()
        else:
            print("ACC not exists or wrong Acc.number")
            count+=1
            b=input("want to continue....press y")
            if count<2 and b=='y':
                Balance(count)
            else:
                print("Limit exceeded...visit bank manager you")
                print()
    else:
        a=int(input("Enter Aadhar Number:"))
        if a in Aadhar:
            ind=Aadhar.index(a)
            print("Name: ",name[ind])
            print("ACC num:",Acc[ind])
            print("balance:",bal[ind])
            count=0
            print()
        else:
            print("ACC not exists or wrong Aadhar number")
            count+=1
            b=input("want to continue....press y")
            if count<2 and b=='y':
                Balance(count)
            else:
                print("Limit exceeded...visit bank manager you")
                print()
        
def Deposit(count):
    a=int(input("Enter Acc.Number:"))
    if a in Acc:
        ind=Acc.index(a)
        dep=float(input("enter amount to deposit:"))
        while(dep<0):
            print("Invalid amount")
            dep=float(input("Re-enter the amount amount to deposit:"))
        k=list(str(dep).split("."))
        if len(k[1])>2:
            print("Invalid amount")
            Deposit(count)
        bal[ind]+=dep
        b=input("Deposited successfully........do you want to check balance enter y:")
        if(b=='y'):
            print("BALANCE:",bal[ind])
            print()
    else:
        print("ACC not exists (or) enter correct Acc.number:")
        count+=1
        if count<2:
            Balance(count)
        else:
            print("Limit exceeded.......meet bank manager you!")
            print()
def Withdrawl(count):
    a=int(input("Enter Acc.Number:"))
    for j in range(len(loan)):
        if loan[j][0]==a:
            break
    if a in Acc:
        ind=Acc.index(a)
        if Typ[ind]=="loan":
            print("since its a ",loan[j][1], "loan Account...withdrawl operation cant be performed")
        else:
            wit=float(input("Enter amount to withdrawl:"))
            k=list(str(wit).split("."))
            if len(k[1])>2 or wit<0:
                print("Invalid amount")
            else:
                if bal[ind]>=wit+500 and wit>0:
                    bal[ind]-=wit
                    b=input("Withdrawl success.........do you want to check balance enter y:")
                    if(b=='y'):
                        print("balance: ",float(format(round(bal[ind],2))))
                else:
                    print("Insufficient funds/invalid amount/you should maintain minimum balance 500")
                    print()
    else:
        print("ACC not exists (or) enter correct Accoun  number:")
        count+=1
        if count<2:
            Withdrawl(count)
        else:
            print("Limit exceeded........meet bank manager you!")
def status(count):
    a=int(input("enter Acc.Number:"))
    for j in range(len(loan)):
        if loan[j][0]==a:
            break
    if a in Acc:
        p=Acc.index(a)
        print("*****************STATE BANK OF INDIA*********************")
        print("                                    BRANCH: Vidyanikethan")
        print("NAME            :",name[p])
        print("DOB             :",Dob[p])
        print("ADDRESS         :",address[p])
        print("ACCOUNT NUMBER  :",a)
        print("AADHAR NUMBER   :",Aadhar[p])
        print("TYPE OF ACC     :",Typ[p])
        if Typ[p]=="loan":
            print("LOAN TYPE       :",loan[j][1])
            print("PAYBLE Amount   :",-bal[p])
        else:
            print("BALANCE         :",bal[p])
        print("MOBILE NUMBER   :",cell[p])
    else:
        print("ACC not exists or enter correct Acc.number:")
        count+=1
        if count<=2:
            status(count)
        else:
            print("Limit exceeded........meet bank Manager you!")
def Transfer():
    af=int(input("Enter Acc number to transfer from:"))
    at=int(input("enter Acc number to transfer to:"))
    if af in Acc and at in Acc:
        amt=int(input("Enter the Amounnt:"))
        if bal[Acc.index(af)]>=amt+500:
            bal[Acc.index(af)]-=amt
            bal[Acc.index(at)]+=amt
            print("Transfered successfully")
            print()
        else:
            print("Insuffientfunds.......")
    else:
        print("Invalid Account number(s).......Re-enter Account numbers")
        Transfer()
def delete(count):
        a=int(input("Enter Account number to delete:"))
        if a not in Acc or len(Acc)==0:
            print("Account not exists/No Accounts Available to Delete")
        else:
           xxx=Acc.index(a)
           name.pop(xxx)
           Acc.pop(xxx)
           address.pop(xxx)
           bal.pop(xxx)
           Aadhar.pop(xxx)
           if Typ[xxx]==loan:
               loan.pop(xxx)
               Typ.pop(xxx)
               ch2=input("Account deleted successfully.....:")
def Add():
    un=input("Enter username")
    psw=input("entre password")
    Access[un]=psw
    print("Accountant %s Added Successfully" %un)
    c=input("Enter y to re-login:")
    if c=='y':
        login()
def login():
    t=0
    i=0
    while(t<2):
        print("Enter your username:")
        na=input()
        print("Enter access key:")
        acckey=input()
        if acckey not in Access and na not in Access:
            print("HEY DONGA.....DONGA.....DONGA...")
            print("POYINDI POOO MOTHHAM POYINDI POO...")
            exit(1)
        elif Access[na]==acckey:
            t=3
            print("LOGGED IN AS",na,"..........")
            while(1):
                print("1.Create Account")
                print("2.Balance Enquiry")
                print("3.Deposit")
                print("4.Withdrawl")
                print("5.Status Of Account")
                print("6.Transfer")
                print("7.Delete Account")
                print("8.Add Accountant")
                print("9.Exit/Stop/logout")
                n=int(input())
                if n==1:
                    i+=1
                    Create(i)
                    lt=[]
                elif n==2:
                    Balance(0)
                elif n==3:
                    Deposit(0)
                elif n==4:
                    Withdrawl(0)
                elif n==5:
                    status(0)
                elif n==6:
                    Transfer()
                elif n==7:
                    delete(0)
                elif n==8:
                    Add()
                elif n==9:
                    exit(0)
                else:
                    print("enter valid option")
                    print()
        elif ((na not in Access)and (acckey in Access))or((acckey not in Access)and (na in Access)):
            print("One word missing.......Try to think to get yourself out.")
            t+=1
        elif (acckey in Access and na in Access)and Access[na]!=acckey:
            print("Accesskey dose not matched with your username")
            print()
            t+=1
    if t==2:
                print("limit exceeded....!")

name=[]
address=[]
Dob=[]
Acc=[]
bal=[]
Aadhar=[]
Typ=[]
lt=[]
loan=[]
cell=[]
Access={'vishnu':'vardhan','anil':'kumar','sunil':'sunny','muni':'jyo'}
login()
            
    
    
    
