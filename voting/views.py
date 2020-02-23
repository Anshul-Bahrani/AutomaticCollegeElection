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

from .models import Position, Nominee


class PositionListView(ListView):

    template_name = 'voting/position_list.html'
    model = Position
    context_object_name = 'positions'
    paginate_by = 20

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
    success_message = "%(title)s was created successfully"

class NomineeCreateView(CreateView):

    model = Nominee
    template_name = 'voting/nominee-create.html'
    fields = ['agenda', 'election']
    success_message = "%(title)s was created successfully"
