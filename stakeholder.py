stakeholder_Dictionary={
            'kiran':['kiran','KKS','100000.0','Cash','6949'],
            'B kiran':['B kiran','BK','300000.0','Bonds','1234'],
            'B Pavan':['B Pavan','BPK','700000.0','Land','4321'],
            'Anas':['Anas','MAS','800000.0','Shares','0987'],
        }
def insert(lis,name):
    stakeholder_Dictionary[name]=lis

def Display(user):
    if user in stakeholder_Dictionary:
        name,company,amount,intype,a5=stakeholder_Dictionary[user]
        print("Name : ", name)
        print("Company Name : ", company)
        print("Investement Amount : ",amount)
        print("Investement Type : ",intype)
    else:
        print("User not found")

def Delete(user):
    if user in stakeholder_Dictionary:
        print("Deleting below user:\n")
        print(stakeholder_Dictionary[user])
        del stakeholder_Dictionary[user]
        print("\n Deleted\n") 

    else:
        print("User not found")

def display_all():
    print("{:<10}{:<10}{:<10}{:<10}".format('NAME','Company ','Amount','Type'))
    for key,value in stakeholder_Dictionary.items():
           NAME,Company_Name,Investement_Amount,Investement_Type,a5=value
           print("{:<10}{:<10}{:<10}{:<10}".format(NAME,Company_Name,Investement_Amount,Investement_Type))

def Edit_details(user,index,edit_value):
    temp=[]
    temp=stakeholder_Dictionary[user]
    temp.remove(temp[index-1])
    temp.insert(index-1,edit_value)
    stakeholder_Dictionary[user]=temp

def validetion(user,password):
    if user in stakeholder_Dictionary:
        print("user id is verifide")
        a1,a2,a3,a4,password1=stakeholder_Dictionary[user]
        if password==password1:
            print("password is verified:")
            return True
        else:
            print("password is incorrect")
            return False
    else:
        print("user is not found")
        return False
def validet_username(name):
    if name in stakeholder_Dictionary:
        return True
    else:
        return False     
def suggestion(amount,type):
    k=0
    for key,value in stakeholder_Dictionary.items():
        at=value
        if amount and type in at:
            print("this is our suggestion:",at[0])
            k=1
    if k==0:
        print("Sorry we dont have your required")
        print("if we get the type u need we will suggest you")
    
