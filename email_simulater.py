# This program simulates a simple email application that allows
# the user to view and interact with a list of emails.

# Define the Email class and the attributes
class Email:
    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content


# Define an empty list to hold emails
Inbox = []


# Define a function to populate the inbox with some example emails
def populate_inbox():
    email_one = Email('luci@gmail.com', 'Greeting', 'Welcome, HiperyonDEv')
    email_two = Email('igor@gmail.com', 'Math lesson', 'do not forget to do your lessons')
    email_three = Email('george@gmail.com', 'Soccer Game', 'good luck with you match today!')
    Inbox.append(email_one)
    Inbox.append(email_two)
    Inbox.append(email_three)

# Call the populate_inbox function to create some example emails
populate_inbox()

# Define a function to list the email subjects in the inbox
def list_emails():
    if not Inbox:
        print('Empty box')
    else:
        print('Inbox email: ')
        for i, email in enumerate(Inbox):
            print(f'{i + 1} {email.subject_line}')

# Define a function to read an email from the inbox
def read_email():
    user_choice = int(input("Enter the email Id that you want to read or 0 to return to main menu: "))
    for i, email in enumerate(Inbox):
        if i + 1 == user_choice:
            print(f'Email address: {email.email_address} \n')
            print(f'Subject: {email.subject_line} \n')
            print(f'Content: {email.email_content} \n')
            email.has_been_read = True
            user_action = int(input('''What do you want to do?
            [0] Delete the email?
            [1] Return main menu?'''))
            if user_action == 0:
                Inbox.remove(email)
                print('Email successfully deleted!')
                break
            elif user_action == 1:
                break
        elif user_choice == 0:
            break
        else:
            print('*' * 40)
            print(f'Ooops... That was not valid! Try again.')


# Define a function to list the unread emails in the inbox
def list_unread_emails():
    unread_emails = [email for email in Inbox if not email.has_been_read]
    if not unread_emails:
        print("You have no unread emails.")
    else:
        print("Your unread emails:")
        for email in unread_emails:
            print(f"{email.subject_line}")



# Define a while loop to display the menu and respond to user choices
while True:
    try:
        print('*' * 40)
        choice = int(input('''Enter what do you want to do?
        [1] Read e-mail
        [2] View unread emails
        [3] Quit the application'''))
        print('*' * 30)
        if choice == 1:
            list_emails()
            read_email()
        elif choice == 2:
            list_unread_emails()
        elif choice == 3:
            print('Goodbye!')
            exit()

    except ValueError:
        print(f'Ooops... That was not valid! Try again.')
