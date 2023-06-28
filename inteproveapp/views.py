
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Investor,User, Project,Updates
from django.http import HttpResponseRedirect
from django.db import connection

from .forms import LogInForm,RegisterForm,AddInvestorForm,AddUpdatesForm


# Create your views here.
from django.views import View

class Home(View):
    template = 'index.html'

    def get(self,request):
        return render(request, self.template)


class LogIn(View):
    template = 'login.html'

    def get(self,request):
        form = LogInForm()
        return render(request, self.template,{'form':form})

    def post(self,request):
        form = LogInForm(request.POST)
        uname = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.filter(username=uname,password=password).values()
        if not user:
            error = "Username or Password is incorrect."
            return render(request, self.template, {'form': form, 'error':error})
        else:
            type = user[0]['type']
            request.session['name'] = user[0]['username']
            request.session['type'] = type
            if type == 'S':
                return HttpResponseRedirect('/inteproveapp/supervisorView')
            elif type == 'R':
                return HttpResponseRedirect('/inteproveapp/researcherView')
            else:
                return HttpResponseRedirect('/inteproveapp/investorView')


class Register(View):
    template = 'register.html'

    def get(self,request):
        form = RegisterForm()
        return render(request,self.template,{'form':form})

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('inteproveapp:login'))
        return render(request,self.template,{'form':form})


class AddInvestor(View):
    template = 'addInvestor.html'

    def get(self,request):
        form = AddInvestorForm()
        return render(request, self.template, {'form': form})

    def post(self,request):
        form = AddInvestorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('inteproveapp:addInvestor'))
        return render(request,self.template,{'form':form})


class AddUpdates(View):
    template = 'addUpdates.html'

    def get(self,request):
        form = AddUpdatesForm()
        updates = Updates.objects.all()
        return render(request, self.template, {'form': form,'updates':updates})

    def post(self,request):
        form = AddUpdatesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('inteproveapp:addUpdates'))
        return render(request,self.template,{'form':form})

class ViewUpdates(View):
    template = 'viewUpdates.html'

    def get(self,request):
        updates = Updates.objects.all()
        return render(request, self.template, {'updates': updates})


class ViewProfile(View):
    template = 'viewProfiles.html'

    def get(self,request):
        name = User.objects.all()
        profiles = Investor.objects.filter(allocated='No')
        return render(request,self.template,{'profiles':profiles, 'name':name})

    def post(self,request):
        id = request.POST.get("id")
        pprofile = Investor.objects.get(pk=int(id))
        researcher_username = request.POST.get("researcher")
        Uname = User.objects.filter(username=researcher_username).first()
        projectname = "Tier 8"
        project = Project(projectname=projectname, investorprofileid=pprofile, username=Uname)
        project.save()
        pprofile.allocated='Yes'
        pprofile.save()
        return HttpResponseRedirect('/inteproveapp/viewProfile')



class ViewProject(View):
    template = 'viewProject.html'

    def get(self,request):
        profile = Investor.objects.filter(allocated='Yes')
        project = Project.objects.all()
        name = User.objects.all()
        return render(request, self.template, {'profile': profile, 'project': project, 'name':name})



class ViewAllocation(View):
    template = 'viewAllocation.html'

    def get(self, request):
        cursor = connection.cursor()
        try:
            print(request.session.get('name'))
            cursor.execute('call viewProject(%s)', {request.session.get('name')})
            results = cursor.fetchall()
        finally:
            cursor.close()
        return render(request,self.template,{'results':results})

    def post(self,request):
        id = request.POST.get("id")
        task = Investor.objects.get(pk=int(id))
        status = request.POST.get("status")
        task.status = status
        task.save()
        return HttpResponseRedirect('/inteproveapp/viewAllocation')


class UpdateProfile(View):
    template = 'updateProfile.html'

    def get(self, request, iid):
        uname = request.session.get('name')
        profilee = Investor.objects.get(pk=int(iid))
        investor = Investor.objects.filter(investorprofileid=int(iid))
        userLoggedIn = User.objects.filter(username=uname)
        userID = userLoggedIn[0]
        user = User.objects.get(pk=userID.username)
        return render(request, self.template, {'profilee': profilee, 'user': user,'investor':investor})

    def post(self,request,iid):
        idd = request.POST.get("idd")
        task = Investor.objects.get(pk=int(idd))
        profilename = request.POST.get("profilename")
        profiletype = request.POST.get("profiletype")
        aum = request.POST.get("aum")
        aa = request.POST.get("aa")
        actuary = request.POST.get("actuary")
        auditor = request.POST.get("auditor")
        custodian = request.POST.get("custodian")
        leadconsultant = request.POST.get("leadconsultant")
        mcontact = request.POST.get("mcontact")
        email = request.POST.get("email")
        task.profilename = profilename
        task.profiletype = profiletype
        task.aum = aum
        task.aa = aa
        task.actuary = actuary
        task.auditor = auditor
        task.custodian = custodian
        task.leadconsultant = leadconsultant
        task.mcontact = mcontact
        task.email = email
        task.save()
        return render(request, 'published.html')


class ResearcherView(View):
    template = 'researcherView.html'

    def get(self,request):
        if not request.session.get('name'):
            return HttpResponseRedirect('/inteproveapp/login')
        else:
            if request.session.get('type') == 'R':
                researcher = User.objects.get(username=request.session.get('name'))
                first_name = researcher.firstname
                last_name =  researcher.lastname
                return render(request, self.template, {'first_name': first_name,'last_name':last_name})
            else:
                return HttpResponseRedirect('/inteproveapp/login')

class SupervisorView(View):
    template = 'supervisorView.html'

    def get(self, request):
        if not request.session.get('name'):
            return HttpResponseRedirect('/inteproveapp/login')
        else:
            if request.session.get('type') == 'S':
                supervisor = User.objects.get(username=request.session.get('name'))
                first_name = supervisor.firstname
                last_name = supervisor.lastname
                return render(request, self.template, {'first_name': first_name,'last_name':last_name})
            else:
                return HttpResponseRedirect('/inteproveapp/login')

class InvestorView(View):
    template = 'investorView.html'

    def get(self,request):
        if not request.session.get('name'):
            return HttpResponseRedirect('/inteproveapp/login')
        else:
            if request.session.get('type') == 'I':
                investor = User.objects.get(username=request.session.get('name'))
                first_name = investor.firstname
                last_name = investor.lastname
                return render(request, self.template, {'first_name': first_name,'last_name':last_name})
            else:
                return HttpResponseRedirect('/inteproveapp/login')

class ViewInvestorProfile(View):
    template = 'viewInvestorProfile.html'

    def get(self,request):
        investor = Investor.objects.filter(status ='Completed')
        return render(request, self.template, {'investor':investor})

class InvestorProfile(View):
    template = 'investorProfile.html'

    def get(self,request,id):
            uname = request.session.get('name')
            iinvestor = Investor.objects.get(pk=int(id))
            investors = Investor.objects.filter(investorprofileid=int(id))
            userLoggedIn = User.objects.filter(username=uname)
            userID = userLoggedIn[0]
            user = User.objects.get(pk=userID.username)
            return render(request, self.template, {'iinvestor': iinvestor, 'user': user, 'investors': investors})


class SignOut(View):
    def get(self, request):
        del request.session['name']
        del request.session['type']
        return HttpResponseRedirect('/inteproveapp/login')

def delete(request, projectid):
    project = Project.objects.get(projectid=projectid)
    project.delete()
    return redirect('inteproveapp:viewProject')



