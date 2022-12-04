########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

class Control():
    def get_control_int(control):
        if control == "Public": return 0
        elif control == "Confidential": return 1
        elif control == "Privileged": return 2
        elif control == "Secret": return 3

    def read(subjectControl, assetControl):
        if (Control.get_control_int(subjectControl) >= Control.get_control_int(assetControl)) is False:
            print("Read access denied")
            return False
        return True
    
    def write(subjectControl, assetControl):
        if (Control.get_control_int(subjectControl) <= Control.get_control_int(assetControl)) is False:
            print("Write access denied")
            return False
        return True
