#first module(starting of project)
from spy_detail import spy,spy1,chatmessage, friends
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored

#add status messageska
status_message=['My name is Ruchi.',"what's up",'bring me back.','walk with faith.']

print"hi"
print"Let's get started."

#your choice to start app
question="continue as " + spy.salutation+ " " + spy.name + "(Yes/No)?"
existing=str(raw_input(question))


def add_status():

    updated_status_message = None                                                 #add_status function which is used to add new status or use older status.


    if spy.current_status_message != None:
        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'


    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")


        if len(new_status_message) > 0:
            status_message.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in status_message:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))


        if len(status_message) >= message_selection:
            updated_status_message = status_message[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message

def add_friend():
    new_friend = spy1('','',0,0.0)

    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")                                #add_friend function is used to add another new friends in chat.

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)


#select a friend whom with you want to chat.
def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number + 1, friend.name,
                                                             friend.age,
                                                             friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def send_message():

     friend_choice = select_a_friend()

     original_image = raw_input("What is the name of the image?")                                 #send a secret messgae within a photo.
     output_path = "output.jpg"
     text = raw_input("What do you want to say? ")

     Steganography.encode(original_image, output_path, text)
     new_chat = chatmessage(text,True)

     friends[friend_choice].chats.append(new_chat)
     print "Your secret message image is ready!"


     print"please send some message."

#read a secret messgae.
def read_message():
    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)

    new_chat = chatmessage(secret_text,False)

    friends[sender].chats.append(new_chat)


    print "Your secret message has been saved!"


#history details
def read_chat_history():

    read_for = select_a_friend()

    print '\n6'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' %(colored(chat.time.strftime("%d %B %Y"),'blue'),colored(spy.name,'red'),chat.message)
        else:
            print '[%s] %s said: %s' %(colored(chat.time.strftime("%d %B %Y"),'blue'),colored( friends[read_for].name,'red'), chat.message)


#function declaration
def start_chat(spy):
    current_status_message = None

    spy.name = spy.salutation + " " + spy.name

    if spy.age > 12 and spy.age < 50:

        print "Authentication complete. Welcome  "  + spy.name +  "  age: " + str(spy.age) + "  and rating of: " + str(
            spy.rating) + " Proud to have you onboard."

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    print 'You choose to update the status.'
                    spy.current_status_message=add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy!'


if existing == "Yes":
    start_chat(spy)
else:
    spy =spy1('','',0,0.0)
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)
        if(spy.rating)> 4.5:
            print"you are great one."
        elif(spy.rating)> 3.5and(spy.rating)<=4.5:
            print"it's good."
        elif(spy.rating)>2.5 and (spy.rating)<=3.5:
            print"you are on right track."
        else:
            print"please enter valid rating."

        start_chat(spy)
    else:
        print 'Please add a valid spy name'
