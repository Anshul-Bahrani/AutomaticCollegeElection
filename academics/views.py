from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
# pylint: disable=unused-import
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.views import View
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from .models import Department, Term

class TermCreateView(CreateView):

    model = Term
    template_name = 'academics/term_create.html'
    fields = ['academic_year', 'department_id', 'sem']
    success_message = "%(title)s was created successfully"

    def form_valid(self, form):
        form.instance.term_id = f"{form.instance.academic_year%100}{form.instance.department_id.pk}{form.instance.sem}"
        return super().form_valid(form)

class TermListView(ListView):

    template_name = 'academics/term_list.html'
    model = Term
    context_object_name = 'terms'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # pylint: disable=arguments-differ
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['sidebarSection'] = 'term'
        return context

class DepartmentCreateView(CreateView):

    model = Department
    template_name = 'academics/department_create.html'
    fields = ['code', 'name']
    success_message = "%(title)s was created successfully"

class DepartmentListView(ListView):

    template_name = 'academics/department_list.html'
    model = Department
    context_object_name = 'departments'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # pylint: disable=arguments-differ
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['sidebarSection'] = 'department'
        return context
