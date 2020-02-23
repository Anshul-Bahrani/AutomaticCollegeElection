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

from .models import StaffCtCcAllotment

class CtCcCreateView(CreateView):

    model = StaffCtCcAllotment
    template_name = 'staff/staff_cc_ct_allotment_create.html'
    fields = ['term_id', 'division', 'class_teacher', 'class_counsellor']
    success_message = "%(title)s was created successfully"

    def form_valid(self, form):
        print("######################", form.instance.class_teacher.role.role_number)
        if(form.instance.class_teacher.role.role_number == 1 and form.instance.class_counsellor.role.role_number == 1):
            return super().form_valid(form)

        return HttpResponse("404")

class CtCcListView(ListView):

    template_name = 'staff/staff_cc_ct_allotment_list.html'
    context_object_name = 'objects'
    model = StaffCtCcAllotment
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # pylint: disable=arguments-differ
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['sidebarSection'] = 'ctcc'
        return context
