

from pathlib import Path
import json
import random
import string 



class Bank:
    database = "data.json"
    data = []

    try:
        if Path(database).exists():
            print("file exists")
            with open(database) as fs:
                data = json.loads(fs.read())

        else:
            print("file dosent exists!!")

    except Exception as err:
        print(f"error...{err}")

    @classmethod
    def update(cls):
        with open(Bank.database,"w") as fs:
            fs.write(json.dumps(cls.data))

    @staticmethod    
    def generate():
        digits = random.choices(string.digits,k=4)
        alpha = random.choices(string.ascii_letters,k=4)
        id = digits + alpha
        random.shuffle(id)
        return "".join(id)



    # create user
    def createacc(self):
        info = {
            'name' : input("enter your name"),
            'age' : int(input("enter your age")),
            'email' : input("entery your email"),
            'pin' : int(input("enter tour pin")),
            'account' : Bank.generate(), #''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
            'balance': 0,
            'phoneno.': int(input("enter your phone number"))
        }
        if info['age'] >= 18 and len(str(info['pin'])) == 4 and len(str(info['phoneno.'])) == 10:
            Bank.data.append(info)
            Bank.update()
            print("data added in list")
            # print(Bank.data)
        else:
            print("unvalid credintials")

    def depositemoney(self):
        acc = input("enter your account no ")
        pinno = int(input("enter your pin "))

        user_data = [i for i in Bank.data if i['account']== acc and i['pin'] == pinno]
        if user_data == False:
            print(("user not found"))
        else:
            amount = int(input("enter your amount"))
            if amount <= 0:
                print("invalid amount")
            elif amount > 10000:
                print("enter the lessser amount")
            else:
                user_data[0]['balance'] += amount
                Bank.update()
                print("amount creadted") 

    def withdrow(self):
        accountno = input("enter your account")
        pin = int(input("enter your pin"))
        user_data = [i for i in Bank.data if i['account']==accountno and i['pin']==pin]

        if user_data == False:
            print("no user found")
        else:
            amount = int(input("enter your amount"))
            if amount <= 0:
                print("invalid amount")
            elif amount > 10000:
                print("enter the lessser amount")
            else:
                if user_data[0]['balance'] < amount:
                    print("invalid amount")
                else:
                    user_data[0]['balance'] -= amount
                    Bank.update()
                    print("amount debited")
    
    def details(self):
        acc = input("enter your account")
        pinno = int(input("enter your pin"))
        user_data = [i for i in Bank.data if i['account'] == acc and i['pin']==pinno]

        if user_data == False:
            print("no user found")
        else:
            for key, value in user_data[0].items():
                print(f"{key}: {value}")
    

    def delete(self):
        accountno = input("enter your account")
        pin = int(input("enter your pin"))
        user_data = [i for i in Bank.data if i['account']==accountno and i['pin']==pin]

        if user_data == False:
            print("no user found")
        else:
            choic = input("are you sure to remove the data(Yes or No)")
            if choic == 'Yes' or 'yes' or 'YES':
                index = Bank.data.index(user_data[0])
                Bank.data.pop(index)
                Bank.update()
                print("deleted!!")
            else:
                print("operation terminated")


    def updatedetails(self):
        accountno = input("enter your account")
        pin = int(input("enter your pin"))
        user_data = [i for i in Bank.data if i['account']==accountno and i['pin']==pin]

        if user_data == False:
            print("no user found")
        else:
            print("print are you surely want to update your details")
            print("to update enter your new details or just enter to pass")

            dect = {
                'newname' : input("enter your name"),
                'newage' : input("enter new age"),
                'newemail' : input("enter new email"),
                'newpin' : input("enter new pin"),
                'newphoneno' : input("enter new phone number")
            }

            for key, value in dect.items():
                if value == "":
                    continue
                elif key == 'newname':
                    user_data[0]['name'] = value
                elif key == 'newage':
                    user_data[0]['age'] = int(value)
                elif key == 'newemail':
                    user_data[0]['email'] = value
                elif key == 'newpin':
                    user_data[0]['pin'] = int(value)
                elif key == 'newphoneno':
                    user_data[0]['phoneno.'] = int(value)
                    print("details updated")
                Bank.update()
                
                                

                






