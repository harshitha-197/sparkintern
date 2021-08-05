from django.db.models.fields import NullBooleanField
from Bank.models import customerdata, transfer
from django.shortcuts import render
from .forms import transaction, customerdataform, checkdetailForm
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    return render(request, 'home.html')


def home1(request):
    return render(request, 'home1.html')

def cust_data(request):
    if request.method == "POST":
        form = checkdetailForm(request.POST)
        if form.is_valid():
            acc_no = request.POST.get('account_num')
            print(acc_no)
            user_count = customerdata.objects.filter(account_number=acc_no).count()
            if (user_count == 0):
                message = "No users found"
                form = checkdetailForm()
                return render(request, 'customerdata.html', {'form': form, 'message': message, 'bool': "hidden"})
            else:
                Users = customerdata.objects.get(account_number=acc_no)
                form = checkdetailForm()
                return render(request, 'customerdata.html', {'form': form, 'user': Users})
        else:
            form = checkdetailForm()

    form = checkdetailForm()

    return render(request, 'customerdata.html', {'form': form, 'bool': "hidden"})


def customer_details(request):
    Users = customerdata.objects.all()
    return render(request, 'customer_details.html', {'Users': Users})


def transactions(request):
    transactions = transfer.objects.all()
    return render(request, 'transactions.html', {'transactions': transactions})


def sendmoney(request):
    if request.method == "POST":
        form = transaction(request.POST)
        if form.is_valid():
            toacc = request.POST.get('toaccount')
            fromacc = request.POST.get('fromaccount')
            amnt = request.POST.get('amount')
            print(amnt)
            Sender_verify = customerdata.objects.filter(account_number=fromacc).count()
            Receiver_verify = customerdata.objects.filter(account_number=toacc).count()
            if Sender_verify == 0 or Receiver_verify == 0:
                message = "Transaction Failed"
                return render(request, 'sendmoney.html', {'form': form, 'message': message, 'signal': "danger"})
            else:
                Sender = customerdata.objects.get(account_number=fromacc)
                Receiver = customerdata.objects.get(account_number=toacc)
                if Sender.balance < int(amnt):
                    message = "Insufficient Funds"
                    return render(request, 'sendmoney.html', {'form': form, 'message': message, 'signal': "danger"})
                Sender.balance = Sender.balance - int(amnt)
                Sender.save()
                Receiver.balance = Receiver.balance + int(amnt)
                Receiver.save()
                message = "Transaction Success"
                form.save()
                form = transaction()
                return render(request, 'sendmoney.html', {'form': form, 'message': message, 'signal': "success"})
        else:
            message = "Transaction Failed"
            form = transaction()
            return render(request, 'sendmoney.html', {'form': form, 'message': message, 'signal': "danger"})
    form = transaction()
    return render(request, 'sendmoney.html', {'form': form, 'hiddensignal': "hidden"})


def insertdata(request):
    if request.method == "POST":
        form = customerdataform(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = customerdataform()

    form = customerdataform()
    return render(request, 'addcustomerdata.html', {'form': form})

