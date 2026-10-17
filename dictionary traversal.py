contacts={}
while True:
    print("\n CONTACT MANAGEMENT SYSTEM")
    print("1.Add contact")
    print("2.Search Contact")
    print("3.Update Contact")
    print("4.Delete Contact")
    print("5.Display Contacts")
    print("6.Exit")
    choice=int(input("Enter Choice:"))
    if choice==1:
        name=input("Enter name:")
        phone=input("enter phone:")
        contacts[name]=phone
        print("Contact Added Successfully")
        elif choice==2:
            name=input("Enter Name:")
            if name in contacts:
                print("phone:",contacts[name])
            else:
                print("Contact Not Found")
        elif choice==3:
            name=input("Enter Name:")
            if name in contact:
                phone=input("Enter New phone:")
                contacts[name]=phone
                print("Update Successfully")
            else:
                print("Contact Not Found")
            elif choice==4:
                name=input("Enter Name:")
                if name in contacts:
                    del contacts[name]
                    print("Delete Successfully")
                else:
                    print("Contact Not Found")
                eli choice==5:
                    print("\nCONTACTLIST")
                    for name,phone in contact.items():
                        print(name,"\t",phone)
                    elif choice==6:
                        print("Thank you")
                        break
                    else:
                        print("Invalid Choice")
                        
                    
                    

    








         
    
    
