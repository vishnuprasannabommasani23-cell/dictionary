Contacts = {}
while True:
    print("\nCONTACT MANAGEMENT SYSTEM")
    print("1.Add Contact")
    print("2.Search Contact")
    print("3.Update Contact")
    print("4.Delect Contact")
    print("5.Display Contact")
    print("Exit")
    choice=int(input("enter choice"))
    if choice==1:
        name = input("enter name:")
        phone = input("enter phone:")
        Contacts[name]=phone
        print("contact Added Successfully")
    
    elif choice==2:
        name = input("enter name:")
        if name in Contacts:
                print("Contact Not Found")
        else:
                print("Contact Not Found")
    elif choice==3:
         name = input("enter name:")
         if name in Contacts:
            Phone=input("enter New Phone:")
            Contacts[name]=Phone
            print("Update Successfully")
         else:
                print("Contact Not Found")
    elif choice==4:
         name = input("enter name:")
         if name in Contacts:
                del Contacts[name]
                print("Deleted Successfully")
         else:
                print("Contact Not Found")
    elif choice==5:
            print("\nCONTACT LIST")
            for name,phone in Contacts.items():
                print(name,"\t",phone)
    elif choice==6:
            print("Thank you")
            break
    else:
            print("Invalid Choice")
