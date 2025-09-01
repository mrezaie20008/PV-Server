from configs import *
from mega import Mega
from exceptions import (
    UnauthorizedAccess as ua
)
from cryptography.fernet import Fernet
from os import remove



class Storage:
    def __init__(self, email: str, password: str):
        # Instances
        self.cloud = Mega() 
        self.logger = None
        self.locker = Fernet(b"TW9oYW1tYWQ6UmV6YWllOjIwMDg6TW9oYW1tYWRAOTk=")

        # Credentials
        self.email = email
        self.password = password
        self.logged_in = False

    # Helping Methods
    def verify(self):
        if self.logged_in:
            return 

        else:
            raise ua("You must login first then perform something!")


    # The main methods
    def upload(self, file: str | Path):
        self.verify()

        if not Path(file).exists():
            raise FileNotFoundError(f"{file.__str__()} not found!")

        try:
            data = open(file, "rb").read()

            with open(HOME_DIR / ".temp.temp", "wb") as encfile:
                encfile.write(self.locker.encrypt(data))
            
            self.cloud.upload(".temp.temp", dest_filename=Path(file).name)

            remove(".temp.temp")


        except Exception as e:
            print(e)


    def download(self, filename: str, output: str = ""):
        self.verify()
        __file = self.cloud.find(filename)


        if not __file:
            raise FileNotFoundError("File Not Found!")

        __output = output if output else "Default.bin"

        self.cloud.download(__file, dest_filename=".temp.dtemp")
        edata = open(".temp.dtemp", "rb").read()

        try:
            __dd = self.locker.decrypt(edata)

            with open(output, "wb") as dfile:
                dfile.write(__dd)

        except Exception as e:
            print(e)


    def get_files(self):
        self.verify()

        return self.cloud.get_files()


    def whoami(self):
        self.verify()

        return self.cloud.get_user()


    def login(self):
        try:
            self.cloud.login(self.email, self.password)
            self.logged_in = True

            #self.logger.info("You logged in successfully!")

        except Exception as e:
            print("SOMETHING WENT WRONG!")
            exit()


cl = Storage("working_etc@outlook.com", "Mohammad@99")
cl.login()

cl.download("db.py", "tdb.py")
