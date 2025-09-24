from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age']

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 5:
            raise forms.ValidationError("Age must be at least 5.")
        return age
