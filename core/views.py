from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):

    template_name = 'pages/home.html'

    def get(self, request, *args, **kwargs):
        # pylint: disable=unused-argument
        context = {'sidebarSection': 'dashboard'}
        return render(request, self.template_name, context)
