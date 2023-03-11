from django.shortcuts import render, redirect
from .models import Student
from .form import StudentForm

def main_page(request):
    students = Student.objects.all()
    return render(request, 'main_page.html', {'students': students})

def StudentListView(request):
    students = Student.objects.all()
    return render(request, 'student_detail.html', {'students': students})

def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'endpage.html')
    return render(request, 'student_form.html', {'form': form})

def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return render(request, 'endpage.html')
    return render(request, 'student_form.html', {'form': form})

def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return render(request, 'endpage.html')
