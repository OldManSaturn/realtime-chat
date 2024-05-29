class Message:
    def __init__(self, user, content, timestamp):
        self.user = user
        self.content = content
        self.timestamp = timestamp

class User:
    def __init__(self, username):
        self.username = username
