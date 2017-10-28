from django.shortcuts import render, redirect
from django.utils import timezone
from wimm.models import Wimm, DayState
from wimm.forms import WimmForm, StateForm, WimmFormWithDate, LoginForm
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
import datetime


def index(request):
    context = {}
    date = timezone.now().date()
    context['current_date'] = date
    context['day_state'] = DayState.objects.filter(date=date).first()
    context['wimms'] = Wimm.objects.filter(pub_date__date=date).order_by('pub_date')
    return render(request, 'wimm/show_day.html', context)


def show_day(request, year, month, day):
    context = {}
    try:
        date = datetime.date(day=int(day), month=int(month), year=int(year))
    except ValueError:
        raise Http404("Invalid date")
    context['current_date'] = date
    context['day_state'] = DayState.objects.filter(date=date).first()
    context['wimms'] = Wimm.objects.filter(pub_date__date=date, show=True).order_by('pub_date')
    return render(request, 'wimm/show_day.html', context)


def user_login(request):
    # if user is authenticated it doesn't need login
    if request.user.is_authenticated():
        return redirect('index')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login()
            login(request, user)
            return redirect('index')
    return render(request, 'wimm/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


@login_required
def add_wimm(request):
    form = WimmForm()
    if request.method == 'POST':
        form = WimmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'wimm/add_wimm.html', {'form': form})


@login_required
def add_wimm_for_date(request, day, month, year):
    pub_date = timezone.now().replace(day=int(day), month=int(month), year=int(year))
    form = WimmFormWithDate(initial={'pub_date': pub_date})
    if request.method == 'POST':
        form = WimmFormWithDate(request.POST, request.FILES)
        if form.is_valid():
            wimm = form.save()
            return redirect('show_day', wimm.pub_date.day, wimm.pub_date.month, wimm.pub_date.year)
    return render(request, 'wimm/add_wimm.html', {'form': form})


@login_required
def show_trash(request):
    wimms = Wimm.objects.filter(show=False).order_by('-pub_date')
    return render(request, 'wimm/show_trash.html', {'wimms': wimms})


@login_required
def edit_wimm(request, wimm_id):
    wimm = Wimm.objects.get(pk=wimm_id)
    date = wimm.pub_date
    # get image name
    if wimm.img:
        img_name = wimm.img.name.split('/').pop()
    else:
        img_name = None
    form = WimmForm(instance=wimm)
    if request.method == 'POST':
        form = WimmForm(request.POST, request.FILES, instance=wimm)
        if form.is_valid():
            form.save()
            return redirect('show_day', date.day, date.month, date.year)
    return render(request, 'wimm/edit_wimm.html', {'form': form, 'img_name': img_name})


@login_required
def trash_wimm(request, wimm_id):
    wimm = Wimm.objects.get(pk=wimm_id)
    pub_date = wimm.pub_date
    wimm.show = False
    wimm.save()
    return redirect('show_day', pub_date.day, pub_date.month, pub_date.year)


@login_required
def restore_wimm(request, wimm_id):
    wimm = Wimm.objects.get(pk=wimm_id)
    wimm.show = True
    wimm.save()
    return redirect('show_trash')


@login_required
def delete_wimm(request, wimm_id):
    wimm = Wimm.objects.get(pk=wimm_id)
    wimm.delete()
    return redirect('show_trash')


@login_required
def add_state(request):
    form = StateForm()
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'wimm/add_state.html', {'form': form})


@login_required
def edit_state(request, day, month, year):
    # valid date checking
    try:
        date = datetime.date(day=int(day), month=int(month), year=int(year))
    except ValueError:
        raise Http404("Invalid date")
    # if date in DayState
    try:
        day_state = DayState.objects.get(date=date)
    except DayState.DoesNotExist:
        day_state = None
    # form generating
    if day_state:
        form = StateForm(instance=day_state)
    else:
        form = StateForm()
    if request.method == 'POST':
        # check for duplicating
        if day_state:
            form = StateForm(request.POST, instance=day_state)
        else:
            form = StateForm(request.POST)
        if form.is_valid():
            di = form.save(commit=False)
            di.date = date
            di.save()
            return redirect('show_day', di.date.day, di.date.month, di.date.year)
    return render(request, 'wimm/add_state.html', {'form': form})


@login_required
def del_state(request, state_id):
    day_state = DayState.objects.get(pk=state_id)
    state_date = day_state.date
    day_state.delete()
    return redirect('show_day', state_date.day, state_date.month, state_date.year)

