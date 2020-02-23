from django.shortcuts import render
from django.views.generic import TemplateView
from academics.models import Department
from voting.models import Ballot
from ACE.users.models import Student, CustomUser
import json
from django.db import connection

def my_custom_sql(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return rows

class HomeView(TemplateView):
    template_name = 'pages/home.html'
    def get(self, request, *args, **kwargs):
        query = 'SELECT dept_name, COUNT(vot_id), post_name FROM ( SELECT dept.id as dept_id, student.id as student_id, ball.voter_id as ball_voter_id, nom.id as nom_id, ball.nominee_id as ball_nominee_id, nom.election_id as nom_election_id, elec.id as elec_id, elec.position_id as elec_position_id, post.id as post_id, dept.name as dept_name, post.name as post_name,ball.id as vot_id FROM academics_department as dept, voting_position as post, voting_ballot as ball, users_customuser as student, voting_nominee as nom, voting_election as elec WHERE dept.id = student.department_id_id AND ball.voter_id = student.id AND nom.id = ball.nominee_id AND nom.election_id = elec.id AND elec.position_id = post.id )as derived GROUP BY dept_name, post_name;'
        answer = my_custom_sql(query)
        answer = json.dumps(answer)
        print(answer)
        # pylint: disable=unused-argument
        context = {'sidebarSection': 'dashboard', 'answer' : answer}
        return render(request, self.template_name, context)
