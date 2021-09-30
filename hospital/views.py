from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
import reportlab.lib

from .utils import render_to_pdf #created in step 4
import datetime


def get(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    data = Discharge.objects.get(id=pid)
    data1 = User.objects.get(id=request.user.id)
    data2 = Profile.objects.filter(user=data1).first()
    template = get_template('invoice.html')
    data = {
        'today': datetime.date.today(),
        'data': data,
        'data2': data2,
    }
    html = template.render(data)
    pdf = render_to_pdf('invoice.html',data)
    return HttpResponse(pdf,content_type='application/pdf')

def get1(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    data = Testing.objects.get(id=pid)
    data1 = User.objects.get(id=request.user.id)
    data2 = Profile.objects.filter(user=data1).first()

    template = get_template('invoice1.html')
    data = {
        'today': datetime.date.today(),
        'data': data,
        'data2': data2,
    }
    html = template.render(data)
    pdf = render_to_pdf('invoice1.html',data)
    return HttpResponse(pdf,content_type='application/pdf')

def get2(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    data = Patient.objects.get(id=pid)
    data1 = User.objects.get(id=request.user.id)
    data2 = Profile.objects.filter(user=data1).first()
    template = get_template('invoice_patient.html')
    data = {
        'today': datetime.date.today(),
        'time': datetime.datetime.now(),
        'data': data,
        'data2': data2,
    }
    html = template.render(data)
    pdf = render_to_pdf('invoice_patient.html',data)
    return HttpResponse(pdf,content_type='application/pdf')


def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    stats = Stats.objects.all()
    d = {'stats': stats}
    return render(request, 'index.html', d)
def Dashboard(request):
    if not request.user.is_staff:
        return redirect('login')
    stats = Stats.objects.all()
    d = {'stats': stats}
    return render(request, 'front page.html', d)

def Login(request):
    error = False
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['psw']
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = True
    d = {'error': error}

    return render(request, 'login.html', d)

def Add_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    stats = Stats.objects.all()
    if request.method == "POST":
        n = request.POST['name']
        c = request.POST['contact']
        sp = request.POST['special']
        d = request.POST['day']
        t = request.POST['time']
        Doctor.objects.create(name=n, mobile=c, special=sp,o_time=t,o_days=d)
        count = 0
        for i in Doctor.objects.all():
            count += 1
        for j in Stats.objects.all():
            if j.stats_name == "doctor":
                j.stats_num = count
                j.save()
                return redirect('view_doctor')

    d = {'stats': stats}
    return render(request, 'doctor.html', d)

def Change_Profile(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    data = User.objects.get(id=pid)
    pro = Profile.objects.filter(user=data).first()
    if request.method == "POST":
        n = request.POST['direct']
        c = request.POST['mobile']
        a = request.POST['address']
        e = request.POST['email']
        m = request.POST['hospital']
        pro.h_name= n
        pro.contact= c
        pro.add= a
        pro.email= e
        pro.m_name= m
        pro.save()

    d = {'pro': pro}
    return render(request, 'profile.html', d)

def Add_Profile(request):
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST['direct']
        c = request.POST['mobile']
        a = request.POST['address']
        e = request.POST['email']
        m = request.POST['hospital']
        user1 = User.objects.get(id=request.user.id)
        Profile.objects.create(user=user1,h_name=n, contact=c, add=a,email=e,m_name=m)
        return redirect('profile',request.user.id)

    return render(request, 'add_profile.html')

def Delete_Doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    data = Doctor.objects.get(id=pid)
    data.delete()
    return redirect('view_doctor')


def view_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    stats = Stats.objects.all()
    doc = Doctor.objects.all()
    d = {'doc': doc, "stats": stats}
    return render(request, 'view_doctor.html', d)

def view_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    stats = Stats.objects.all()
    doc = Patient.objects.all()
    d = {'doc': doc, "stats": stats}
    return render(request, 'view_patient.html', d)

def Add_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    stats = Stats.objects.all()
    gen1 = Gender.objects.all()
    purp = Purpose.objects.all()
    if request.method == "POST":
        #s = request.POST['stats']
        n = request.POST['name']
        d = request.POST['disease']
        r = request.POST['relation']
        cn = request.POST['cnic']
        p = request.POST['payment']
        pu = request.POST['purpose']
        c = request.POST['contact']
        gen = request.POST['gen']
        add = request.POST['add']
        age = request.POST['age']
        #stat = Stats.objects.filter(stats_name=s).first()
        gender = Gender.objects.filter(type=gen).first()
        pur = Purpose.objects.filter(purpose=pu).first()
        put = Patient.objects.create(name=n, mobile=c, gender=gender, address=add,age=age,cnic=cn,payment=p,rel=r,disease=d,purpose=pur)
        if put:
            return redirect('get2',put.id)
        #if data:
            #stats.stats_num += 1
            #stats.save()
            #return redirect('home')
        #else:
            #pass
        count = 0
        for i in Patient.objects.all():
            count += 1
        for j in Stats.objects.all():
            if j.stats_name == "Patient":
                j.stats_num = count
                j.save()
                return redirect('view_patient')


    d = {'stats': stats, 'gen': gen1,'purpose':purp}
    return render(request, 'patient.html', d)

def Delete_Patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    data = Patient.objects.get(id=pid)
    data.delete()
    return redirect('view_patient')



def view_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    app = Appointment.objects.all()
    d = {'app': app}
    return render(request, 'view_appointment.html', d)

def Add_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    stats = Stats.objects.all()
    doc1 = Doctor.objects.all()
    pat1 = Patient.objects.all()
    if request.method == "POST":

        d = request.POST['doc']
        p = request.POST['pat']
        da = request.POST['date']
        ti = request.POST['time']

        doc = Doctor.objects.filter(name=d).first()
        pat = Patient.objects.filter(name=p).first()
        Appointment.objects.create(doctor=doc, patient=pat, date1=da, time1=ti)
        count = 0
        for i in Appointment.objects.all():
            count += 1
        for j in Stats.objects.all():
            if j.stats_name == "Appointment":
                j.stats_num = count
                j.save()
                return redirect('view_appointment')

    d = {'stats': stats, 'doc': doc1, 'pat': pat1}
    return render(request, 'appointment.html', d)

def Delete_Appointment(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    data = Appointment.objects.get(id=pid)
    data.delete()
    return redirect('view_appointment')


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def Edit_Patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    stats = Stats.objects.all()
    gen1 = Gender.objects.all()
    data = Patient.objects.get(id=pid)
    if request.method == "POST":
        #s = request.POST['stats']
        n = request.POST['name']
        d = request.POST['disease']
        r = request.POST['relation']
        cn = request.POST['cnic']
        p = request.POST['payment']
        pu = request.POST['purpose']
        c = request.POST['contact']
        gen = request.POST['gen']
        add = request.POST['add']
        #stat = Stats.objects.filter(stats_name=s).first()
        gender = Gender.objects.filter(type=gen).first()
        #data.stats = stat
        data.name = n
        data.disease = d
        data.purpose = pu
        data.payment = p
        data.rel = r
        data.gender = gender
        data.mobile = c
        data.address = add
        data.save()
        return redirect('view_patient')
    d = {'stats': stats, 'gen': gen1, 'data': data}
    return render(request, 'edit_patient.html', d)

def Edit_Doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    stats = Stats.objects.all()
    data = Doctor.objects.get(id=pid)
    if request.method == "POST":
        s = request.POST['stats']
        n = request.POST['name']
        c = request.POST['contact']
        sp = request.POST['special']
        d = request.POST['day']
        t = request.POST['time']
        stat = Stats.objects.filter(stats_name=s).first()
        data.stats = stat
        data.name = n
        data.mobile = c
        data.special = sp
        data.o_days = d
        data.o_time = t
        data.save()
        return redirect('view_doctor')

    d = {'stats': stats, 'data': data}
    return render(request, 'edit_doctor.html', d)

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
def discharge(request):
    if not request.user.is_staff:
        return redirect('login')
    pat=Patient.objects.all()
    doc1=Doctor.objects.all()
    if request.method=="POST":
        pid=request.POST['patient']
        pname=request.POST['name']
        d=request.POST['diseases']
        dd=request.POST['doctor']
        pay=request.POST['payment']
        out=request.POST['outstanding']
        da=datetime.date.today()
        ti=datetime.datetime.now()
        pat1=Patient.objects.filter(name=pname,id=pid).first()
        doc=Doctor.objects.filter(name=dd).first()
        dis = Discharge.objects.create(patient=pat1,doctor=doc,disease=d,payment_status=pay,remaining=out,date1=da,time1=ti)
        if dis:
            return redirect('get',dis.id)
    d = {'pat':pat,'doc':doc1}
    return render(request,'form.html',d)

def view_discharge(request):
    if not request.user.is_staff:
        return redirect('login')
    data=Discharge.objects.all()
    d={"data":data}
    return render(request,'view_discharge.html',d)
def delete_discharged(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    data=Discharge.objects.get(id=pid)
    data.delete()
    return redirect('view_discharge')

def Testing_lab(request):
    if not request.user.is_staff:
        return redirect('login')
    pat=Patient.objects.all()
    doc1=Doctor.objects.all()
    test=Test.objects.all()
    if request.method=="POST":
        pid=request.POST['payment1']
        doc=request.POST['doctor']
        t=request.POST['test']
        b=request.POST['group']
        dd=request.POST['date2']
        pay=request.POST['payment']
        d=request.POST['date1']
        tet = Test.objects.filter(id=t).first()
        pat1=Patient.objects.filter(id=pid).first()
        doc2=Doctor.objects.filter(name=doc).first()
        dis = Testing.objects.create(patient=pat1,doctor=doc2,payment=pay,delivery_date=dd,date1=d,b_group=b,test=tet)
        if dis:
            return redirect('get1',dis.id)
    d = {'pat':pat,'doc':doc1,'test':test}
    return render(request,'form2.html',d)

def view_tested(request):
    if not request.user.is_staff:
        return redirect('login')
    data=Testing.objects.all()
    d={"data":data}
    return render(request,'view_tested.html',d)
def delete_tested(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    data=Testing.objects.get(id=pid)
    data.delete()
    return redirect('view_tested1')
def test(request):
    if not request.user.is_staff:
        return redirect('login')
    if request.method=="POST":
        t1=0
        p1=0
        try:
            t=request.POST['test']
            if t:
                t1 = Test.objects.create(test=t)
        except:
            pass
        try:
            p=request.POST['purpose']
            if p:
                p1 = Purpose.objects.create(purpose=p)
        except:
            pass
        if t1:
            return redirect('view_test')
        if p1:
            return redirect('view_purpose')
    return render(request,'test.html')

def view_test(request):
    if not request.user.is_staff:
        return redirect('login')
    data=Test.objects.all()
    d = {'data':data}
    return render(request,'view_test.html',d)
def view_purpose(request):
    if not request.user.is_staff:
        return redirect('login')
    data=Purpose.objects.all()
    d = {'data':data}
    return render(request,'view_purpose.html',d)

def delete_test(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    data=Test.objects.get(id=pid)
    data.delete()
    return redirect('view_test')

def delete_purpose(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    data=Purpose.objects.get(id=pid)
    data.delete()
    return redirect('view_purpose')