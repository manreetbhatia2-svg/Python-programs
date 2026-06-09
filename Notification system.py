from abc import ABC, abstractmethod
class Notification(ABC):
    def send(self,message):
        pass

class EmailNotification(Notification):
    def send(self,message):
        print("You are sending message through email")

class SMSNotification(Notification):
    def send(self,message):
        print("You are sending message through SMS")

class PushNotification(Notification):
    def send(self,message):
        print("You are pushing the notification")

messages = [EmailNotification(),
            SMSNotification(),
            PushNotification()]
for i in messages:
    i.send("server is down")