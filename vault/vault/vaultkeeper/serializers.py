from django.contrib.auth.models import User
from rest_framework import serializers
from vaultkeeper.models import Customer, Card, Transaction, CentralAccount

class CentralAccountSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = CentralAccount
		fields = ('centralAccountID', 'debit', 'credit', 'currency', 'accountName', 'accountCountry')

class CustomerSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Customer
		fields = ('customerID', 'name', 'email', 'address')
	

class CardSerializer(serializers.ModelSerializer):
	owner = serializers.CharField(read_only=True)
	
	class Meta:
		model = Card
		fields = ('cardID', 'ownerID', 'bankID', 'debit', 'credit', 'currency')
		
class TransactionSerializer(serializers.ModelSerializer):
	card = serializers.CharField(read_only=True)
	
	class Meta:
		model = Transaction
		fields = ('transactionID', 'cardID', 'authorized', 'settled', 'datetime',
		'transaction_amount', 'transaction_currency', 'billing_amount','billing_currency', 'settlement_amount', 'settlement_currency',
		'merchant_name', 'merchant_country', 'merchant_mcc')

