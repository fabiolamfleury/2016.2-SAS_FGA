from django.conf.urls import url
from django.contrib import admin
from .views import new_booking, search_booking, search_booking_table, search_booking_query
from .views import confirm_booking, cancel_booking

urlpatterns = [
    url(r'^newbooking/$', new_booking, name='newbooking'),
    url(r'^searchbooking/$', search_booking, name='searchbooking'),
    url(r'^confirmbooking/(\d+)$', confirm_booking, name='confirmbooking'),
    url(r'^cancelbooking/(\d+)$', cancel_booking, name='cancelbooking'),
	url(r'^searchbookingg/$', search_booking_table, name='searchbookingtable'),
	url(r'^searchbookingquery/$', search_booking_query, name='searchbookingquery'),
]
