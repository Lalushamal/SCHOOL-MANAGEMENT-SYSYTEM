from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import RegisterPost,CourseForm,BatchForm,RegisterForm,NewForm,AttendenceForm,MarkForm,AttendForm
from . models import Register,Attendences,Mark
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle   





def index(request):
    form=CourseForm()
    forms=BatchForm()
    first=RegisterForm()
    connect=""
    connect1=""
    connect2=""
    attend=""
    mark=""
    if request.method=='POST' and 'btn1' in request.POST:
        num=request.POST['register_no']
        connect=Register.objects.get(register_no=num)
        attend=Attendences.objects.filter(register_no=num)
        mark=Mark.objects.filter(register_no=num)
    if request.method=='POST' and 'btn2' in request.POST:
        num=request.POST['course']
        connect1=Register.objects.filter(course=num)
    if request.method=='POST' and 'btn3' in request.POST:
        num=request.POST['batch_time']
        connect2=Register.objects.filter(batch_time=num)
    k={'connect':connect,'form':form,'forms':forms,'first':first,'attend':attend,'connect1':connect1,'connect2':connect2,'mark':mark}
    return render(request, 'index.html',k)

def login(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'login.html',{'form': form})
def register(request):
    if request.method == 'POST':
        form =RegisterPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'register.html',{'form':RegisterPost()})
def course(request):
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return index(request)
    return render(request,'course.html',{'form':NewForm()})
def attendence(request):
    if request.method == 'POST':
        forme = AttendenceForm(request.POST, request.FILES)
        if forme.is_valid():
            forme.save()
            return index(request)
    return render(request,'attendence.html',{'forme':AttendenceForm()})
def mark(request):
    if request.method == 'POST':
        form_1 = MarkForm(request.POST, request.FILES)
        if form_1.is_valid():
            form_1.save()
            return index(request)
    return render(request,'mark.html',{'form_1':MarkForm()})
def view(request,view_id):
    connect = Register.objects.get(register_no=view_id)
    attend=Attendences.objects.filter(register_no=view_id)
    mark=Mark.objects.filter(register_no=view_id)
    k={'connect':connect,'attend':attend,'mark':mark}
    return render(request,'view.html',k)
def student(request):
    connect = Register.objects.all()
    attend=Attendences.objects.all()
    mark=Mark.objects.all()
    k={'connect':connect,'attend':attend,'mark':mark}
    return render(request,'student.html',k)
def delete(request,view_id):
    empty = Register.objects.get(register_no=view_id)
    if request.method == 'POST':
        empty.delete()
        return redirect('index')
    return render(request, 'view.html', {'empty': empty})
def edit(request,view_id):
    text = Register.objects.get(register_no=view_id)
    form = RegisterPost(instance=text)
    if request.method == 'POST':
        form = RegisterPost(request.POST, instance=text)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'edit.html', {'form': form})
def getpdf(request):
    student=Register.objects.all()
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='attachment; filename="file.pdf"'
    p=canvas.Canvas(response)
    st={'student',student}
    p.setFont("Times-Roman",20)
    p.drawString(250,800,"ICS INDIA")
    p.setFont("Times-Roman",10)
    a=750
    for i in student:
        p.drawString(20,a,""+str(i.register_no))
        p.drawString(40,a,""+i.name)
        p.drawString(80,a,""+i.address)
        p.drawString(170,a,""+str(i.age))
        p.drawString(190,a,""+i.gender)
        p.drawString(220,a,""+str(i.course))
        p.drawString(330,a,""+i.batch_time)
        p.drawString(370,a,""+str(i.phone_no))
        p.drawString(460,a,""+i.email)
        a=a-25
    p.showPage()
    p.save()
    return response
def pdf_view(request):
    student=Attendences.objects.all()
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] ='attachment; filename="attendence.pdf"'
    p=canvas.Canvas(response)
    st={'student',student}
    p.setFont("Times-Roman",20)
    p.drawString(250,800,"ICS INDIA")
    p.setFont("Times-Roman",10)
    a=750
    for i in student:
        p.drawString(20,a,""+str(i.register_no))
        p.drawString(40,a,""+str(i.year))
        p.drawString(80,a,""+i.month)
        p.drawString(170,a,""+str(i.present))
        p.drawString(190,a,""+str(i.absent))
        total=(i.present+i.absent)
        p.drawString(250,a,""+str(total))
        a=a-25
    p.showPage()
    p.save()
    return response
def attend(request):
    attend=""
    form_1 = AttendForm()
    if request.method=='POST':
        month=request.POST['month']
        print(month)
        attend=Attendences.objects.filter(month=month)
        response=HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] ='attachment; filename="attendence.pdf"'
        p=canvas.Canvas(response)
        p.setFont("Times-Roman",20)
        p.drawString(250,800,"ICS INDIA")
        p.setFont("Times-Roman",10)
        a=750
        for i in attend:
            p.drawString(20,a,""+str(i.register_no))
            p.drawString(80,a,""+str(i.year))
            p.drawString(100,a,""+i.month)
            p.drawString(170,a,""+str(i.present))
            p.drawString(190,a,""+str(i.absent))
            total=(i.present+i.absent)
            p.drawString(250,a,""+str(total))
            a=a-25
        p.showPage()
        p.save()
        return response
    return render(request,'attend.html',{'form_1':form_1,'attend':attend})
