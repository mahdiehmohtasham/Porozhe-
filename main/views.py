from django.shortcuts import render
from django.views import View
from main.models import Transaction


class MainView(View):
    def get(self, request):
        print(Transaction.objects.all())
        return render(request, "index.html")
    

class TransactionView(View):
    def get(self, request):
        print(Transaction.objects.all())
        return render(request, "index1.html")

class IncomesView(View):
    def get(self, request):
        print(Transaction.objects.all())
        return render(request, "index2.html")

class ExpensesView(View):
    def get(self, request):
        print(Transaction.objects.all())
        return render(request, "index3.html")