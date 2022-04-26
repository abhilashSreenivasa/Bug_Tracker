from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.forms import JoinForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from tasks.models import Task, TaskCategory
from budget.models import Budget, BudgetCategory

def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            user = join_form.save()
            user.set_password(user.password)
            user.save()
            return redirect("/")
        else:
            page_data = {"join_form": join_form}
            return render(request, 'core/join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = {"join_form": join_form}
        return render(request, 'core/join.html', page_data)


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
                # Check it the account is active
                if user.is_active:
                    # Log the user in.
                    login(request, user)
                    # Send the user back to homepage
                    return redirect("/")
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(
                    username, password))
                return render(request, 'core/login.html', {"login_form": LoginForm})
    else:
        # Nothing has been provided for username or password.
        return render(request, 'core/login.html', {"login_form": LoginForm})


@login_required(login_url='/login/')
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect("/")


@login_required(login_url='/login/')
def home(request):
    taskCatCount = TaskCategory.objects.count()
    budgetCatCount = BudgetCategory.objects.count()
    if taskCatCount == 0:
        TaskCategory(category="Home").save()
        TaskCategory(category="School").save()
        TaskCategory(category="Work").save()
        TaskCategory(category="Self Improvement").save()
        TaskCategory(category="Other").save()
    if budgetCatCount == 0:
        BudgetCategory(category="Food").save()
        BudgetCategory(category="Clothing").save()
        BudgetCategory(category="Housing").save()
        BudgetCategory(category="Education").save()
        BudgetCategory(category="Entertainment").save()
        BudgetCategory(category="Other").save()
    all_tasks = Task.objects.filter(user=request.user)
    incomplete = 0
    complete = 0
    dataExists = Task.objects.count() > 0 or Budget.objects.count() > 0
    for task in all_tasks.iterator():
        if task.is_completed:
            complete = complete + 1
        else:
            incomplete = incomplete + 1

    all_budgets = Budget.objects.filter(user=request.user)
    projected = []
    actual = []
    labels = []
    for budget in all_budgets.iterator():
        projected.append(budget.projected)
        actual.append(budget.actual)
        labels.append(budget.description)
    page_data = {"task_summary": [incomplete, complete],
                 "budget_actual": actual, "budget_projected": projected, "budget_labels": labels,
                 }
    if dataExists:
        page_data['table_data'] = True
    print(page_data)
    return render(request, 'core/home.html', page_data)


def about(request):
    return render(request, 'core/about.html')
