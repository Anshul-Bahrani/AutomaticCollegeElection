from django.urls import path
from . import views as academics_views

app_name = 'academics'

urlpatterns = [

    path('term-create/', academics_views.TermCreateView.as_view(), name='term_create'),
    path('term-list/', academics_views.TermListView.as_view(), name='term_list'),
    path('department-create/', academics_views.DepartmentCreateView.as_view(), name='department_create'),
    path('department-list/', academics_views.DepartmentListView.as_view(), name='department_list'),
]
