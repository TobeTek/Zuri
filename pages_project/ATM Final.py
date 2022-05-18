# author: Tobe
# date: 13/04/2021
# title: Improved ATM program

from datetime import datetime
import shelve
import random
import string
import sys

#Declare global variables
allowedUsers= ['Seyi','Mike','Love']
acctBalance = [100, 1900, 300]
allowedPassword= ['passwordSeyi', 'passwordMike', 'passwordLove']
acctNumbers= [1092039312, 2342346578, 1234234567]

def init(): # Understand the type of customer
    while True:
        ans= input('Are you a registered user? (Yes/No)\n')
        ans= ans.lower()
        if ans == 'yes':
            userLogin()
            break
        if ans == 'no':
            createUser()
            break
        else:
            print('Please enter a valid response')

def userLogin(): 
    try:  # See if the system already has saved data
        shelFile= shelve.open('sysdata')
        allowedUsers = shelFile['aUsers']
        allowedPassword= shelFile['aPassword']
        acctNumbers= shelFile['acctNumbers']
        acctBalance = shelFile['Balance']
        #shelFile.sync()
        shelFile.close()
    except:  # If not give it data
        shelFile = shelve.open('sysdata')
        shelFile['aUsers'] = allowedUsers
        shelFile['aPassword'] = allowedPassword
        shelFile['acctNumbers'] = acctNumbers
        shelFile['Balance'] = acctBalance
        shelFile.close()
        
    login = True # Loop over the login process to give space for error
    while login == True:
        name = input('What is your name?\n')

        if(name in allowedUsers):
            print('Name found')
            namePosition= allowedUsers.index(name)
            
            tries = 0
            cnt = True
            while cnt == True:    # Conditional to check if the user wants to quit
                password = input('Please enter password:\n')
                if(password == allowedPassword[namePosition]):
                    login = False
                    while True:
                        now = datetime.now()
                        print(now)
                        print('Welcome %s' %name)
                        print('Available actions: on %d' %acctNumbers[namePosition])
                        print('1. Withdrawal\n2. Cash Deposit\n3. Check Balance\n4. Change Password\n5.Transfer\n6. Complaint')
                        choice= input('What would you like to do today:\n')
                        if choice == '1':
                            print('You seleceted %s' %choice)
                            withdrawAmount =float(input('How much would you like to withdraw? :'))
                            print('Take your cash # %g ' %withdrawAmount)
                            acctBalance[namePosition] = acctBalance[namePosition] - withdrawAmount
                            print('Current Balance: %g' %(acctBalance[namePosition]))
                            shelFile = shelve.open('sysdata')   # Write data to drive
                            shelFile['Balance'] = acctBalance
                            shelFile.close()
                            cnt = False
                            break
                            
    
                        elif choice == '2':
                            print('You seleceted %s' %choice)
                            depositAmount =float(input('How much would you like to deposit? :'))
                            acctBalance[namePosition] = acctBalance[namePosition] + depositAmount
                            print('Current Balance: #%g' %(acctBalance[namePosition]))
                            shelFile = shelve.open('sysdata')   # Write data to drive
                            shelFile['Balance'] = acctBalance
                            shelFile.close()    
                            cnt = False
                            break
                            
                        elif choice == '3':
                            print('You seleceted %s' %choice)
                            print('Current Balance: %g' %acctBalance[namePosition])
                            cnt = False
                            break
                            
                        elif choice == '4':
                            print('You selected %s' %choice)
                            newPwd= input( 'Enter new password:\n')
                            confirmatory = input('Confirm new password:\n')
                            if newPwd == confirmatory:
                                allowedPassword[allowedUsers.index(name)] = newPwd
                            else:
                                print('Unable to complete process')
                            shelFile = shelve.open('sysdata')       # Write data to drive
                            shelFile['aPassword'] = allowedPassword
                            shelFile.close()
                            cnt = False
                            break

                        elif choice == '5':
                            print('You seleceted %s' %choice)
                            response = input("Enter recipients' account number or username\n")
                            amt = int(input('Enter the amount to transfer')) 
                            if (response in allowedUsers):
                                print('You have transferred %g to %s' %(amt ,response))
                                acctBalance[allowedUsers.index(response)] = acctBalance[allowedUsers.index(response)] + amt      
                                shelFile = shelve.open('sysdata')   # Write data to drive
                                shelFile['Balance'] = acctBalance
                                shelFile.close()    
                            
                            elif (response in acctNumbers):
                                print('You have transferred %g to %d' %(amt ,response))
                                acctBalance[namePosition] = acctBalance[namePosition] - amt
                                acctBalance[acctNumbers.index(response)] = acctBalance[acctNumbers.index(response)] + amt      
                                shelFile = shelve.open('sysdata')   # Write data to drive
                                shelFile['Balance'] = acctBalance
                                shelFile.close()    
                            
                            else:
                                print('Invalid account details')
                            cnt = False
                            break

                        elif choice == '6':
                            print('You seleceted %s' %choice)
                            complaint = input('What is your complaint?:\n')
                            print('Thank you for reaching us.')
                            cnt = False
                            break
                            
                        else:
                            response = input('Invalid option selected, to try again press 1 , to exit 2: ')
                            if response == '2':
                                cnt = False
                                sys.exit()
            
                else:
                    print('Password Incorrect, please try again')
                    tries = tries + 1
                    if tries >= 3:
                        print( 'Please try again later')
                        login = False
                        cnt = False
                        break
        
        else:
            response= input ('Name not found, press  1 to try again, or 2 to exit: ')
            if response == '2':
                sys.exit()
def createUser():
    
    name= input('Enter your username:\n')
    pwd= input('Enter your secret password: ')
    allowedUsers.append(name)
    allowedPassword.append(pwd)
    acctNumbers.append(int(accountNumber()))
    acctBalance.append(0)
    shelFile = shelve.open('sysdata')
    shelFile['aUsers'] = allowedUsers
    shelFile['aPassword'] = allowedPassword
    shelFile['acctNumbers'] = acctNumbers
    shelFile['Balance'] = acctBalance
    shelFile.close()

def accountNumber():
    Number= []
    a = string.digits
    for i in range(10):
        Number.append(random.choice(a))
    return ''.join(Number)

#--------------------------------------------------------------------------------------
    


init()


