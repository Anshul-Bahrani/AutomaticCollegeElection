from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
# pylint: disable=unused-import
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.views import View
from tablib import Dataset
from .resources import NomineeResource


from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from ACE.users.models import CustomUser, Student
from staff.models import StaffCtCcAllotment
from .models import Position, Nominee, Election, Ballot


class PositionListView(ListView):

    template_name = 'voting.position-list.html'
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

def simple_upload(request):
    # if request.method == 'GET':
    #     nominee_resource = NomineeResource()
    #     dataset = Dataset()
    #     return render(request, "voting/import.html")

    # if request.method == 'POST':
    #     nominee_resource = NomineeResource()
    #     dataset = Dataset(['', 'New nominees'], headers=['id', 'agenda'])
    #     new_nominees = request.FILES['myfile']

    #     result = nominee_resource.import_data(dataset, dry_run=True)  # Test the data import

    #     if not result.has_errors():
    #         nominee_resource.import_data(dataset, dry_run=False)  # Actually import now

    return redirect('/admin/voting/nominee/import/')

class VotingView(LoginRequiredMixin, View):

    template_name = 'voting/voting.html'
    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(pk=request.user.pk)
        student = Student.objects.get(user_id=user.pk)
        staff = StaffCtCcAllotment.objects.filter(division=student.division).first()
        election = Election.objects.filter(Q(registrar=staff.class_teacher) | Q(registrar=staff.class_counsellor))
        context = {
            'elections': election,
        }

        return render(request, self.template_name, context)

class ElectionNommineeListView(LoginRequiredMixin, View):

    template_name = 'voting/election_nominee.html'
    def get(self, request, *args, **kwargs):
        election = get_object_or_404(Election, pk=self.kwargs.get('pk'))
        nominees = Nominee.objects.filter(election=election)
        context = {
                'nominees': nominees,
            }

        return render(request, self.template_name, context)

class VoteView(LoginRequiredMixin, View):

    template_name = 'voting/vote.html'
    def get(self, request, *args, **kwargs):
        election = get_object_or_404(Election, pk=self.kwargs.get('election'))
        nominee = get_object_or_404(Nominee, pk=self.kwargs.get('nominee'))
        user = CustomUser.objects.get(pk=request.user.pk)
        vote = Ballot()
        vote.election = election
        vote.nominee = nominee
        vote.voter = user
        vote.save()
        messages.add_message(request, messages.SUCCESS, "ThankYou for your vote")
        return redirect('home')
