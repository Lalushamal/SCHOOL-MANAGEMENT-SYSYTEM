from django import forms
from .models import Register,Course,Attendences,Mark,Attend

EXTRA_CHOICES = [
    ('january','january'),
    ('february','february'),
    ('march','march'),
    ('april','april'),
    ('may','may'),
    ('june','june'),
    ('july','july'),
    ('august','august'),
    ('september','september'),
    ('october','october'),
    ('november','november'),
    ('december','december'),
    ]


class DateInput(forms.DateInput):
    input_type = 'date'

class NewForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
class RegisterPost(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
class CourseForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['course']
class BatchForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['batch_time']
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['register_no']
class AttendenceForm(forms.ModelForm):
    class Meta:
        model = Attendences
        fields = '__all__'
class AttendForm(forms.Form):
        month=forms.ChoiceField(choices = EXTRA_CHOICES)
class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = '__all__'
        widgets = {
            'exam_date': DateInput()
        }
    


