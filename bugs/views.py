from bugs.models import Bug,BugType,BugPriority,BugStatus,BugHistory
from core.models import UserProfile,Role
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from bugs.forms import BugForm,UpdateForm,AssignForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def tickets(request):
    page_data=BugHistory.objects.filter(creator=request.user)
    return render(request, 'client/tickets.html', {'page_data':page_data})

@login_required(login_url='/login/')
def raise_ticket(request):
    if (request.method == "POST"):
        bug_form = BugForm(request.POST)
        if (bug_form.is_valid()):

            # Save form data to DB
            bug=Bug()
            bug_type_id=''+bug_form.cleaned_data['bug_type']
            bug.bug_type=BugType.objects.get(bug_type_id=bug_type_id)

            bug.bug_desc=bug_form.cleaned_data['bug_desc']
            
            bug_priority_id=''+bug_form.cleaned_data['bug_priority']
            bug.bug_priority=BugPriority.objects.get(bug_priority_id=bug_priority_id)

            user= UserProfile.objects.get(is_staff=True,is_admin=False)
            bug.bug_owner=user
        
            # Save encrypted password to DB
            bug.save()


            bugHistory=BugHistory()
            bugHistory.bug=bug
            bugHistory.creator=request.user

            bugHistory.save()
            # Success! Redirect to home page.
            return redirect("/")
        else:
            page_data = { "bug_form": bug_form }
            return render(request, 'client/raise-ticket.html', page_data)

    else:
        bug_form = BugForm()
        page_data = { "bug_form": bug_form }
        return render(request, 'client/raise-ticket.html',page_data)


@login_required(login_url='/login/')
def staff_tickets(request):
    page_data=Bug.objects.filter(bug_owner=request.user)
    return render(request, 'staff/staff-tickets.html', {'page_data':page_data})


@login_required(login_url='/login/')
def update_tickets(request,id):
    if request.method == "GET":
            bug = Bug.objects.get(bug_id=id)
            data = {"bug_type": bug.bug_type, "bug_desc": bug.bug_desc,
                "bug_priority": bug.bug_priority,"bug_status":bug.bug_status}
            update_form = UpdateForm(initial=data)
            page_data = {"update_form": update_form}
            return render(request, 'staff/update-tickets.html', page_data)
    if request.method == "POST":
            bug = Bug.objects.get(bug_id=id)
            update_form = UpdateForm(request.POST)
            if update_form.is_valid():
                updated_type = update_form.cleaned_data['bug_type']
                updated_desc = update_form.cleaned_data['bug_desc']
                updated_priority = update_form.cleaned_data['bug_priority']
                updated_status = update_form.cleaned_data['bug_status']
                Bug.objects.filter(bug_owner=request.user, bug_id=id).update(
                bug_type=updated_type, bug_desc=updated_desc, bug_priority=updated_priority, bug_status=updated_status)
                return redirect("/myTickets/")
            else:
                page_data = {"update_form": update_form}
                return render(request, 'staff/update-tickets.html', page_data)

@login_required(login_url='/login/')
def all_tickets(request):
    page_data=Bug.objects.all()
    return render(request, 'staff/all-tickets.html', {'page_data':page_data})


@login_required(login_url='/login/')
def assign_tickets(request,id):
    if request.method =="GET":
        bug=Bug.objects.get(bug_id=id)
        data={"bug_owner":bug.bug_owner}
        assign_form = AssignForm(initial=data)
        page_data = {"assign_form": assign_form}
        return render(request, 'staff/assign-tickets.html', page_data)
    if request.method == "POST":
        bug = Bug.objects.get(bug_id=id)
        assign_form = AssignForm(request.POST)
        if assign_form.is_valid():
            updated_owner = assign_form.cleaned_data['bug_owner']
            Bug.objects.filter(bug_id=id).update(
            bug_owner=updated_owner)
            return redirect("/allTickets/")
        else:
            page_data = {"assign_form": assign_form}
            return render(request, 'staff/assign-tickets.html', page_data)
    

        
                
