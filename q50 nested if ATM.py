# card is insert
language=input("enter account holder language:")
if language=="english":
    print("next")
    PIN=int(input("enter 4 digit PIN:"))
    if PIN==6644:
        print("next")
        transaction=input("enter type of transaction:")
        if transaction=="withdraw":
            print("next")
            account=input("enter type of account:")
            if account=="saving account":
                print("next")
                amount=int(input("enter withdraw amount:"))
                if amount>=3000:
                    print(amount,"\nwithdraw is succesful")
                else:
                    print("insfficient balance")
            else:
                print("invaliad account")
        else:
            print("invaliad transaction")
    else:
        print("invaliad PIN")
else:
    print("invaliad language")
