from vaultkeeper.models import Customer, Card, Transaction, CentralAccount
from vaultkeeper.serializers import CardSerializer, CustomerSerializer, TransactionSerializer, CentralAccountSerializer
from rest_framework import generics
from django.http import JsonResponse, HttpResponse
from django.core.context_processors import csrf
from django.http import JsonResponse, HttpResponse
from datetime import datetime

class CustomerList(generics.ListAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class CardList(generics.ListAPIView):
	queryset = Card.objects.all()
	serializer_class = CardSerializer

class CardDetail(generics.RetrieveAPIView):
	queryset = Card.objects.all()
	serializer_class = CardSerializer

class TransactionList(generics.ListAPIView):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

class TransactionDetail(generics.RetrieveAPIView):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

class CentralAccountList(generics.ListAPIView):
	queryset = CentralAccount.objects.all()
	serializer_class = CentralAccountSerializer

class CentralAccountDetail(generics.RetrieveAPIView):
	queryset = CentralAccount.objects.all()
	serializer_class = CentralAccountSerializer

def AddBasics(request):
	customers = Customer.objects.all()
	
	if(customers.count() > 0):
		return HttpResponse(status = 403)
	else:
		c1 = Customer(name = "Erkki Esimerkki", email = "erkki.esimerkki@esim.fi", address = "Esimerkinkuja 11 E Espoo")
		c2 = Customer(name = "Eric Example", email = "eric.example@examples.com", address = "Example Street 14 E Espoo")
		
		c1.save()
		c2.save()
		
		account = CentralAccount(debit = 0, credit = 1000, currency= "EUR", accountName = "Main Account Finland", accountCountry = "FIN")
		account.save()
		
		card1 = Card(ownerID = c1.customerID, bankID = account.centralAccountID, debit = 500.0, credit = 0.0, currency = "EUR")
		card2 = Card(ownerID = c2.customerID, bankID = account.centralAccountID, debit = 500.0, credit = 0.0, currency = "EUR")
		
		card1.save()
		card2.save()
		
		return HttpResponse(status = 200)


def Message(request):
	if(request.method == 'POST'):
		type = request.POST['type']
		
		if(type == 'authorization'):
			c_id			= request.POST['card_id']
			t_id			= request.POST['transaction_id']
			m_name			= request.POST['merchant_name']
			m_country		= request.POST['merchant_country']
			m_city			= request.POST['merchant_city']
			m_mcc			= request.POST['merchant_mcc']
			bill_amount 	= request.POST['billing_amount']
			bill_currency	= request.POST['billing_currency']
			trans_amount	= request.POST['transaction_amount']
			trans_currency	= request.POST['transaction_currency']
			
			cards = Card.objects.filter(cardID=c_id)
			
			if(cards.count() == 1):
				card = cards[0]
				balance = card.debit - card.credit
				
				if (balance >= bill_amount):
					card.credit = card.credit + bill_amount
					trans = Transaction(transactionID = t_id, cardID = c_id, datetime = datetime.now(), authorized = True,
					merchant_name = m_name, merchant_country = m_country, merchant_city = m_city, merchant_mcc = m_mcc,
					transaction_currency = trans_currency, transaction_amount = trans_amount,
					billing_currency = bill_currency, billing_amount = bill_amount)
				
					card.save()
					trans.save()
				
					return HttpResponse(status = 200)
				else:
					return HttpResponse(status = 403)
			
			else:
				return HttpResponse(status = 403)
	
			return HttpResponse(status = 200)
		
		if(type == 'presentment'):
			c_id			= request.POST['card_id']
			t_id			= request.POST['transaction_id']
			m_name			= request.POST['merchant_name']
			m_country		= request.POST['merchant_country']
			m_city			= request.POST['merchant_city']
			m_mcc			= request.POST['merchant_mcc']
			bill_amount		= request.POST['billing_amount']
			bill_currency	= request.POST['billing_currency']
			trans_amount	= request.POST['transaction_amount']
			trans_currency	= request.POST['transaction_currency']
			sett_amount		= request.POST['settlement_amount']
			sett_currency	= request.POST['settlement_currency']
			
			transactions = Transaction.objects.filter(transactionID = t_id)
			
			if((transaction.count == 1) and (transaction[0].authorized == True) and (transaction[0].settled == False)):
				transaction = transactions[0]
				
				card.credit = card.credit - transaction.billing_amount
				
				transaction.settled					= True
				transaction.merchant_name			= m_name
				transaction.merchant_country		= m_country
				transaction.merchant_city			= m_city
				transaction.merchant_mcc			= m_mcc
				transaction.transaction_currency	= trans_currency
				transaction.transaction_amount		= trans_amount
				transaction.billing_currency 		= bill_currency
				transaction.billing_amount			= bill_amount
				transaction.settlement_currency		= sett_currency
				transaction.settlement_amount		= sett_amount
				
				#Kortti
				card.debit = card.debit - settlement_amount
		
				#Tili
				account.debit = account.debit + settlement_amount
			
				card.save()
				account.save()
				
				return HttpResponse(status = 200)
			else:
				return HttpResponse(status = 403)
		
		if(type == 'settlement'):
			
			acc_id = request.POST['account_id']
			
			accounts = CentralAccount.objects.filter(centralAccountID = acc_id)
			
			if(accounts.count() != 1):
				return HttpResponse(status = 403)
			else:
				account = accounts[0]
				account.credit = account.credit - account.debit
				account.debit = 0
		
				#Insert-sending-settlement-minus-our-share-to-card-company-here
		
				account.save()

				return HttpResponse(status = 200)
		
		return HttpResponse(status = 403)
		
	else:
		return HttpResponse(status = 403)
