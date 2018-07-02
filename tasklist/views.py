from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .forms import SignupForm, TaskForm
from .models import Task
from django.db.models import Max
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# from .models import Task

# Create your views here.
@login_required
def index(request, username):
    # import pdb; pdb.set_trace()

    form = TaskForm()

    search_param = request.GET.get('search')
    search = ''

    if search_param is not None:
        search = request.GET["search"]
        data = Task.objects.filter(user_id=request.user, status=1, is_active=1, task_head__contains=search).order_by('due_date')

    else:
        data = Task.objects.filter(user_id=request.user, status=1, is_active=1).order_by('due_date')
    
    # import pdb; pdb.set_trace()
    task_id_list = data.values_list('task_id', flat=True)
    sub_task_dict = {}

    if len(task_id_list) > 0:
        sub_task = Task.objects.filter(task_id__in=task_id_list,parent_task_id__gt=0,status=1).values('parent_task_id', 'task_id', 'task_group', 'task_group_id')
        for row in sub_task:
            key = row['parent_task_id']
            if key in sub_task_dict:
                sub_task_dict[key].append(row)
            else:
                sub_task_dict[key] = [row]

    # import pdb; pdb.set_trace()
    
    return render(request, 'tasklist/home.html', {'username': request.user.username , 'task_form': form, 'data': data, 'sub_task': sub_task_dict, 'search': search})

@login_required
def completedPage(request, username):
    pass


@login_required
def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # import pdb; pdb.set_trace()
            data = Task.objects.filter(user_id=request.user, task_group=request.POST['task_group']).aggregate(Max('task_group_id'))
            parent_task = request.POST['parent_task']
            # import pdb; pdb.set_trace()
            parent_task_arr = parent_task.split('-')
            post = form.save(commit=False)

            if len(parent_task_arr) == 2:
                # import pdb; pdb.set_trace()
                get_parent = Task.objects.filter(user_id=request.user, task_group=parent_task_arr[0].upper(), task_group_id=parent_task_arr[1]).values('task_id')
                if len(get_parent) == 1:
                    post.parent_task_id = get_parent[0]['task_id']
                
            task_group_id =  int(data['task_group_id__max'] or 0)
            
            post.user_id = request.user
            post.task_group_id = task_group_id + 1
            # import pdb; pdb.set_trace()
            post.save()

    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)

@login_required
def deleteTask(request):
    if request.method == 'POST':
        task_id = request.POST['task_id']
        del_task = Task.objects.filter(task_id=task_id).update(status=0)
    return JsonResponse({"task_id": task_id, "success": del_task})

@login_required
def updateTask(request):
    if request.method == 'POST':
        task_id = request.POST['task_id']
        task_head = request.POST['task_head']
        description = request.POST['description']
        due_date = request.POST['due_date']
        update_task = Task.objects.filter(task_id=task_id).update(task_head=task_head, description=description, due_date=due_date)
    return JsonResponse({"task_id": task_id, "success": update_task})

@login_required
def completeTask(request):
    if request.method == 'POST':
        task_id = request.POST['task_id']
        complete_task = Task.objects.filter(task_id=task_id).update(is_active=0)
    return JsonResponse({"task_id": task_id, "success": complete_task})

@login_required
def task_search(request):
    search_qs = Task.objects.filter(task_head_startswith=request.REQUEST['search'])
    results = []
    for r in search_qs:
        results.append(task_head.name)
    resp = request.REQUEST['callback'] + '(' + simplejson.dumps(result) + ');'
    return HttpResponse(resp, content_type='application/json')

def signup(request):
    if request.method == 'POST':
        if request.POST.get('submit') == 'sign_up':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save()
            # user.is_active = False
            # user.save()

                return redirect('user_page', username=request.POST['username'])
        elif request.POST.get('submit') == 'login':
            username = request.POST['username']
            password = request.POST['password']
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('user_page')
            else:
                form = SignupForm()

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'signup_form': form})

