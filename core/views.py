from django.shortcuts import render
from django.views.generic import TemplateView
from academics.models import Department
from voting.models import Ballot
from ACE.users.models import Student, CustomUser


class HomeView(TemplateView):
    template_name = 'pages/home.html'
    def get(self, request, *args, **kwargs):
        query = Department.objects.raw('SELECT * FROM academics_department as dept, voting_position as post, voting_ballot as ball, users_customuser as student, voting_nominee as nom, voting_election as elec WHERE dept.id = student.id AND ball.voter_id = student.id AND nom.id = ball.nominee_id AND nom.election_id = elec.id AND elec.position_id = post.id;')
        print(query)
        # pylint: disable=unused-argument
        context = {'sidebarSection': 'dashboard'}
        return render(request, self.template_name, context)
