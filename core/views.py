from core.models import UserProfile,Role
from bugs.models import Bug,BugHistory,BugPriority,BugStatus,BugType
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from core.forms import  JoinForm, LoginForm

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    user = UserProfile.objects.get(id=request.user.id)
    if((user.role.role_id is '2') or (user.role.role_id is '3') ):
        userBugs=[]
        data=[]
        listOfBugs=[]
        userBugs=Bug.objects.filter(bug_owner=request.user)

        for b in userBugs:
            print(b)
            listOfBugs.append(b)
       

        new=[x for x in listOfBugs if x.bug_status.bug_status_id == '1'] 
        open=[x for x in listOfBugs if x.bug_status.bug_status_id  == '2']
        inProgress=[x for x in listOfBugs if x.bug_status.bug_status_id  == '3']
        closed=[x for x in listOfBugs if x.bug_status.bug_status_id  == '4']
        cancelled=[x for x in listOfBugs if x.bug_status.bug_status_id  == '5']
        
        

        #--------------------------------
        allBugs=[]
        listOfBugsAll=[]
        allBugs=Bug.objects.filter()
        for b in allBugs:
            listOfBugsAll.append(b)
        
        newAll=[x for x in listOfBugsAll if x.bug_status.bug_status_id == '1'] 
        openAll=[x for x in listOfBugsAll if x.bug_status.bug_status_id  == '2']
        inProgressAll=[x for x in listOfBugsAll if x.bug_status.bug_status_id  == '3']
        closedAll=[x for x in listOfBugsAll if x.bug_status.bug_status_id  == '4']
        cancelledAll=[x for x in listOfBugsAll if x.bug_status.bug_status_id  == '5']

        currentData=[]
        historyData=[]
        if user.role.role_id is '3':
            currentData=[len(new),len(open),len(inProgress)]
            historyData=[len(closed),len(cancelled)]
            data=currentData+historyData
        else:
            currentData=[len(newAll),len(openAll),len(inProgressAll)]
            historyData=[len(closedAll),len(cancelledAll)]
            data=currentData+historyData
        return render(request,"staff/staff-home.html",
        {
        'data':data, 
        'historyData':historyData,
        'currentData':currentData
        })

    else:
        userBugs=[]
        data=[]
        listOfBugs=[]
        userBugs=BugHistory.objects.filter(creator=request.user)

        for b in userBugs:
            listOfBugs.append(b.bug)
       

        new=[x for x in listOfBugs if x.bug_status.bug_status_id == '1'] 
        open=[x for x in listOfBugs if x.bug_status.bug_status_id  == '2']
        inProgress=[x for x in listOfBugs if x.bug_status.bug_status_id  == '3']
        closed=[x for x in listOfBugs if x.bug_status.bug_status_id  == '4']
        cancelled=[x for x in listOfBugs if x.bug_status.bug_status_id  == '5']
        
        currentData=[len(new),len(open),len(inProgress)]
        historyData=[len(closed),len(cancelled)]

        data=currentData+historyData
        return render(request,"client/client-home.html",
        {'data':data, 
        'historyData':historyData,
         'currentData':currentData
        })

def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):

            # Save form data to DB
            user=UserProfile()
            user.username=join_form.cleaned_data['username']
            user.email=join_form.cleaned_data['email']
            user.set_password(join_form.cleaned_data['password'])
            role_id=''+join_form.cleaned_data['role']
            user.role=Role.objects.get(role_id=role_id)
            
            # Save encrypted password to DB
            user.save()
            # Success! Redirect to home page.
            return redirect("/login")
        else:
            page_data = { "join_form": join_form }
            return render(request, 'auth/join.html', page_data)

    else:
        join_form = JoinForm()
        page_data = { "join_form": join_form }
        return render(request, 'auth/join.html',page_data)

def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # First get the username and password supplied
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)
            # If we have a user
            if user:
                #Check it the account is active
                if user.is_active:
                    # Log the user in.
                    login(request,user)
                    # Send the user back to homepage
                    return redirect("/")
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return render(request, 'auth/login.html', {"login_form": LoginForm})
    else:
        #Nothing has been provided for username or password.
        return render(request, 'auth/login.html', {"login_form": LoginForm})

@login_required(login_url='/login/')
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect("/")