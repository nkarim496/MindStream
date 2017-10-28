from django.shortcuts import render, redirect
from minder.models import Mind, UserProfile
from utils import minds_lst_builder
from minder.forms import MindForm
from django.contrib.auth.decorators import login_required


def index(request):
    if request.user.is_authenticated:
        return redirect('minds', username=request.user.username)
    else:
        return redirect('auth_login')


def minds(request, username):
    context = {}
    if 'added' in request.GET:
        context['mind_added'] = True
    if request.user.is_authenticated and request.user.username == username:
        if request.method == 'POST':
            form = MindForm(request.POST, request.FILES)
            if form.is_valid():
                mind = form.save(commit=False)
                mind.user = request.user
                mind.save()
                return redirect('/' + request.user.username + '/' + '?added=1')
            else:
                print(form.errors)
        form = MindForm()
        context['form'] = form
    try:
        userprofile = UserProfile.objects.get(user__username=username)
    except UserProfile.DoesNotExist:
        userprofile = None
    context['userprofile'] = userprofile
    if userprofile:
        context['minds'] = minds_lst_builder(username, 7)
    return render(request, 'minder/minds.html', context)


@login_required
def mind_del(request, username, mind_id):
    if username == request.user.username:
        Mind.objects.filter(pk=mind_id).delete()
    return redirect('minds', request.user.username)

@login_required
def mind_edit(request, username, mind_id):
    context = {}
    if username == request.user.username:
        try:
            mind = Mind.objects.get(pk=mind_id)
        except Mind.DoesNotExist:
            mind = None
        if mind:
            if request.method == 'POST':
                form = MindForm(request.POST, request.FILES, instance=mind)
                if form.is_valid():
                    form.save()
                    return redirect('minds', request.user.username)
                else:
                    print(form.errors)
            context['form'] = MindForm(instance=mind)
    return render(request, 'minder/mind_edit.html', context)
