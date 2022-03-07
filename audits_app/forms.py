from django import forms
from .models import Audit
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AuditForm(forms.ModelForm):
    class Meta:
        model = Audit
        fields = ['date_added', 'audit_zone', 'type_of_risk', 'level_of_risk']
        labels = {
            'date_added': 'Дата аудита',
            'audit_zone': 'Зона аудита',
            'type_of_risk': 'Оцениваемый риск',
            'level_of_risk': 'Уровень риска',
        }


class SignUpForm(UserCreationForm):
    required_css_class = "field"
    error_css_class = "error"

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name')
        labels = {
            'username': 'Логин',
        }
