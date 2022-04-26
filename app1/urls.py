"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from tasks import views as tasks_views
from budget import views as budget_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home),
    path('about/', core_views.about),
    path('join/', core_views.join),
    path('login/', core_views.user_login),
    path('logout/', core_views.user_logout),
    path('tasks/', tasks_views.home),
    path('tasks/create', tasks_views.create),
    path('tasks/edit/<int:id>/', tasks_views.update),
    path('tasks/complete/<int:id>/', tasks_views.complete),
    path('tasks/delete/<int:id>', tasks_views.delete),
    path('budgets/', budget_views.home),
    path('budgets/create', budget_views.create),
    path('budgets/edit/<int:id>/', budget_views.update),
    path('budgets/delete/<int:id>', budget_views.delete),
]
