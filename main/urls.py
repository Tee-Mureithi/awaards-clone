from django.urls import path
from . import views
from .views import HomeView, ProjectDetailView,DeleteProjectView,UpdateProjectView,EditProfileView,ProfileList,ProjectList
app_name = "main"   


urlpatterns = [
    # path("", views.homepage, name="homepage"),
    
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path('home/',HomeView.as_view(), name='home'),
    path('post/',views.post_project,name='post_project'),
    path('project-detail/<int:id>',views.project_details, name='project_details'),
    path('edit_project/<int:pk>',UpdateProjectView.as_view(),name='update_project'),
    # path('review/<int:pk>',views.review_rate,name="review"),
    path('search/',views.search_for_project,name='search_term'),
    path('delete/<int:pk>',DeleteProjectView.as_view(),name="delete"),
    path('profile/<int:id>',views.my_profile,name='profile'),
    path('edit-profile/<int:pk>',EditProfileView.as_view(),name='edit_profile'),
    path('api/profile/',ProfileList.as_view(), name='all_profiles'),
    path('api/projects/',ProjectList.as_view(), name='all_profiles'),
]