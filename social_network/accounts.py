class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name  
        self.last_name = last_name    
        self.email = email            
        self.posts = []               
        self.following = []          

    def add_post(self, post):
        post.set_user(self)  
        self.posts.append(post)  

    def get_timeline(self):
        return sorted(self.posts, key=lambda post: post.timestamp, reverse=True)

    def follow(self, other):
        if other not in self.following:
            self.following.append(other)  

    def __str__(self):
        return self.first_name + " " + self.last_name
