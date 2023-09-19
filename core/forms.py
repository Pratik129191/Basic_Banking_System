from django import forms
from .models import Transaction, Customer, Account


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['receiver', 'amount', 'description']

    def __init__(self, user_id, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.payee = Customer.objects.get(id=user_id)
        self.fields['receiver'].queryset = Customer.objects.exclude(id=user_id)

    def save(self, commit=True):
        self.instance = Transaction.objects.create(
            payee=self.payee,
            receiver=self.cleaned_data['receiver'],
            amount=self.cleaned_data['amount'],
            description=self.cleaned_data['description']
        )
        return self.instance

    def update(self):
        payee = Account.objects.get(customer=self.payee)
        receiver = Account.objects.get(customer=self.instance.receiver)

        payee.balance -= self.instance.amount
        payee.save()

        receiver.balance += self.instance.amount
        receiver.save()









