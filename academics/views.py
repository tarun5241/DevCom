from email import message
from django.shortcuts import render
from .models import Student,Marks
from django.http import  HttpResponse

def academics(request):
    return render(request, 'homepage/academics.html')

def student(request, pk):
    return render(request, 'homepage/student.html', {'pk':pk})


def addMarks(request):
    return render(request, 'homepage/add_marks.html')

def addStudent(request):
    if request.method == 'POST':
            uname = request.POST.get('uname')
            urollno = request.POST['rollno']
            upassword = request.POST['password']
            ustd = request.POST['std']

            data = Student(name=uname, rollno = urollno, password=upassword, std = ustd)
            data.save()
            print(uname, urollno, upassword, ustd)
            context = {'sts': "success"}
            return render(request, 'homepage/add_student.html', context)
    return render(request, 'homepage/add_student.html')
        # form = StudentForm(request.POST, request.FILES)
        # if form.is_valid():
        #     form.save()
        #     return redirect('projects')

def addMarks(request):
    if request.method == 'POST':
        print(request.POST.get('std'))

        # if Student.std == request.POST['std'] and Student.rollno == request.POST['rollno']:
        #     eng = request.POST['eng']
        #     math = request.POST['maths']            
        #     sci = request.POST['sci']     
        #     rs = Marks(eng=eng, math=math, sci=sci)
        #     rs.save()
        # print(eng)
        # print(math)
        # print(sci)
        context = {'sts': "success"}
        return render(request, 'homepage/add_marks.html', context)
    return render(request, 'homepage/add_marks.html')