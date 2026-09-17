print("welcome SBI atm")
data={"Name":"Sai",
    "pin":"6600",
      "Balance":50000}
Trans_His=[f"current balance:{data['Balance']}",]
attempt=0
while attempt<4:
    c_or_e=1
    pin=input("Enter Pin:")
    if(len(pin)==4):
        if pin in data["pin"]:
            while(c_or_e==1):
                print("\n1.Withdrawal\n2.Deposit\n3.check Balance \n4.Change pin\n5.Transaction history\nenter:",end=" ")
                selection=int(input())
                if(selection==1):
                    Wd_c=3
                    while(Wd_c!=0):
                        print(f"\nEnter the amount for Withdrawl:",end=" ")
                        amount=int(input())
                        if(data["Balance"]>=amount and amount%100==0):
                            Wd_c=0
                            data["Balance"]-=amount
                            print(f"Remaining balance is {data['Balance']}")
                            Trans_His.append(f"withdrawl:{amount},Remaining balance:{data['Balance']}")
                        else:
                            Wd_c-=1
                            if(Wd_c==0):
                                if(data["Balance"]<amount):
                                    print("their is no required balance to withdraw enterless then your balance")
                                if(amount%100!=0):
                                    print(f"\ndon't enter change, enter amount correctly")
                                c_or_e=2
                                print("\ntry after some time,you attempted so many times")
                            else:
                                if(data["Balance"]<amount):
                                    print("their is no required balance to withdraw enterless then your balance")
                                if(amount%100!=0):
                                    print(f"\ndon't enter change, enter amount correctly")
                                
                                
                elif(selection==2):
                    D_c=3
                    while(D_c!=0):
                        print(f"\nEnter the amount for deposit:",end=" ")
                        amount=int(input())
                        if(amount%100==0):
                            D_c=0
                            data["Balance"]+=amount
                            print(f"now your balance is {data['Balance']}")
                            Trans_His.append(f"Deposit:{amount},Now balance:{data['Balance']}")
                        else:
                            D_c-=1
                            if(D_c==0):
                                print("don't enter change, enter amount correctly")
                                c_or_e=2
                                print("\ntry after some time,you attempted so many times")
                            else:
                                print("don't enter change, enter amount correctly")
                elif(selection==3):
                    print(f"your balance is {data['Balance']}")
                elif(selection==4):
                    print("otp is sent to the mobile number linked ")

                    print("enter current pin:",end=" ")
                    pin=input()
                    if(len(pin)==4 and pin in data["pin"]):
                        Cp_c=3
                        while(Cp_c!=0):
                            print("\n enter new pin:",end=" ")
                            pin1=input()
                            if(len(pin1)==4 and pin!=pin1):
                                print("\nconfirm new pin:",end=" ")
                                pin2=input()
                                if(pin1==pin2):
                                    Cp_c=0
                                    data["pin"]=pin1
                                    print("\npin was sussesfully updated")
                                else:
                                    Cp_c-=1
                                    if(Cp_c==0):
                                        print("\ntry after some time,you attempted so many times")
                                    else:
                                        
                                        print("enter correct match pin,retry")
                            else:
                                print("pls eneter correct four digit number\n\t\t\t or\n old and new password is same change it\n")
                    else:print("you enetered wrong pin")
                    break
                
                elif(selection==5):
                    for Transaction in Trans_His:
                        print(Transaction)
                else:
                    print("invalid entry\n")
                    break
                if(c_or_e!=2):
                    print(f"\nyou want to continue or exit\nEnter:1-Continue\t0-Exit:",end=" ")
                    c_or_e=int(input())
                    if(c_or_e!=0 and c_or_e!=1):
                        c_or_e=2
                        print("invalid entry\n")
           
                  
        else:
            attempt+=1
            if(4-attempt==0):print("your card is blocked")
            else:print(f"incorrect pin,you have {4-attempt} attempts")
    else:
        print("pls enter 4 digit pin")
    if(c_or_e==0):
        print("thank you") 
        break
    

