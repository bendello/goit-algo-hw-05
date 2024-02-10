def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid number of arguments provided."
    return inner

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Error: Please enter a name and phone number.")
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Error: Please enter a name and new phone number.")
    name, phone = args
    if name not in contacts:
        raise KeyError("Error: Contact not found.")
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError("Error: Please enter a name.")
    name = args[0]
    if name not in contacts:
        raise KeyError("Error: Contact not found.")
    return f"{name}: {contacts[name]}"

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def show_help():
    
    help_text = """
Available commands:
    hello - Greet the user.
    add [name] [phone] - Add a new contact.
    change [name] [new phone] - Change the phone number of an existing contact.
    phone [name] - Show the phone number of a contact.
    all - Show all saved contacts.
    help - Show available commands.
    close, exit - Exit the program.
    """
    return help_text

def main():
    contacts = {}
    print("Welcome to the assistant bot! Type 'help' to see all commands.")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            response = add_contact(args, contacts)
            print(response)
        elif command == "change":
            response = change_contact(args, contacts)
            print(response)
        elif command == "phone":
            response = show_phone(args, contacts)
            print(response)
        elif command == "all":
            response = show_all(contacts)
            print(response)
        elif command == "help":
            print(show_help())
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
