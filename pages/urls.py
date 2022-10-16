from django.urls import path
from .views import home, hospitals, register_hospital, hospital_page, donors_list, register_donation, use_blood_hospital, loginPage, logoutUser

urlpatterns = [
    path('', home, name='home'),
    path('hospitals/', hospitals, name='hospitals'),
    path('registerhospital/', register_hospital, name='register-hospital'),
    path('hospital/<int:id>', hospital_page, name='hospital-page'),
    path('donorlist/<int:hospital_id>', donors_list, name='donor-list'),
    path('registerdonation/<int:hospital_id>', register_donation, name='register-donation-hospital'),
    path('hospitaluseblood/<int:hospital_id>', use_blood_hospital, name='use-blood-hospital'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
]