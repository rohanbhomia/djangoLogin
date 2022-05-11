import email
from django.shortcuts import render, redirect
from todos.forms import CreateTodo
from todos.models import Todos
from users.models import CustomUser
from django.contrib.auth import login
from login.views import home, login_page, login
from django.contrib import messages
from django_datatables_view.base_datatable_view import BaseDatatableView


def create_todo(request):
    form = CreateTodo()
    user = request.user
    if request.method == "POST":
        form = CreateTodo(
            request.POST)
        title = request.POST.get('title')
        description = request.POST.get('description')
        print('CustomUser...', user.email)
        custom_user = CustomUser.objects.get(email=user.email)
        print('CustomUser...', custom_user)
        todos = Todos(
            title=title,
            description=description,
            user_id=custom_user
        )
        todos.save()
        messages.success(request, 'Created successfully')
        return redirect('create_todo')

    return render(request, "todos/create_todo.html", {'form': form})


def delete_todo(request):

    row_id = request.POST.get('row_id')
    todo_obj = Todos.objects.filter(id=row_id).delete()
    print('row_id...', row_id)
    messages.success(request, 'Deleted successfully')
    return redirect('todo_list')


def edit_todo(request):

    row_id = request.POST.get('row_id')
    title = request.POST.get('title')
    description = request.POST.get('description')

    todo_obj = Todos.objects.get(id=row_id)
    todo_obj.title = title
    todo_obj.description = description
    todo_obj.save()

    print('row_id...', row_id)
    messages.success(request, 'Updated successfully')
    return redirect('todo_list')


def todo_list(request):

    return render(request, "todos/list.html")


class todo_list_json(BaseDatatableView):
    model = Todos

    columns = ['id', 'title', 'description', 'action']
    order_columns = ['id', '', '', '', '', '', '', '']

    def get_initial_queryset(self):
        Todos_obj = Todos.objects.filter()

        return Todos_obj

    def render_column(self, row, column):

        if column == 'action':
            onclick = f"editFunction('{row.title}','{row.description}','{row.id}')"

            return f'<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#editmodal" onclick={onclick}>Edit</button>&nbsp;&nbsp;&nbsp;<button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#deletemodal" onclick="deleteFunction('+str(row.id)+')">Delete</button>'

        return super(todo_list_json, self).render_column(row, column)

    def filter_queryset(self, qs):

        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(title__icontains=search)

        return qs


# @login_required(login_url='/adminlogin/login')
# def ReachOuts(request):

#     getColumn = HiringQuestion.objects.using('replica').values(
#         'columnLable', 'question_response').filter(bot_uuid=request.GET['bot_id']).order_by('sort_order')
#     setColumn = []
#     check = []

#     for c in getColumn:
#         if c['question_response'] not in check:
#             setColumn.append(c['columnLable'])
#             check.append(c['question_response'])

#     org_obj = Clients.objects.get(org_id=request.GET['org_id'])
#     campaign_obj = Sms_campaigns.objects.get(id=request.GET['campaign_id'])
#     bot_obj = Bots.objects.get(id=request.GET['bot_id'])

#     stu = {
#         "heading": "Conversation list",
#         "org_id": request.GET['org_id'],
#         "bot_id": request.GET['bot_id'],
#         "campaign_id": request.GET['campaign_id'],
#         "setColumn": setColumn,
#         "org_obj": org_obj,
#         "campaign_obj": campaign_obj,
#         "bot_obj": bot_obj


#     }
#     return render(request, "conversation/reachouts.html", stu)


# class ListRandstadJson(BaseDatatableView):
# 	model = Clients


# 	def get_columns(self):
# 		columns=[]
# 		skill_columns = []
# 		hiring_column = []
# 		org_id = self.request.GET.get('SearchData')
# 		bot_id = self.request.GET.get('SearchData1')
# 		campaign_id = self.request.GET.get('SearchData2')


# 		columns.append('id')
# 		columns.append('candidate_number')

# 		getColumn = HiringQuestion.objects.using('replica').values('columnLable','question_response').filter(bot_uuid=bot_id).order_by('sort_order')

# 		for c in getColumn:
# 			if c['question_response'] not in columns:
# 				columns.append(c['question_response'])
# 				skill_columns.append(c['question_response'])


# 		hiring_column.append('candidate_number')
# 		self.request.POST.column=hiring_column
# 		self.request.POST.skill_columns=skill_columns


# 		return columns


# 	def get_initial_queryset(self):
# 		org_id = self.request.GET.get('SearchData')
# 		bot_id = self.request.GET.get('SearchData1')
# 		campaign_id = self.request.GET.get('SearchData2')

# 		qt =  Sendlist.objects.using('replica').values(*self.request.POST.column).filter(bot_id=bot_id,campaign_id=campaign_id).order_by('-id')
# 		for skill_single in self.request.POST.skill_columns  :
# 			kwarg = {skill_single : Skills.objects.using('replica').values('skill_value').filter(skill_keyword=skill_single).extra(where=['`campaigns_sendlist`.`id`=U0.`sendlist_id`'])}
# 			qt = qt.annotate(**kwarg)
# 		self.max_display_length=100000

# 		return qt

# 	def render_column(self, row, column):
# 		cursor = connections['default'].cursor()

# 		return super(ListRandstadJson, self).render_column(row, column)


# 	def filter_queryset(self, qs):


# 		search = self.request.GET.get('search[value]', None)
# 		if search:
# 			qs = qs.filter(company_name__icontains=search)

# 		return qs
