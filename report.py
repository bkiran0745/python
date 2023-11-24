import stakeholder as st
account =[]
invest=['Bond Paper','Shares','Cash','Land']
def create_stakeholder():
    print("\n Welcome TO Creation of Stakeholders Section \n")
    Name = input("\nEnter you'r Name:")
    account.append(Name)
    company = input("\nCompany Name:")
    account.append(company)
    investing_amount = int(input("\nInvesting Amount:"))
    account.append(investing_amount)
    k=1
    while(k==1):
        print("\n1.Bond Paper")
        print("2.Shares")
        print("3.Cash")
        print("4.Land\n")
        try:
            k=0
            investing_Type = int(input("\nInvesting Type : "))
            account.append(invest[investing_Type-1])
            pas=input("\ncreate your password:")
            account.append(pas)
            print("\nyour user name:",Name)
            print("\nyour passwrd:",pas)
            st.insert(account,account[0])
        except:
            print("\nInvalid Input\n")
def view_stakeholder():
    print("\nThese are the Stackholder we have:\n")
    st.display_all()
def edit_stakeholder(user):
    print("\nWhich part do u want to edit:")
    print("\n1.Name\n2.Company Name\n3.Investement Amount\n4.Investement Type\n5.password\n")
    choice=int(input("\nEnter your choice:"))
    elem=input("\nEnter the your new value(EX:Name=pavan->Name=Kumar):")
    st.Edit_details(user,choice,elem)
    print("\nEditing is completed:")
    st.Display(user)
def delete_stakeholder():
    delete = input("\nEnter the username to delete:")
    password=input("\nEnter the password to delete:")
    if st.validetion(delete,password):
        st.Delete(delete)
    else:
        print("\nSorry something went wrong check your password or username\n")

def stake_holders(usna):
    while(True):
        print("\n1. View Stakeholder")
        print("2. Edit StakeHolder Details")
        print("3. Delete StakeHolder")
        print("4. Exit\n")
        choice = int(input("\nChoose the appropriate option:"))
        if choice == 1:
            view_stakeholder()
        elif choice == 2:
            edit_stakeholder(usna)
        elif choice == 3:
            delete_stakeholder()
        elif choice == 4:
            print("Thank You\n")
            break
        else:
            print("\nEnter the Appropriate choice..\n")
def log():
    n=0
    while(True):
        print("\n1.Log-in")
        print("2.Sign-up")
        print("3.Exit\n")
        choice=input("choose the option to go forword:")
        if choice=='1':
            usna=input("\nEnter your user name:")
            password=input("\nEnter your password:")
            if st.validetion(usna,password):
                stake_holders(usna)
            else:
                print("\nuser or password is not matched \n")
        elif choice=='2':
            create_stakeholder()
        elif choice == '3':
            print("\nThank you..!\n")
            break
        else:
            print("\nchoose the Right option..\n")
def suggest_stackholder():
    amount=int(input("\nHow much amount investment do u need: "))
    type=input("\nwhich type of investment do u want:")
    st.suggestion(amount,type)
def client():
    while(True):
        print("\n1.view stakeholders\n2.suggest stackholder\n3.Exit\n")
        choice1=input("\nEnter your choice:")
        if choice1=="1":
            st.display_all()
            user=input("\nWhich stackholder do you want:")
            if st.validet_username(user):
                st.Display(user)
                print("\nYou Have Collabrated with\n",user)
            else:
                print("Sorry we for inconvience we do not have your reqrement")
        elif choice1=="2":
            suggest_stackholder()
        else:
            print("\n   Thank You...\n")
            break
while(True):
    print("\nDo you want to Log-In as Stakeholder or Client\n")
    print("1.StakeHolder")
    print("2.Client")
    print("3.Exit\n")
    try:
        choice = int(input("Enter your choice : "))
        if choice == 1:
            log()
        elif choice == 2:
            client()
        elif choice == 3:
            print("\n  Thank You...\n")
            break
        else:
            print("\nChoose the correct option.. \n")
    except ValueError as e:  
        print("\nEnter proper values only..\n")



