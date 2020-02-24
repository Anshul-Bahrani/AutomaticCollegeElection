import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from academics.models import Department
from voting.models import Ballot
from ACE.users.models import Student, CustomUser
import json
from django.db import connection

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
def my_custom_sql(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return rows

class HomeView(LoginRequiredMixin ,TemplateView):
    template_name = 'pages/home.html'
    def get(self, request, *args, **kwargs):
        query = 'SELECT dept_name, COUNT(vot_id),MAX(elec_date), post_name FROM ( SELECT dept.id as dept_id, student.id as student_id, ball.voter_id as ball_voter_id, nom.id as nom_id, ball.nominee_id as ball_nominee_id, nom.election_id as nom_election_id, elec.id as elec_id, elec.position_id as elec_position_id, post.id as post_id, dept.name as dept_name, post.name as post_name,ball.id as vot_id , elec.start_at as elec_date FROM academics_department as dept, voting_position as post, voting_ballot as ball, users_customuser as student, voting_nominee as nom, voting_election as elec WHERE dept.id = student.department_id_id AND ball.voter_id = student.id AND nom.id = ball.nominee_id AND nom.election_id = elec.id AND elec.position_id = post.id )as derived GROUP BY dept_name, post_name;'
        answer = list(my_custom_sql(query))
        answer2 = list()
        for i in answer:
            tempo = datetime.datetime.strftime(i[2], "%y")
            temp = tuple([i[0], i[1], tempo, i[3]])
            answer2.append(temp)
        answer = json.dumps(answer2)
        print(answer2)



        id = request.user
        tempquery = f"SELECT dept.id FROM academics_department as dept, users_customuser as user WHERE user.department_id_id = dept.id AND user.email = '{id}'"
        ans = my_custom_sql(tempquery)
        print(ans)
        deptid = ans[0][0]


        query2 = f'SELECT user.first_name, user.last_name, COUNT(*), MAX(election.start_at) FROM users_customuser as user, voting_electedmember as final, voting_election as election, voting_ballot as votes, academics_department as dept, academics_term as term WHERE final.election_id = election.id AND votes.election_id = final.election_id AND votes.nominee_id = final.member_id AND user.id = final.member_id AND term.department_id_id = {deptid} GROUP BY user.id'
        baranswer = my_custom_sql(query2)
        print(baranswer)
        baranswer2 = list()
        for i in baranswer:
            tempo = datetime.datetime.strftime(i[3], "%y")
            temp = tuple([i[0], i[1], i[2], tempo])
            baranswer2.append(temp)
        baranswer = json.dumps(baranswer2)
        # pylint: disable=unused-argument
        context = {'sidebarSection': 'dashboard', 'answer' : answer, 'baranswer' : baranswer}
        return render(request, self.template_name, context)
