from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from vaultkeeper import views

urlpatterns = [
	url(r'^customers/$', views.CustomerList.as_view()),
	url(r'^customers/(?P<pk>[0-9]+)/$', views.CustomerDetail.as_view()),
	url(r'^accounts/$', views.CentralAccountList.as_view()),
	url(r'^accounts/(?P<pk>[0-9]+)/$', views.CentralAccountList.as_view()),
	url(r'^cards/(?P<pk>[0-9]+)/$', views.CardDetail.as_view()),
	url(r'^cards/$', views.CardList.as_view()),
	url(r'^transactions/(?P<pk>[0-9]+)/$', views.TransactionDetail.as_view()),
	url(r'^transactions/$', views.TransactionList.as_view()),
	url(r'^addbasics/$', views.AddBasics),
	url(r'^message/$', views.Message),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
