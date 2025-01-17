"""
URL configuration for settings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from main.views import MainView,TransactionView,IncomesView,ExpensesView
from api.views import AccountAPIView, CategoryAPIView, TransactionAPIView,ExpenseAPIView,IncomeAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('transaction-table/', TransactionView.as_view()),
    path('Incomes/', IncomesView.as_view()),
    path('Expenses/', ExpensesView.as_view()),
    path('api/accounts/', AccountAPIView.as_view()),
    path('api/categories/', CategoryAPIView.as_view()),
    path('api/transactions/', TransactionAPIView.as_view()),
    path('api/incomes/', IncomeAPIView.as_view(), name="income-list"),
    path('api/Expenses/', ExpenseAPIView.as_view(), name="expense-list"),
]
