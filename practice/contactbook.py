
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
                if numberss.isdigit():
                    return True
                else:
                    return False
            except(ValueError):
                return False

    @staticmethod
    def find(person):
        for contact in Contact.all_contact:
            if person == contact.name:
                Contact.display(contact)
                break
        else:
            return f"The name You have provided does not appear in your rubric"


luca = Contact("Luca", "+39 333 1234567")
luca.display()
anna = Contact.created_from_text("Anna;+44 7700 900123")
anna.display()
print(Contact.created_from_text("Marco;333 1234567"))
print(Contact.created_from_text("Giulia;+39 abc"))
print(Contact.created_from_text("Bob +39 333 1234567"))
print(Contact.check_number("+39 333 1234567"))
print(Contact.check_number("+39+333"))
Contact.find("Anna")
print(Contact.find("Nobody"))
print("Contacts saved:", len(Contact.all_contact))

