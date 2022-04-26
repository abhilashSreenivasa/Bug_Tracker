from django.shortcuts import render, redirect
from budget.models import Budget
from django.contrib.auth.decorators import login_required
from budget.forms import CreateForm, UpdateForm


# Create your views here.

def add_budget(request):
    page_data = {"budget_form": CreateForm}
    return render(request, 'budget/add-budget.html', page_data)

def get_budgets(request):
    budgets = Budget.objects.filter(user=request.user)
    output = []
    for budget in budgets.iterator():
        output.append({"description": budget.description, "category": budget.category.category,
                       "actual": budget.actual, "projected": budget.projected,
                       "id": budget.id})

    return output


@login_required(login_url='/login/')
def create(request):
    if request.method == "GET":
        return add_budget(request)
    if request.method == "POST":
        budget_form = CreateForm(request.POST)
        if(budget_form.is_valid()):
            category = budget_form.cleaned_data['category']
            description = budget_form.cleaned_data['description']
            actual = budget_form.cleaned_data['actual']
            projected = budget_form.cleaned_data['projected']
            Budget(user=request.user, category=category,
                   description=description, actual=actual, projected=projected).save()
            return redirect("/budgets/")
        else:
            page_data = {"budget_form": budget_form}
            return render(request, 'budget/add-budget.html', page_data)


@login_required(login_url='/login/')
def home(request):
    if request.method == "GET":
        budgets = get_budgets(request)
        page_data = {}
        if len(budgets) > 0:
            return render(request, "budget/home.html", {"budgets": budgets})
        else:
            return render(request, "budget/home.html", {})


@login_required(login_url='/login/')
def update(request, id):
    if request.method == "GET":
        budget = Budget.objects.get(id=id)
        data = {"description": budget.description, "category": budget.category,
                "actual": budget.actual, "projected": budget.projected}
        budget_form = UpdateForm(initial=data)
        page_data = {"budget_form": budget_form}
        return render(request, 'budget/update-budget.html', page_data)
    if request.method == "POST":
        budget = Budget.objects.get(id=id)
        budget_form = UpdateForm(request.POST)
        if budget_form.is_valid():
            updated_description = budget_form.cleaned_data['description']
            updated_category = budget_form.cleaned_data['category']
            actual = budget_form.cleaned_data['actual']
            projected = budget_form.cleaned_data['projected']
            Budget.objects.filter(user=request.user, id=id).update(
                description=updated_description, category=updated_category, actual=actual, projected=projected)
            return redirect("/budgets/")
        else:
            page_data = {"budget_form": budget_form}
            return render(request, 'budget/update-budget.html', page_data)


@login_required(login_url='/login/')
def delete(request, id):
    if request.method == "POST":
        Budget.objects.filter(user=request.user, id=id).delete()
    return redirect("/budgets/")
