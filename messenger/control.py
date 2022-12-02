########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, Aaron Rooks, Daxton Wirth
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################
class Control():
    def __init__(self):
        self.PUBLIC = 0
        self.CONFIDENTIAL = 1
        self.PRIVILEGED = 2
        self.SECRET = 3

    def securityConditionRead(subjectControl, assetControl):
        return subjectControl >= assetControl
    
    def securityConditionWrite(subjectControl, assetControl):
        return subjectControl <= assetControl

    def read(subjectControl, assetControl, self):
        if (self.securityConditionRead(subjectControl, assetControl) is False):
            print("Read access denied")
            return False
        return True
    
    def write(subjectControl, assetControl, self):
        if (self.securityConditionWrite(subjectControl, assetControl) is False):
            print("Write access denied")
            return False
        return True
