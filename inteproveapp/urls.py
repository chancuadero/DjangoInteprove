from . import views
from django.urls import path


app_name = 'inteproveapp'

urlpatterns =[
    path('', views.Home.as_view(), name='index'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('addInvestor/', views.AddInvestor.as_view(), name='addInvestor'),
    path('addUpdates/', views.AddUpdates.as_view(), name='addUpdates'),
    path('viewUpdates/', views.ViewUpdates.as_view(), name='viewUpdates'),
    path('viewProfile/', views.ViewProfile.as_view(), name='viewProfile'),
    path('viewAllocation/', views.ViewAllocation.as_view(), name='viewAllocation'),
    path('updateProfile/<int:iid>', views.UpdateProfile.as_view(), name='updateProfile'),
    path('updatedProfile/', views.UpdateProfile.as_view(), name='updatedProfile'),
    path('viewProject/', views.ViewProject.as_view(), name='viewProject'),
    path('researcherView/', views.ResearcherView.as_view(), name='researcherView'),
    path('supervisorView/', views.SupervisorView.as_view(), name='supervisorView'),
    path('investorView/', views.InvestorView.as_view(), name='investorView'),
    path('viewInvestorProfile/', views.ViewInvestorProfile.as_view(), name='viewInvestorProfile'),
    path('investorProfile/<int:id>', views.InvestorProfile.as_view(), name='investorProfile'),
    path('delete/<int:projectid>', views.delete, name='delete'),
    path('signOut/', views.SignOut.as_view(), name='signOut'),
]