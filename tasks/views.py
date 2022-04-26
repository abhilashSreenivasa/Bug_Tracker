from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from tasks.forms import CreateForm, UpdateForm
from tasks.models import Task, TaskCategory
# Create your views here.


def add_task(request):
    page_data = {"task_form": CreateForm}
    return render(request, 'tasks/add-task.html', page_data)


def get_tasks(request):
    tasks = Task.objects.filter(user=request.user)
    output = []
    for task in tasks.iterator():
        output.append({"name": task.name, "category": task.category.category,
                      "is_completed": "Yes" if task.is_completed else "No", "id": task.id})

    return output


@login_required(login_url='/login/')
def create(request):
    if request.method == "GET":
        return add_task(request)
    if request.method == "POST":
        task_form = CreateForm(request.POST)
        if(task_form.is_valid()):
            category = task_form.cleaned_data['category']
            name = task_form.cleaned_data['name']
            Task(user=request.user, category=category, name=name).save()
            return redirect("/tasks/")
        else:
            page_data = {"task_form": task_form}
            return render(request, 'tasks/add-task.html', page_data)


@login_required(login_url='/login/')
def home(request):
    if request.method == "GET":
        tasks = get_tasks(request)
        page_data = {}
        if len(tasks) > 0:
            return render(request, "tasks/home.html", {"tasks": tasks})
        else:
            return render(request, "tasks/home.html", {})


@login_required(login_url='/login/')
def update(request, id):
    if request.method == "GET":
        task = Task.objects.get(id=id)
        data = {"name": task.name, "category": task.category}
        task_form = UpdateForm(initial=data)
        page_data = {"task_form": task_form}
        return render(request, 'tasks/update-task.html', page_data)
    if request.method == "POST":
        task = Task.objects.get(id=id)
        task_form = UpdateForm(request.POST)
        if task_form.is_valid():
            updated_name = task_form.cleaned_data['name']
            updated_category = task_form.cleaned_data['category']
            Task.objects.filter(user=request.user, id=id).update(
                name=updated_name, category=updated_category)
            return redirect("/tasks/")
        else:
            page_data = {"task_form": task_form}
            return render(request, 'tasks/update-task.html', page_data)


@login_required(login_url='/login/')
def complete(request, id):
    if request.method == "POST":
        return render(request, "tasks/home.html", {"tasks": get_tasks()})
    if request.method == "GET":
        task = Task.objects.get(id=id)
        Task.objects.filter(user=request.user, id=id).update(
            is_completed=not task.is_completed)
        return redirect("/tasks/")


@login_required(login_url='/login/')
def delete(request, id):
    if request.method == "POST":
        Task.objects.filter(user=request.user, id=id).delete()
    return redirect("/tasks/")
