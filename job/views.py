from django.shortcuts import render,redirect,HttpResponseRedirect
from.models import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def admin_login(request):
    if request.method == 'POST':
        e = request.POST.get('email')
        p = request.POST.get('pwd')
        user = authenticate(request, username=e, password=p)
        if user is not None:
            login(request, user)
            return redirect('admin_home')
        else:
            return render(request, 'admin_home.html')

    return render(request, 'admin_login.html')


def user_login(request):
    if request.method == 'POST':
        e = request.POST.get('email')
        p = request.POST.get('pwd')
        user = authenticate(request, username=e, password=p)
        if user is not None:
            login(request, user)
            return redirect('user_home')
        else:
            return render(request, 'user_home.html')
    return render(request, 'user_login.html')


def recruiter_login(request):
    if request.method == 'POST':
        e = request.POST.get('email')
        p = request.POST.get('pwd')
        user = authenticate(request, username=e, password=p)
        if user is not None:
            login(request, user)
            data = Recruiter.objects.all()
            return redirect('recruiter_home',{'data':data})
        else:
            data = Recruiter.objects.all()
            return render(request, 'recruiter_home.html',{'data':data})
    return render(request, 'recruiter_login.html')


def recruiter_signup(request):
    if request.method == 'POST':
        f = request.POST['finame']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        gen = request.POST['gender']
        company = request.POST['company']
        user = Recruiter(finame=f, lname=l, image=i, pwd=p, email=e, contact=con, gender=gen, company=company)
        user.pwd = make_password(user.pwd)
        user.save()
        messages.success(request, "Signup Successfully")
    return render(request, 'recruiter_signup.html')


def Logout(request):
  logout(request)
  return redirect('index')


def user_home(request):
    if not request.user.is_authenticated:
        student = StudentUser.objects.all()
        d = {'student': student}
        return render(request, 'user_home.html', d)
    student = StudentUser.objects.all()
    d = {'student': student}
    return render(request, 'user_home.html', d)


def recruiter_home(request):
    if not request.user.is_authenticated:
        data = Recruiter.objects.all()
        d = {'data': data}
        return render(request, 'recruiter_home.html', d)
    data = Recruiter.objects.all()
    d = {'data': data}
    return render(request, 'recruiter_home.html', d)


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    rcount = Recruiter.objects.all().count()
    scount = StudentUser.objects.all().count()
    d = {'rcount':rcount,'scount':scount}
    return render(request, 'admin_home.html',d)





def user_signup(request):

   if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        gen = request.POST['gender']
        user = StudentUser(fname=f,lname=l,image=i,pwd=p,email=e,contact=con,gender=gen)
        user.pwd = make_password(user.pwd)
        user.save()
        messages.success(request, "Signup Successfully")
   return render(request, 'user_signup.html')


def view_users(request):
    if not request.user.is_authenticated:
        data = StudentUser.objects.all()
        d = {'data': data}
        return render(request, 'view_users.html',d)
    data = StudentUser.objects.all()
    d = {'data': data}
    return render(request, 'view_users.html',d)


def delete_user(request, pid):
    if not request.user.is_authenticated:
        student = StudentUser.objects.get(id=pid)
        student.delete()
        return redirect('view_recruiter')
    return render(request, 'admin_home.html')


def recruiter(request):
    if not request.user.is_authenticated:
        data = Recruiter.objects.all()
        d = {'data': data}
        return render(request, 'recruiter.html', d)
    data = Recruiter.objects.all()
    d = {'data': data}
    return render(request, 'recruiter.html', d)


def delete_recruiter(request, pid):
    if not request.user.is_authenticated:
        recruiter = Recruiter.objects.get(id=pid)
        recruiter.delete()
    return render(request, 'recruiter.html')


def change_passwordadmin(request):
   if not request.user.is_authenticated:
       return render(request, 'change_passwordadmin.html')
   if request.method == 'POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
   try:
        u = User.objects.get(id=request.user.id)
        if u.check_password(c):
            u.set_password(n)
            u.save()
   except:
       return render(request,'change_passwordadmin.html')


def change_passworduser(request):
   if not request.user.is_authenticated:
       return render(request, 'change_passworduser.html')
   if request.method == 'POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
   try:
        u = User.objects.get(id=request.user.id)
        if u.check_password(c):
            u.set_password(n)
            u.save()
   except:
       return render(request,'change_passworduser.html')


def change_passwordrecruiter(request):
   if not request.user.is_authenticated:
       return render(request, 'change_passwordrecruiter.html')
   if request.method == 'POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
   try:
        u = User.objects.get(id=request.user.id)
        if u.check_password(c):
            u.set_password(n)
            u.save()
   except:
       return render(request,'change_passwordrecruiter.html')


def add_job(request):
        if request.method == 'POST':
            jt = request.POST['jobtitle']
            sd = request.POST['sdate']
            ed = request.POST['edate']
            sal = request.POST['salary']
            cn = request.POST['cname']
            cl = request.FILES['image']
            exp = request.POST['experience']
            loc = request.POST['location']
            skills = request.POST['skills']
            des = request.POST['description']
            Job.objects.create(recruiter=recruiter,image=cl,cname = cn ,startdate=sd,enddate=ed,title=jt,salary=sal,description=des,location=loc,experience=exp,skills=skills,creationdate=date.today())
            messages.success(request, "Job Added Successfully")
        return render(request, 'add_job.html')


def job_list(request):
    if not request.user.is_authenticated:
        job = Job.objects.all()
        d = {'job': job}
        return render(request, 'job_list.html', d)
    job = Job.objects.all()
    d = {'job': job}
    return render(request, 'job_list.html', d)


def delete_job(request, pid):
    if not request.user.is_authenticated:
        job = Job.objects.get(id=pid)
        job.delete()
    return render(request, 'job_list.html')


def edit_jobdetail(request,pid):

    job = Job.objects.get(id=pid)

    if request.method == 'POST':
            jt = request.POST['jobtitle']
            sd = request.POST['startdate']
            ed = request.POST['enddate']
            sal = request.POST['salary']
            exp = request.POST['experience']
            loc = request.POST['location']
            skills = request.POST['skills']
            des = request.POST['description']

            job.title = jt
            job.salary = sal
            job.experience = exp
            job.location = loc
            job.skills = skills
            job.description = des
            job.save()

            if sd:
                try:
                    job.start_date = sd
                    job.save()
                except:

                 pass
            else:
                pass

            if ed:
                try:
                    job.end_date = ed
                    job.save()
                except:

                    pass
            else:
                pass
    d = {'job': job}
    return render(request, 'edit_jobdetail.html',d)






def change_companylogo(request,pid):

    job = Job.objects.get(id=pid)

    if request.method == 'POST':
            cl = request.FILES['image']

            job.image = cl

    try:
            job.save()
    except:
            pass

    d = {'job': job}
    return render(request, 'change_companylogo.html',d)


def latest_job(request):
    if not request.user.is_authenticated:
        data = Job.objects.all()
        i = Recruiter.objects.all()
        d = {'data': data,'i':i}
        return render(request, 'latest_job.html',d)
    data = Job.objects.all()
    i = Recruiter.objects.all()
    d = {'data': data, 'i':i}
    return render(request, 'latest_job.html',d)


def user_latestjobs(request):
     if not request.user.is_authenticated:
        data = Job.objects.all().order_by('-start_date')
        student = StudentUser.objects.get()
        datas = Apply.objects.filter(student=student)
        f = Recruiter.objects.all()
        li = []
        for i in datas:
            li.append(i.job.id)
        d = {'data': data, 'f': f, 'li': li}
        return render(request, 'user_latestjobs.html',d)
        data = Job.objects.all().order_by('-start_date')
        student = StudentUser.objects.get()
        datas = Apply.objects.filter(student=student)
        f = Recruiter.objects.all()
        li = []
        for i in datas:
            li.append(i.job.id)
        d =  {'data': data, 'f':f,'li':li}
        return render(request, 'user_latestjobs.html',d)

def job_detail(request):
    f = Recruiter.objects.all()
    job = Job.objects.all()
    d = {'f':f,'job':job}
    return render(request, 'job_detail.html', d)


def applyforjob(request):
    student = StudentUser.objects.get()
    job = Job.objects.get()
    date1 = date.today()
    if job.end_date < date1:
         messages.error(request,"Application line are close, last date is over")
    if job.start_date > date1:
         messages.add_message(request, messages.INFO, 'Application date are not open, Apply after 2 days')
    else:
        if request.method == 'POST':
          r = request.FILES['resume']
          Apply.objects.create(job=job, student=student,resume=r,applydate=date.today())
          messages.success(request,"Done")
    try:
        job.save()
        pass
    except:
            pass

    d = {}
    return render(request, 'applyforjob.html',d)


def applied_candidatelist(request):

    data1 = StudentUser.objects.all()
    data = Job.objects.all()
    f = Recruiter.objects.all()
    a = Apply.objects.all()
    d = {'data': data,'f':f,'data1':data1,'a':a}
    return render(request, 'applied_candidatelist.html',d)


def contact(request):
    return render(request, 'contact.html')


def admin_signup(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        p = request.POST['pwd']
        e = request.POST['email']
        admin = Admin(pwd=p, email=e, uname=uname)
        admin.pwd = make_password(admin.pwd)
        admin.save()
        messages.success(request, "Signup Successfully")
    return render(request, 'admin_signup.html')


def feedback(request):
    if request.method == 'POST':
        t = request.POST['text']
        s = Feedback(text=t)
        s.save()
    return render(request, 'index.html')