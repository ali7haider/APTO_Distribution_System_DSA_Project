import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from BL.Credentials import credential
from BL.User import user
class admin(user):
    def __init__(self,userName,password,name,cnic,email,cellNo,Id,dateCreated):
        self.login = credential(userName, password, "Admin")
        super(). __init__(name,cnic,email,cellNo,Id , dateCreated)