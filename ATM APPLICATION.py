#ATM APPLICATION
account=100000
pwd=1234
card=input("insert the card")
if card=="c":
    print("welcome sai")
    password=int(input("enter the password"))
    if password==pwd:
        option=int(input('''choose the option
                          1.balance enq
                          2.withdraw'''))
        if option==1:
          print("acc bal is",account)
        elif option==2:
              money=int(input("enter the amount"))
              print(money)
              balance=account-money
              print("rem bal acc is",balance)
        else:
             print("invalid option")
    else:
         print("invalid password")
else:
     print("invalid card")
              
