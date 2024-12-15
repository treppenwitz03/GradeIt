import json

class UserDatabase(dict):
    def __init__(self):
        super().__init__()
        
        self.load_file()

    def hash_password(self, password: str):
        hash_value = 0
    
        # Iterate over each character in the password
        for char in password:
            # Use the ASCII value of the character and perform a combination of operations
            hash_value = (hash_value * 31 + ord(char)) & 0xFFFFFFFFFFFFFFFF  # Keep it 64-bit
        
        # Convert the hash to a hexadecimal string (64 characters wide)
        hash_hex = hex(hash_value)[2:].zfill(64)  # Ensure it's exactly 64 characters
        
        return hash_hex
    
    def load_file(self):
        with open("src/contents.json", "r+", encoding="utf-8") as f:
            self.users: dict = json.load(f)

    def add(self, user, username):
        if (user not in list(self.users.keys())):
            password = user[username]["password"]
            user[username]["password"] = self.hash_password(password)
            self.users["Users"].update(user)
        else:
            return False

        with open("src/contents.json", "r+", encoding="utf-8") as f:
            json.dump(self.users, f, indent=4)
        
        self.load_file()

        return True
    
    def existing(self, uname, pw):
        for user in list(self.users["Users"].keys()):
            if uname == user:
                if self.users["Users"][uname]["password"] == self.hash_password(pw):
                    return True
                else:
                    return "PW wrong"
        
        return False

    def get_groups_for_user(self, name):
        classes = list()
        if len(list(self.users["Classes"].keys())) == 0:
            return False
        
        for klass in list(self.users["Classes"].keys()):
            if name in list(self.users["Classes"][klass].keys()):
                classes.append({klass : self.users["Classes"][klass]})
        
        return classes

    def create_group_for_user(self, name, group):
        try:
            if group in self.users["Classes"].keys():
                self.users["Classes"][group][name] = {}
            else:
                self.users["Classes"][group] = {
                    name : {
                        # Grades
                    }
                }

            with open("src/contents.json", "r+", encoding="utf-8") as f:
                json.dump(self.users, f, indent=4)
            
            self.load_file()
        except:
            return False

        return True

    def add_grades(self, name, group, dsa, hdl, rm, ms, fb, logic, fili, cisco):
        try:
            self.users["Classes"][group][name] = {
                "DSA": dsa,
                "HDL": hdl,
                "RM": rm,
                "Mixed Signals": ms,
                "Feedback": fb,
                "Logic": logic,
                "FILI": fili,
                "CISCO": cisco
            }

            with open("src/contents.json", "r+", encoding="utf-8") as f:
                json.dump(self.users, f, indent=4)
            
            self.load_file()
        except:
            return False

        return True

def ordinalize(number: int):
    try:
        match number:
            case 1:
                return "1st"
            case 2:
                return "2nd"
            case 3:
                return "3rd"
            case _:
                return f"{number}th"

    except AssertionError:
        return None