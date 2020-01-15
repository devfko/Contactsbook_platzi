from contact import Contact
import csv

class ContactBook():

    def __init__(self):
        self._contacts = []
        self._OneContact = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def getContact(self, name):        
        # self._fill()        

        with open('contacts.csv', newline='') as f:
            reader = csv.DictReader(f)

            # for idx, row in enumerate(reader):
            for row in reader:
                if row['name'].lower() == name.lower():                    
                    contactFill = Contact(str(row['name']), str(row['phone']), str(row['email']))
                    # return row['email'].lower() + ' ' + name.lower()                    
                    self._OneContact.append(contactFill)
            else:
                return('No found items')
    
    def _save(self):
        with open('contacts.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )

    def delete(self, email):
        for idx, contact in enumerate(self._contacts):
            if contact.email.lower() == email.lower():
                del self._contacts[idx]
                self._save()
                break
