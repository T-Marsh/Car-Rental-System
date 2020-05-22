import re # regular expression

class Validation():

    def is_numeric(self, val):
        val = str(val) # only str have the isnumeric() method
        if val.isnumeric():
            print("Numeric")
            return True
        else:
            print("Not numeric")
            return False  

    def is_alphabetic(self, val):
        val = str(val)
        if val.isalpha():
            print("Alphabetic")
            return True
        else:
            print("Not alphabetic")
            return False  

    def is_alphanumeric(self, val):
        val = str(val)
        if val.isalnum():
            print("Alphanumeric")
            return True
        else:
            print("Not alphanumeric")
            return False  

    def is_phone_number(self, val):
        val = str(val)
        if re.search(r'(^\d{2} \d{4} \d{4})', val): # 02 9999 9999
            print("Valid phone number")
            return True
        else:
            print("Invalid phone number")
            return False

    # NOTE: WIP
    # def is_date(self, val):
    #     val = str(val)
    #     if re.search(r'(^\d{2} \d{2} \d{2}', val):
    #         print("Valid date")
    #         return True
    #     else:
    #         print("Invalid date")
    #         return False
        
    pass

if __name__ == '__main__':
    pass        