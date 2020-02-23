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

from .models import Position, Nominee, Election


class PositionListView(ListView):

    template_name = 'voting/position-list.html'
    model = Position
    context_object_name = 'positions'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # pylint: disable=arguments-differ
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['sidebarSection'] = 'position'
        return context

class PositionCreateView(LoginRequiredMixin, CreateView):

    model = Position
    template_name = 'voting/position-create.html'
    fields = ['name', 'type']
    success_message = "%(name)s was created successfully"

class NomineeCreateView(CreateView):

    model = Nominee
    template_name = 'voting/nominee-create.html'
    fields = ['agenda', 'election']
    success_message = "%(title)s was created successfully"

    def form_valid(self, form):
        form.instance.nominee_id = self.request.user
        return super().form_valid(form)

class NomineeListView(ListView):

    template_name = 'voting/nominee_list.html'
    model = Nominee
    context_object_name = 'nominees'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # pylint: disable=arguments-differ
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['sidebarSection'] = 'nominee'
        return context

class ElectionCreateView(CreateView):

    model = Election
    template_name = 'voting/election-create.html'
    fields = ['position', 'term_id', 'start_at', 'duration', 'nomination_deadline']
    success_message = "%(title)s was created successfully"

    def form_valid(self, form):
        form.instance.registrar = self.request.user
        return super().form_valid(form)

class ElectionListView(ListView):

    template_name = 'voting/election_list.html'
    model = Election
    context_object_name = 'elections'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # pylint: disable=arguments-differ
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['sidebarSection'] = 'election'
        return context

# class VotingView(View):

#     def get(self, request, *args, **kwargs):
#         user = request.user

