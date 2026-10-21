
class Contact:
    all_contact = []

    def __init__(self,name , phone_number) -> None:
        self.name = name
        self.phone_number = phone_number
        Contact.all_contact.append(self)

    def display(self):
        print(f"{self.name}  , {self.phone_number} ")

    @classmethod
    def created_from_text(cls, text):
        try:
            name , number = text.split(";")
            if not cls.check_number(number):
                return f"Invalid Phone Number"
            else:
                x = cls(name, number)
                print(f"{x.name} Successfully added to teh contact Rubric")
                return x
        except(ValueError):
            return f"Your text does not contain follow the correct format"

    @staticmethod
    def check_number(number):
        if not number.startswith("+"):
            return False
        else:
            try:
                sign , numbers = number.split("+")
                numberss = numbers.replace(" ", "")
                if not isinstance(numberss,int):
                    return False
                else:
                    return True
            except(ValueError):
                return False

    @staticmethod
    def find(person):
        for contact in Contact.all_contact:
            if person == contact.name:
                Contact.display(contact)
        else:
            return f"The name You have provided does not appear in your rubric"

