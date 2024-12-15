import json

class UserDatabase(dict):
    def __init__(self):
        super().__init__()
        
        self.load_file()
    
    def load_file(self):
        with open("src/contents.json", "r+", encoding="utf-8") as f:
            self.users: dict = json.load(f)

    def add(self, user):
        if (user not in list(self.users.keys())):
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
                if self.users["Users"][uname]["password"] == pw:
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

def ordinalize(number: str):
    try:
        assert number.isnumeric()

        num = int(number)
        match num:
            case 1:
                return "1st"
            case 2:
                return "2nd"
            case 3:
                return "3rd"
            case _:
                return f"{num}th"

    except AssertionError:
        return None