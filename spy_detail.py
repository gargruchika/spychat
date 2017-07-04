from datetime import datetime

class spy1:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

class chatmessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = spy1('ruchika', 'Ms.', 19, 4)

friend_one = spy1('Rsahmi', 'Ms.', 19,4.9)
friend_two = spy1('Munisha', 'Ms.',19, 4.39)
friend_three = spy1('sunidhi', 'Ms.',20, 4.95)


friends = [friend_one, friend_two, friend_three]
