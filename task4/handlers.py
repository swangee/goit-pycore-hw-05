from functools import partial
import error


add_contact_error = partial(
    error.input_error,
    value_error="Please enter both name and phone number."
)


@add_contact_error
def add_contact(args, contacts: dict):
    """
    Adds new contact to the contact list

    :param args: expects two arguments: name and phone
    :param contacts: contacts dictionary
    :return:
    """
    if len(args) < 2:
        raise ValueError

    set_contact_phone(args, contacts)

    return "Contact has been added.", False


def exit(args, contacts: dict):
    """
    Returns goodbye message with the termination flag
    :return:
    """
    return "Good bye!", True


def hello(args, contacts: dict):
    """
    Returns welcome message
    :return:
    """
    return "How can I help you?", False


set_contact_phone_error = partial(
    error.input_error,
    value_error="Please enter both name and phone number."
)


@set_contact_phone_error
def set_contact_phone(args, contacts: dict):
    """
    Changes contact phone number if it exists

    :param args: expects two arguments: name and phone
    :param contacts: contacts dictionary
    :return:
    """
    name, phone = args

    if name not in contacts:
        raise KeyError

    contacts[name] = phone

    return "Contacts' phone has been changed.", False


get_contact_phone_error = partial(
    error.input_error,
    value_error="Please enter both name and phone number."
)


@get_contact_phone_error
def get_contact_phone(args, contacts: dict):
    """
    Returns contact phone number if it exists

    :param args: expects one argument: name
    :param contacts: contacts dictionary
    :return: contact phone number
    """

    name = args[0]

    if name not in contacts:
        raise KeyError

    return contacts[name], False


def get_contacts_list(args, contacts: dict):
    """
    Returns contacts list as a string

    :param args: doesn't expect any arguments
    :param contacts: contacts dictionary
    :return: list of contacts in a string representation
    """

    output = ""

    for contact, phone in contacts.items():
        output += f"{contact} - {phone}\n"

    return output, False


def render_help(commands: dict):
    """
    Renders help message with the commands list
    :param commands:
    :return:
    """
    output = "list of allowed commands: ["

    for command in commands:
        output += f"{command},"

    output = output.strip(',')

    return output + "]"
