# 13. Basic Contact Book
# 1. Add contact
# 2. View contact
# 3. Delete contact
# 4. View all contacts
# 5. Exit
contact = {}

def add_contact():
    global contact
    contact_name = input("Enter the name for the contact: ")
    contact_number = input(f"Enter the phone_number for the {contact_name}: ")
    contact[contact_name] = contact_number
    print("Contact info Added successfully")

def view_contact():
    global contact
    print(contact.values())
    
def del_contact():
    global contact
    delete_key = input("Enter the name for the phone number to be deleted: ")
    del contact[delete_key]
    print("contact deleted successfully")

def view_all_contact():
    global contact
    print(contact)

def exit_contact():
    exit()

def contact_book():
    menu = input("These are the available option \n 1.Add Contact \n 2. View Contact \n 3. Delete Contact \n 4.View all contacts \n 5.Exit: \n")
    if menu =="1":
        add_contact()
    elif menu == "2":
        view_contact()
    elif menu == "3":
        del_contact()
    elif menu == "4":
        view_all_contact()
    elif menu == "5" :
        exit_contact()
    else:
        print("Incorrect Input")
        contact_book()
        
    print("Do you want to do another option")
    repeat = input("1. Yes 2. No \n")
    if repeat == "1":
        contact_book()
    else:
        print("Thank you for your time")
        exit()
        
contact_book()