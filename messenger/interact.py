########################################################################
# COMPONENT:
#    INTERACT
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class allows one user to interact with the system
########################################################################

import messages, control

###############################################################
# USER
# User has a name and a password
###############################################################
class User:
    def __init__(self, name, password, control):
        self.name = name
        self.password = password
        self.control = control

userlist = [
   [ "AdmiralAbe",     "password",  "Secret" ],  
   [ "CaptainCharlie", "password" , "Privileged"], 
   [ "SeamanSam",      "password" , "Confidential"],
   [ "SeamanSue",      "password" , "Confidential"],
   [ "SeamanSly",      "password" , "Confidential"]
]

###############################################################
# USERS
# All the users currently in the system
###############################################################
users = [*map(lambda u: User(*u), userlist)]

ID_INVALID = -1

######################################################
# INTERACT
# One user interacting with the system
######################################################
class Interact:

    ##################################################
    # INTERACT CONSTRUCTOR
    # Authenticate the user and get him/her all set up
    ##################################################
    def __init__(self, username, password, messages):
        self.authenticated = self._authenticate(username, password)
        self._username = username
        self.id = self._id_from_user(username)
        self.control = self._control_from_user(self.id)
        self._p_messages = messages

    ##################################################
    # INTERACT :: SHOW
    # Show a single message
    ##################################################
    def show(self, _control):
        id_ = self._prompt_for_id("display")
        if not self._p_messages.show(id_, _control):
            print(f"ERROR! Message ID \'{id_}\' does not exist")
        print()

    ##################################################
    # INTERACT :: DISPLAY
    # Display the set of messages
    ################################################## 
    def display(self, control):
        print("Messages:")
        self._p_messages.display(control)
        print()

    ##################################################
    # INTERACT :: ADD
    # Add a single message
    ################################################## 
    def add(self, _control):
        self._p_messages.add(_control,
                             self._prompt_for_line("message"),
                             self._username,
                             self._prompt_for_line("date"))

    ##################################################
    # INTERACT :: UPDATE
    # Update a single message
    ################################################## 
    def update(self, _control):
        id_ = self._prompt_for_id("update")
        if not self._p_messages.show(id_, _control):
            print(f"ERROR! Message ID \'{id_}\' does not exist\n")
            return
        self._p_messages.update(id_, self._prompt_for_line("message"), _control)
        print()
            
    ##################################################
    # INTERACT :: REMOVE
    # Remove one message from the list
    ################################################## 
    def remove(self, _control):
        self._p_messages.remove(self._prompt_for_id("delete"), _control)

    ##################################################
    # INTERACT :: PROMPT FOR LINE
    # Prompt for a line of input
    ################################################## 
    def _prompt_for_line(self, verb):
        return input(f"Please provide a {verb}: ")

    ##################################################
    # INTERACT :: PROMPT FOR ID
    # Prompt for a message ID
    ################################################## 
    def _prompt_for_id(self, verb):
        return int(input(f"Select the message ID to {verb}: "))

    ##################################################
    # INTERACT :: AUTHENTICATE
    # Authenticate the user: find their control level
    ################################################## 
    def _authenticate(self, username, password):
        id_ = self._id_from_user(username)
        return ID_INVALID != id_ and password == users[id_].password

    ##################################################
    # INTERACT :: ID FROM USER
    # Find the ID of a given user
    ################################################## 
    def _id_from_user(self, username):
        for id_user in range(len(users)):
            if username == users[id_user].name:
                return id_user
        return ID_INVALID

    ##################################################
    # INTERACT :: Control FROM USER
    # Find the Control of a given user
    ################################################## 
    def _control_from_user(self, id):
        return users[id].control


#####################################################
# INTERACT :: DISPLAY USERS
# Display the set of users in the system
#####################################################
def display_users():
    for user in users:
        print(f"\t{user.name}")
