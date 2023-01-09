import pyrebase

firebaseConfig = {'apiKey': "AIzaSyDICkdJ1RMuG-CGyNM6xAtLWaQmk6Lnr88",
                  'authDomain': "bff-a2663.firebaseapp.com",
                  'databaseURL': "https://bff-a2663-default-rtdb.firebaseio.com",
                  'projectId': "bff-a2663",
                  'storageBucket': "bff-a2663.appspot.com",
                  'messagingSenderId': "126648597174",
                  'appId': "1:126648597174:web:93e685132ca63489a64417",
                  'measurementId': "G-94RBWB55RW"}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


def login():
    print("Log in...")
    email = input("Enter email: ")
    password = input("Enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
        # print(auth.get_account_info(login['idToken']))
    # email = auth.get_account_info(login['idToken'])['users'][0]['email']
    # print(email)
    except:
        print("Invalid email or password")
    return


def signup():
    print("Sign up...")
    email = input("Enter email: ")
    password = input("Enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        ask = input("Do you want to login?[y/n]")
        if ask == 'y':
            login()
    except:
        print("Email already exists")
    return


signup()
