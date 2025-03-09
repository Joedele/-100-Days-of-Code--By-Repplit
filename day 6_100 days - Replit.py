print()
print("\033[38;5;214m","Welcome to Day 6","\033[0m")

print("\033[93m"," >",'\033[0m',"For today's project I made a simple login system using the","\033[32m","if, else, and elif conditionals",'\033[0m')
print("\033[93m"," >",'\033[0m',"I also created some user accounts with usernames, so there's a slight chance that your name might be registered already.","\033[32m","If not,",'\033[0m'," don't worry, just sign up, and read the custom message made just for you","\033[0m")

print()

#Don't mind this large code. It's just there to aid in the sign in process.
def login():

    username = input("\033[35mEnter your username > \033[0m").lower()
    password = input("\033[35mEnter your password > \033[0m").lower()


    if username == "joedele" and password == "jtf":
        print("\033[93m"," >",'\033[0m',"👋 Welcome back Joe, how's been business?")
        print("We got some special deals just for you 😉") 
#Concerning this particular username, it's locked just for me. I don't know how else to block it, so i gave it a different password.

    elif username == "agnes" and password == "password":
        print("\033[93m"," >",'\033[0m',"😲 Oh my! Is it really you Agnes? it's been quite some time. How've you been?")

    elif username == "brian" and password == "password":
        print("\033[93m"," >",'\033[0m',"😲 Brian, what's up my dude?  We've got some exiting deals for you, you don't want to miss them.😉")

    elif username == "kelly" and password == "password":
        print("\033[93m"," >",'\033[0m',"Kelly. What a beautiful name! You remind me of my Lil. Sis. Hope you'll be shopping none stop? Just kidding, but seriously, if you can, don't hesitate to.")
        print("And to help you out we've made some custom coupons just for you. Happy Shopping!")

#This one's for the registeration/signup
def signUp():
    print("\033[35m")

    new_username = input("\033[35mEnter a username: \033[0m").lower()
    new_password = input("\033[35mEnter a password: \033[0m").lower()
    print()
    print("\033[0mWelcome",new_username,"we're glad to have you here. If you've got any enquiries or issues, just give us a call🤙")

#The start of the real code.
print("\033[38;5;214m"," MY LOGIN SYSTEM","\033[0m")

print()
print("Account Checker:","\033[35m")
nameCheck = input("Please enter your first name: \033[0m").lower()

if nameCheck == "joedele" or nameCheck == "agnes" or nameCheck == "brian" or nameCheck == "kelly":
    print("\033[93m"," >",'\033[0m',"The name's on the list. Use the name, and your default password 'Password', to sign in")
    login()

else:
    print("There's no account under such name, sign up now.")
    signUp()
print()








