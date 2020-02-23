from django.urls import path
from . import views as staff_views

app_name = 'staff'

urlpatterns = [

    path('ctcc-create/', staff_views.CtCcCreateView.as_view(), name='ctcc_create'),
    path('ctcc-list/', staff_views.CtCcListView.as_view(), name='ctcc_list'),
]
