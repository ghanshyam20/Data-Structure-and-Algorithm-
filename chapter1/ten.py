class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print("Name:", self.first_name, self.last_name)
        print("Username:", self.username)
        print("Email:", self.email)
        print("Location:", self.location)

    def greet_user(self):
        print("Hello", self.username, "welcome back!")


# i have try to do all this code as in my way it might not run on moodle in some cases but 
# most importatn thing is i am doing this for practice not to make it perfect 

# this code creates user class to store basic user detaisls
# like name, username and so on and it includes two methods one todisplay 
#user info and anotehr to greet user 
