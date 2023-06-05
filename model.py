

class User:
    
    def __init__(self,signum,name, email):
        self.signum = signum
        self.name = name
        self.email = email
        
    def to_dict(self):
        return {
            'signum': self.signum,
            'name': self.name,
            'email': self.email,
        } 