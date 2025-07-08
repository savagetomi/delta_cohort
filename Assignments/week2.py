lastbal = []
pin = 1234
accountBalance = 0

while True:
    register = int(input("Welcome to Naija Simple ATM,\n1. Register:\n"))
    if register == 1:
        regnum = input("Please Input your Mobile Number:\n")
        regnu = regnum[1:]
        print(regnu)
        lentt = len(regnum)
        if lentt < 11:
            print("Invalid Number")
        elif lentt > 11:
            print("Invalid Number")
        else:
            regname = input("Please Input your Name:\n")
            print(f"Registration is complete, Your Account Number is {regnu} and Account Name is {regname}")
    while True:
                option = int(input("Welcome to Naija Simple ATM,\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Buy Data\n6. Exit\n "))
                if option == 1:
                        pininput = int(input("Please input your pin:\n "))
                        if pininput == pin:
                            print(f"Your account Balance is {accountBalance}")

                        else:
                            print("Incorrect PIN")
                elif option == 2 :
                    amountdepo = int(input("Please input the amount you want to Deposit: "))
                    # slicing --------- print(amount[1:])
                    if amountdepo <= 100:
                        print("Invalid Amount, Minimum deposit is NGN100")
                    else:
                        accountBalance += amountdepo
                        lastbal.append(accountBalance)
                        print(f"Your Deposit of {amountdepo} was successful and your new account Balance is {accountBalance}")
                elif option == 3 :
                    amountwithdraw = int(input("How much are you willing to Withdraw\n1. 1000\n2. 2000\n3. 5000\n4. 10000\n5. 20000\n6. 50000\n Input Custom Amount: "))
                    if amountwithdraw == 1:
                        withdrawbalance1 = accountBalance - 1000
                        if 1000 > accountBalance:
                            print("Insufficient Balance")
                        else:
                            if withdrawbalance1 < 1000:
                                print("You cannot have less than NGN1000 in your account")
                            else:
                                pininput1 = int(input("You're about to withdraw 1000,Input your pin to complete transaction: "))
                                if pininput1 == pin:
                                    print(f"You have successfully withdrawn the sum of NGN 1000, Your available Balance is {withdrawbalance1}")
                                else:
                                    print("Incorrect PIN")
                    elif amountwithdraw == 2:
                        withdrawbalance2 = accountBalance - 2000
                        if 2000 > accountBalance:
                            print("Insufficient Balance")
                        else:
                            if withdrawbalance2 < 1000:
                                print("You cannot have a zero account, you would need atleast NGN1000 in your account")
                            else:
                                pininput2 = int(input("You're about to withdraw 2000,Input your pin to complete transaction: "))
                                if pininput2 == pin:
                                    print(f"You have successfully withdrawn the sum of NGN 1000, Your available Balance is {withdrawbalance2}")
                                    
                                else:
                                    print("Incorrect PIN")
                    elif amountwithdraw == 3:
                        withdrawbalance3 = accountBalance - 5000
                        if 5000 > accountBalance:
                            print("Insufficient Balance")
                        else:
                            if withdrawbalance3 < 1000:
                                print("You cannot have a zero account,you would need atleast NGN1000 to keep the account active")
                            else:
                                pininput3 = int(input("You're about to withdraw 5000,Input your pin to complete transaction: "))
                                if pininput3 == pin:
                                    print(f"You have successfully withdrawn the sum of NGN 5000, Your available Balance is {withdrawbalance3}")
                                    
                                else:
                                    print("Incorrect PIN")
                    elif amountwithdraw == 4:
                        withdrawbalance4 = accountBalance - 10000
                        if 10000 > accountBalance:
                            print("Insufficient Balance")
                        else:
                            pininput4 = int(input("You're about to withdraw 50000,Input your pin to complete transaction: "))
                            if pininput4 == pin:
                                print(f"You have successfully withdrawn the sum of NGN 10000, Your available Balance is {withdrawbalance4}")
                                
                            else:
                                print("Incorrect PIN")
                    elif amountwithdraw == 5:
                        withdrawbalance5 = accountBalance - 20000
                        if 20000 > accountBalance:
                            print("Insufficient Balance")
                        else:
                            pininput5 = int(input("You're about to withdraw 20000,Input your pin to complete transaction: "))
                            if pininput5 == pin:
                                print(f"You have successfully withdrawn the sum of NGN 20000, Your available Balance is {withdrawbalance5}")
                               
                            else:
                                print("Incorrect PIN")
                    elif amountwithdraw == 6:
                        withdrawbalance6 = accountBalance - 50000
                        if 50000 > accountBalance:
                            print("Insufficient Balance")
                        else:
                            pininput6 = int(input("You're about to withdraw 50000,Input your pin to complete transaction: "))
                            if pininput6 == pin :
                                print(f"You have successfully withdrawn the sum of NGN 50000, Your available Balance is {withdrawbalance6}")
                                
                            else:
                                print("Incorrect PIN")
                    elif amountwithdraw > 100:
                        withdrawbalance7 = accountBalance - amountwithdraw
                        if withdrawbalance7 < 1000:
                            print("Insufficient Balance")
                        else:
                            pininput7 = int(input(f"You're about to withdraw {amountwithdraw},Input your pin to complete transaction: "))
                            if pininput7 == pin:
                                print(f"You have successfully withdrawn the sum of NGN {amountwithdraw}, Your available Balance is {withdrawbalance7}")
                                
                            else:
                                print("Incorrect PIN")
                    else:
                        print("Minimum withdrawal is NGN100")
            
                    print("Option 3")
                elif option == 4 :
                    accountnumber = input("Input Account Number: ")
                    lent = len(accountnumber)
                    print(lent)
                    if lent < 10:
                        print("Account Number incomplete")
                    else:
                        bank_name = int(input("Bank Name\n1. GTBank\n2. Zenith Bank\n3. UBA\n4. OPay\n5. Kuda\n "))
                        if bank_name == 1:
                            amountt = int(input("Amount: "))
                            if amountt > accountBalance:
                                print("Insufficient Balance")
                            else:
                                pinn = int(input(f"You're about to send {amountt} to {accountnumber} GTBank John Doe.\nInput your PIN: "))
                                if pinn == pin:
                                    print("Successful")
                                    break
                                else:
                                    print("Incorrect Pin")
                        elif bank_name == 2:
                            amountt = int(input("Amount: "))
                            if amountt > accountBalance:
                                print("Insufficient Balance")
                            else:
                                pinn = int(input(f"You're about to send {amountt} to {accountnumber} Zenith Bank John Doe.\nInput your PIN: "))
                                if pinn == pin:
                                    print("Successful")
                                    break
                                else:
                                    print("Incorrect Pin")
                        elif bank_name == 3:
                            amountt = int(input("Amount: "))
                            if amountt > accountBalance:
                                print("Insufficient Balance")
                            else:
                                pinn = int(input(f"You're about to send {amountt} to {accountnumber} UBA John Doe.\nInput your PIN: "))
                                if pinn == pin:
                                    print("Successful")
                                    break
                                else:
                                    print("Incorrect Pin")
                        elif bank_name == 4 :
                            amountt = int(input("Amount: "))
                            if amountt > accountBalance:
                                print("Insufficient Balance")
                            else:
                                pinn = int(input(f"You're about to send {amountt} to {accountnumber} Opay John Doe.\nInput your PIN: "))
                                if pinn == pin:
                                    print("Successful")
                                    break
                                else:
                                    print("Incorrect Pin")
                        elif bank_name == 5:
                            amountt = int(input("Amount: "))
                            if amountt > accountBalance:
                                print("Insufficient Balance")
                            else:
                                pinn = int(input(f"You're about to send {amountt} to {accountnumber} Kuda Bank John Doe.\nInput your PIN: "))
                                if pinn == pin:
                                    print("Successful")
                                    break
                                else:
                                    print("Incorrect Pin")
                        else:
                            print("Invalid Number")
                elif option == 5 :
                    phonenumber = input("Input Phone Number: ")
                    lent = len(phonenumber)
                    print(lent)
                    if lent < 11:
                        print("Phone Number incomplete")
                    else:
                        network_provider = int(input("Network Providers Name\n1. MTN\n2. Airtel\n3. GLO\n4. 9Mobile\n5. Starcomms\n "))
                        if network_provider == 1:
                            amounttt = int(input("Amount: "))
                            if amountt > accountBalance:
                                print("Insufficient Balance")
                            else:
                                pinn = int(input(f"You're about to recharge {amounttt} to {phonenumber} MTN.\nInput your PIN: "))
                                if pinn == pin:
                                    print("Successful")
                                    
                                else:
                                    print("Incorrect Pin")
                        elif network_provider == 2:
                            amounttt = int(input("Amount: "))
                            if amounttt > accountBalance:
                                print("Insufficient Balance")
                            else:
                                pinn = int(input(f"You're about to send {amounttt} to {phonenumber} Airtel.\nInput your PIN: "))
                                if pinn == pin:
                                    print("Successful")
                                
                                else:
                                    print("Incorrect Pin") 
                        elif bank_name == 3:
                            amounttt = int(input("Amount: "))
                            if amounttt > accountBalance:
                                print("Insufficient Balance")
                            else:
                                pinn = int(input(f"You're about to send {amounttt} to {phonenumber} Glo.\nInput your PIN: "))
                                if pinn == pin:
                                    print("Successful")
                                    
                                else:
                                    print("Incorrect Pin")
                        elif bank_name == 4 :
                            amounttt = int(input("Amount: "))
                            if amounttt > accountBalance:
                                print("Insufficient Balance")
                            else:
                                pinn = int(input(f"You're about to send {amounttt} to {phonenumber} 9Mobile.\nInput your PIN: "))
                                if pinn == pin:
                                    print("Successful")
                                    
                                else:
                                    print("Incorrect Pin")
                        elif bank_name == 5:
                            amounttt = int(input("Amount: "))
                            if amounttt > accountBalance:
                                print("Insufficient Balance")
                            else:
                                pinn = int(input(f"You're about to send {amounttt} to {phonenumber} Starcomms.\nInput your PIN: "))
                                if pinn == pin:
                                    print("Successful")
                                    
                                else:
                                    print("Incorrect Pin")
                        else:
                            print("Invalid Number")
                elif option == 6  :
                    print("Thanks for using our Service")
                    break