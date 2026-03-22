from typing import Callable

def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Provide username and phone is format: <command> <username> <phone>"
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Username is missing: <command> <username>"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    return inner

@input_error
def parse_input(user_input):
    if not user_input.strip():
        raise ValueError
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact '{name}' updated."
    raise KeyError

@input_error
def show_phone(args, contacts):
    name = args[0]
    return f"{name}'s phone: {contacts[name]}"

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = []
    count_id = 0
    for name, phone in contacts.items():
        count_id += 1
        result.append(f"{count_id} | {name}: {phone}")
    return "\n".join(result)

def show_commands():
    text = {
        'Add New User': "add <username> <phone>",
        'Change user phone': "change <username> <new phone>",
        'Check user phone': "phone <username>",
        "See all contacts": "all"
    }
    print("    List of available commands:")
    for purpose, command in text.items():
        print(f"    > {purpose}: {command}")  

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "help":
            show_commands()
        else:
            print("Invalid command. Enter 'help' to see all commands.")

if __name__ == "__main__":
    main()
