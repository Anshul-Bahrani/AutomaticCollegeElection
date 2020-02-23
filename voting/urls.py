from django.urls import path
from . import views as voting_views

app_name = 'voting'

urlpatterns = [

    path('position-list/', voting_views.PositionListView.as_view(), name='position_list'),
    path('position-create/', voting_views.PositionCreateView.as_view(), name='position_create'),
    path('nominee-create/', voting_views.NomineeCreateView.as_view(), name='nominee_create'),
    path('nominee-list/', voting_views.NomineeListView.as_view(), name='nominee_list'),
    path('election-create/', voting_views.ElectionCreateView.as_view(), name='election_create'),
    path('election-list/', voting_views.ElectionListView.as_view(), name='election_list'),
]
