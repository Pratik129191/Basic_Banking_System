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
    """
    <tr>
        <td align="center"> Purnendu Sahoo </td>
        <td align="center"><img src="https://github.com/Pratik129191/HTML/blob/main/images/techer%20&%20friend/ps_sir1.jpg?raw=true" width="110"></td>
        <td align="center"><a href="https://www.facebook.com/purnendu.sahoo.79"> Facebook Profile </a></td>
    </tr>
    :param request:
    :return: models.Customer.objects.select_related('account').all()
    """
    customer = models.Customer.objects.select_related('account').all()
    context = {
        'queryset': customer,
        'user': reverse('core:customers')
    }
    return render(request, 'customers.html', context)


def customer_details(request, id):
    context = {
        'user': models.Customer.objects.select_related('account').get(pk=id),
        'transfer': reverse('core:transfer')
    }

    return render(request, 'details.html', context)


def transfer(request):
    return HttpResponse('Ok')


def transfer_details(request, id):
    form = TransactionForm(id)
    context = {
        'form': form
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


