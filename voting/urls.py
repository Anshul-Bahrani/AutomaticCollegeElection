from django.urls import path
from . import views as voting_views

app_name = 'printer'

urlpatterns = [

    path('position-list/', voting_views.PositionListView.as_view(), name='position_list'),
    path('position-create/', voting_views.PositionCreateView.as_view(), name='position_create'),
    path('nominee-create/', voting_views.NomineeCreateView.as_view(), name='nominee_create'),

]
