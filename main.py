def register():
    db=open("database.txt","r")
    Username=input("Create username:")
    Password=input("Create password:")
    Password=input("Confirm password")
    d=[]
    f=[]
    for i in db:
        a,b=i.split()
        b=b.strip()
        d.append(a)
        f.append(b)
    data= dict(zip(d,f))
    if Password != Password:
        print("password dont match, restart")
        register()
    else:
        if len(Password)<=6:
            print("Password too short, restart")
            register()
        elif Username in d:
            print("Username exists")
            register()
        else:
            db=open("database.txt","a")
            db.write(Username+","+Password+"\n")
            print("Success!")

def access():
     db= open("database.txt", "r")
     Username= input("Enter your username:")
     Password= input("Enter your password:")

     if not len(Username or Password)<1:
         d=[]
         f=[]
         for i in db:
             a,b= i.split(",")
             b=b.strip()
             d.append(a)
             f.append(b)
         data = dict(zip(d,f))

         try:
             if data[Username]:
                 try:
                     if Password== data[Username]:
                         print("Login success")
                         print("Hi", Username)
                     else:
                         print("Password or Username incorrect")
                 except:
                     print("Incorrect password or username")
             else:
                 print("Username or password doesn't exist")
         except:
             print("Username or password doesn't exist")
     else:
         print("Please enter a value")

def home(option= None):
     option=input("Login | Signup :")
     if option=="Login":
         access()
     elif option =="Signup":
         register()
     else:
         print("Please enter an option")
home()











