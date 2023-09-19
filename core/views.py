from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from . import models
from .forms import TransactionForm


def home(request):
    context = {
        'customers': reverse('core:customers')
    }
    return render(request, 'home.html', context)


def view_all_customers(request):
    customer = models.Customer.objects.select_related('account').all()
    context = {
        'queryset': customer,
        'user': reverse('core:customers'),
        'home': reverse('core:home')
    }
    return render(request, 'customers.html', context)


def customer_details(request, id):
    context = {
        'user': models.Customer.objects.select_related('account').get(pk=id),
        'transfer': reverse('core:transfer'),
        'customers': reverse('core:customers')
    }

    return render(request, 'details.html', context)


def transfer(request):
    return HttpResponse('Ok')


def transfer_details(request, id):
    form = TransactionForm(id)
    context = {
        'form': form,
        'details': (
            reverse('core:customers')
            + id
        ),
        'home': reverse('core:home')
    }

    if request.method == 'POST':
        form = TransactionForm(id, request.POST)
        if form.is_valid():
            form.save()
            form.update()
            return redirect('core:customers')
        else:
            return HttpResponse("OOPs")
    return render(request, 'transfer.html', context)


