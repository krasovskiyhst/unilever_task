from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AuditForm, SignUpForm
from .models import Audit
from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def create_audit(request):
    """Создать новый аудит"""
    if request.method != 'POST':
        form = AuditForm()
    else:
        form = AuditForm(data=request.POST)
        if form.is_valid():
            # Присвоение исполнителя перед сохранением
            new_audit = form.save(commit=False)
            new_audit.performer = request.user
            new_audit.save()
            return redirect('list_of_audits')

    context = {'form': form}
    return render(request, 'create_audit.html', context)


@login_required
def list_of_audits(request):
    audits = Audit.objects.all()
    context = {
        'audits': audits,
    }
    return render(request, 'list_of_audits.html', context)


@login_required
def edit_audit(request, audit_id):
    """Редактировать аудит"""
    audit = Audit.objects.get(id=audit_id)
    if request.method != 'POST':
        form = AuditForm(instance=audit)
    else:
        form = AuditForm(data=request.POST)
        if form.is_valid():
            # Присвоение исполнителя перед сохранением
            new_audit = form.save(commit=False)
            new_audit.performer = request.user
            new_audit.save()
            return redirect('list_of_audits')

    context = {'form': form, 'audit': audit}
    return render(request, 'edit_audit.html', context)


def register(request):
    """Регистрирует нового пользователя."""
    if request.method != 'POST':
        form = SignUpForm()
    else:
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('index')

    context = {'form': form}
    return render(request, 'register.html', context)


def logout_view(request):
    """Выход"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))
