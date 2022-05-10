from bugs.models import Bug,BugType,BugPriority,BugStatus,BugHistory
from core.models import UserProfile,Role
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from bugs.forms import BugForm

# Create your views here.


def tickets(request):
    page_data=BugHistory.objects.filter(creator=request.user)
    print(page_data)
    return render(request, 'client/tickets.html', {'page_data':page_data})


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