from datetime import datetime

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp or datetime.now()

    def set_user(self, user):
        self.user = user

    def __str__(self):
        return "{}: {} ({})".format(self.user.first_name, self.text, self.timestamp)


class TextPost(Post):
    def __init__(self, text, timestamp=None):
        super().__init__(text, timestamp)

    def __str__(self):
        return "TextPost: {}".format(super().__str__())


class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        super().__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return "PicturePost: {} (Image: {})".format(super().__str__(), self.image_url)


class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        super().__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return "CheckInPost: {} (Location: {}, {})".format(super().__str__(), self.latitude, self.longitude)

