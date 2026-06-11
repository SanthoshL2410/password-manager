
def add():
    website = input("Enter Website: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    file = open("passwords.txt", "a")
    file.write(f"Website: {website}\n")
    file.write(f"Username: {username}\n")
    file.write(f"Password: {password}\n")
    file.write("------------------------\n")
    file.close()

    print("Password Saved Successfully!")


def view():
    try:
        file = open("passwords.txt", "r")
        print("\nSaved Passwords:\n")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("No passwords saved yet.")


while True:
    print("\nPASSWORD MANAGER")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add()

    elif choice == "2":
        view()

    elif choice == "3":
        print("Exiting Program.")
        break

    else:
        print("Invalid Choice")