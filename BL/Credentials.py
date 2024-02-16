class credential:    
    def __init__(self,userName,password,role):
        self.userName = ""
        self.password = ""
        self.role = ""
        self.setUserName(userName)
        self.setPassword(password)
        self.setRole(role)
    
    
    def userName(self):
        return self.userName
    
    def password(self):
        return self.password
    
    def role(self):
        return self.role
    
    def setRole(self,value):
        self.role = value
    
    def setUserName(self,value):
        self.userName = value
    
    def setPassword(self,value):
        self.password = value
