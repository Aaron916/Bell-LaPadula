########################################################################
# COMPONENT:
#    MESSAGES
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of a collection of messages
########################################################################

import control, message

##################################################
# MESSAGES
# The collection of high-tech messages
##################################################
class Messages:

    ##################################################
    # MESSAGES CONSTRUCTOR
    # Read a file to fill the messages
    ##################################################
    def __init__(self, filename):
        self._messages = []
        self._read_messages(filename)

    ##################################################
    # MESSAGES :: DISPLAY
    # Display the list of messages
    ################################################## 
    def display(self, _control):
        for m in self._messages:
            if control.Control.read(_control, m._textcontrol):
                m.display_properties()

    ##################################################
    # MESSAGES :: SHOW
    # Show a single message
    ################################################## 
    def show(self, id, _control):
        for m in self._messages:
            if m.get_id() == id and control.Control.read(_control, m._textcontrol):
                m.display_text()
                return True
        return False

    ##################################################
    # MESSAGES :: UPDATE
    # Update a single message
    ################################################## 
    def update(self, id, text, _control):
        for m in self._messages:
            if m.get_id() == id and control.Control.write(_control, m._textcontrol):
                m.update_text(text)

    ##################################################
    # MESSAGES :: REMOVE
    # Remove a single message
    ################################################## 
    def remove(self, id, _control):
        for m in self._messages:
            if m.get_id() == id and control.Control.write(_control, m._textcontrol):
                m.clear()

    ##################################################
    # MESSAGES :: ADD
    # Add a new message
    ################################################## 
    def add(self, text_control, text, author, date):
        m = message.Message(text_control, text, author, date)
        self._messages.append(m)

    ##################################################
    # MESSAGES :: READ MESSAGES
    # Read messages from a file
    ################################################## 
    def _read_messages(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    text_control, author, date, text = line.split('|')
                    self.add(text_control, text.rstrip('\r\n'), author, date)

        except FileNotFoundError:
            print(f"ERROR! Unable to open file \"{filename}\"")
            return
