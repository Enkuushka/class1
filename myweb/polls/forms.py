from django import forms

class NameForm(forms.Form):
    YEAR_IN_SCHOOL_CHOICES = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]
    your_name = forms.CharField(label='Your name', max_length=100, min_length=2)
    songolt = forms.TypedChoiceField(label='Сонгох', choices=YEAR_IN_SCHOOL_CHOICES)
    ognoo = forms.DateField(label="Ognoo")