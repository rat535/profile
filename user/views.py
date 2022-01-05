from logging import info
from django.shortcuts import render
from django.contrib import auth
import pyrebase


# Create your views here.
config={
  "apiKey": "AIzaSyCIdmZvv-G7xqZMKDFMDcgcjn8u5y0ZAXQ",
  "authDomain": "profile-61e78.firebaseapp.com",
  "databaseURL":"https://profile-61e78-default-rtdb.firebaseio.com/",
  "projectId": "profile-61e78",
  "storageBucket": "profile-61e78.appspot.com",
  "messagingSenderId": "586163410924",
  "appId": "1:586163410924:web:1b04fbd35f3b202ffa12c9",

}
firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database=firebase.database()



def home(request):
    return render(request,'registration/home.html')
def login(request):
    return render(request,'registration/login.html')

def postsignIn(request):
    email = request.POST.get('email')
    pasw = request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
    except:
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,"registration/profile.html",{"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)


    return render(request,"registration/profile.html",{"email":email})

def signup(request):
    return render(request,'registration/signup.html')

def postsignUp(request):
     email = request.POST.get('email')
     passs = request.POST.get('pass')
     name = request.POST.get('username')
     try:
        # creating a user with the given email and password
        user=authe.create_user_with_email_and_password(email,passs)
        uid = user['localId']
        data={'name':name,'status':'1'}
        database.child("users").child(uid).child("details").set(data)

     except:
        return render(request, "registration/login.html")
     return render(request,"registration/Login.html")

def profile(request):
    return render(request,'registration/profile.html')

def logout(request):
    auth.logout(request)
    return render(request,'registration/home.html')


def reset(request):
    return render(request,'registration/reset.html')

def postReset(request):
    email = request.POST.get('email')
    try:
        authe.send_password_reset_email(email)
        message  = "A email to reset password is successfully sent"
        return render(request, "registration/reset.html", {"message":message})
    except:
        message  = "Something went wrong, Please check the email you provided is registered or not"
        return render(request, "registration/reset.html", {"message":message})

def create(request):
    name=request.POST.get('username')
    address=request.POST.get('address')
    
    idtoken=request.session['uid'] 
    a=authe.get_account_info(idtoken)
    a=a['users']
    a=a[0]
    a=a['localId']
    print(a)

    data={
        'name':name,
        'address':address 
    }
    try:
        database.child("users").child(a).child("details").child("info").set(data)
        name=database.child("users").child(a).child("details").child('name').get().val()
    except:
        return render(request,'registration/profile.html',{'name':name})
    return render(request,'registration/profile.html',{'name':name})