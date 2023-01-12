import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from fastapi import FastAPI, Depends, HTTPException
from pyasn1.type.univ import Null
from pyrebase import pyrebase
from firebase_admin import db

from auth import AuthHandler
from schemas import AuthDetails, Access, NewUser, User
import flask

firebaseConfig = {'apiKey': "AIzaSyDICkdJ1RMuG-CGyNM6xAtLWaQmk6Lnr88",
                  'authDomain': "bff-a2663.firebaseapp.com",
                  'databaseURL': "https://bff-a2663-default-rtdb.firebaseio.com",
                  'projectId': "bff-a2663",
                  'storageBucket': "bff-a2663.appspot.com",
                  'messagingSenderId': "126648597174",
                  'appId': "1:126648597174:web:392b07d4ddfea5cda64417",
                  'measurementId': "G-CSP5T08Y6M"}

firebase = pyrebase.initialize_app(firebaseConfig)
auth1 = firebase.auth()

app = FastAPI()
auth_handler = AuthHandler()
users = []

cred = credentials.Certificate("bff-a2663-firebase-adminsdk-3eq11-c1610635f2.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bff-a2663-default-rtdb.firebaseio.com/'
})


def loginToFire(email: str, password: str):
    print("Log in...")
    try:
        auth1.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
        user = auth.get_user_by_email(email)
        print(user.uid)
        return user.uid
    except:
        print("Invalid email or password")
        return "error"
    return


@app.post('/login')
def login(auth_details: AuthDetails):
    user_id = loginToFire(auth_details.email, auth_details.password)
    if user_id == "error":
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    return {'user_id': user_id}


@app.post('/AccessLevel')
def AccessLevel(access: Access):
    if db.reference(access.type).child(access.uid).get() is not None:
        return "true"
    else:
        return "false"


# @app.post('/RegisterUser')
# def create_user(new_user: NewUser):
#     auth.create_user(email=new_user.email, password=new_user.password)
#     userID = auth.get_user_by_email(new_user.email).uid
#     db.reference("Users").child(userID).set({'name': new_user.name,
#                                              'email': new_user.email,
#                                              'type': new_user.type,
#                                              'id': userID,
#                                              'breed': new_user.breed,
#                                              'color': new_user.color,
#                                              'flag': new_user.flag,
#                                              'image': None,
#                                              'phone': new_user.phone,
#                                              'username': new_user.username})
#     return "true"






