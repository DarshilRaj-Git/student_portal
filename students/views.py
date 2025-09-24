from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def register_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_student')  # reload page after submit
    else:
        form = StudentForm()

    students = Student.objects.all()
    return render(request, 'students/register.html', {'form': form, 'students': students})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/register.html', {'form': StudentForm(), 'students': students})
