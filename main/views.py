from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, PostProjectForm ,UpdateProjectForm,EditProfileForm,RateForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import Project,Profile,Rate 
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView
import statistics
from django.contrib.auth import authenticate,login



def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			# return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="auth/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request,data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				# return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="auth/login.html", context={"login_form":form})


def post_project(request):

    form = PostProjectForm()
    # current_user = request.user
    if request.method == 'POST':
        form = PostProjectForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    
        else:
            form = PostProjectForm()

    return render(request,'post_project.html',{"form":form})

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project-detail.html'



def project_detail(request,id):
    project = Project.objects.get(id=id)
    rate = Rate.objects.filter(reviewed_project = id).first() 

    context = {
        "object": project,
        "rate": rate,
    }

    return render(request,'project/project-detail.html',context)

def project_details(request,id):
    current_project = Project.objects.get(id=id)
    user = request.user
    user_rating = Rate.objects.filter(reviewed_project = id).all()

    design = Rate.objects.filter(reviewed_project=id).values_list('design',flat=True)
    usability = Rate.objects.filter(reviewed_project=id).values_list('usability',flat=True)
    content = Rate.objects.filter(reviewed_project=id).values_list('content',flat=True)

    if len(design)>0 and len(usability)>0 and len(content)>0:
        average_design = round(statistics.mean(design),1)
        average_usability = round(statistics.mean(usability),1)
        average_content = round(statistics.mean(content),1)

    else:
        average_design = 0
        average_usability = 0
        average_content = 0
    

    form = RateForm()
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.reviewed_project = current_project
            rate.user = user
            rate.save()

            return redirect(request.META.get('HTTP_REFERER'))


        else:
            form = RateForm()


    current_user = request.user

    context ={
        "object":current_project,
        "user":current_user,
        "form":form,
        "rates":user_rating,
        "design":design,
        "avg_design":average_design,
        "avg_usability":average_usability,
        "avg_content": average_content,
    }

    return render(request,'project/project-detail.html', context)



class ProfileUpdateView(UpdateView):
    models = Profile
    form_class = EditProfileForm
    template_name = 'profile/edit-profile.html'

    def get_queryset(self): 
        return Profile.objects.all()

class UpdateProjectView(UpdateView):
    model = Project
    form_class = UpdateProjectForm
    template_name = 'project/edit-project.html'

class DeleteProjectView(DeleteView):
    models = Project
    template_name = 'delete-project.html'
    success_url = reverse_lazy('home')

    def get_queryset(self): 
        return Project.objects.all()


def edit_profile(request,id):
    editing_profile = Profile.objects.get(id=id)
    form = EditProfileForm
    # current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = editing_profile.user.id
            post.save()
            return redirect(request.META.get('HTTP_REFERER'))

    return render(request,'profile/edit-profile.html',{"form":form})

def my_profile(request,id):
    user_profile = Profile.objects.get(user = id)
    # other_profile = Profile.objects.get(user = id)
    user_profile_projects = Project.objects.filter(user = id).all()

    current_user = request.user.id

    return render(request,'profile/profile.html', {"profile":user_profile,"projects":user_profile_projects,"current_user":current_user})

def search_for_project(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        search_results = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"results":search_results,"message":message})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})