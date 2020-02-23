from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):

    template_name = 'pages/home.html'

    def get(self, request, *args, **kwargs):
        # pylint: disable=unused-argument
        return render(request, self.template_name)
