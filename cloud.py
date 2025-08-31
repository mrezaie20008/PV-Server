from configs import *
from mega import Mega


class Storage:
    def __init__(self, email: str, password: str):
        # Instances
        self.cloud = Mega() 
        self.logger = None

        # Credentials
        self.email = email
        self.password = password
        self.logged_in = False


    # The main methods
    def upload(self):
        pass


    def download(self):
        pass


    # Helping Methods
    def get_files(self):
        pass

    def verify(self):
        if self.logged_in:
            return 1


    def whoami(self):
        if self.verify():
            return self.cloud.get_user()


    def login(self):
        try:
            self.cloud.login(self.email, self.password)
            self.logged_in = True

            #self.logger.info("You logged in successfully!")

        except Exception as e:
            print("SOMETHING WENT WRONG!")


cl = Storage("working_etc@outlook.com", "Mohammad@99")
cl.login()

print(cl.whoami())


