from django.urls import path
from . import views
from .views import  DeleteProjectView,UpdateProjectView

app_name = "main"   


urlpatterns = [
  
    
    path("", views.register_request, name="register"),
    path("login", views.login_request, name="login"),

    path('post/',views.post_project,name='post_project'),
    path('project-detail/<int:id>',views.project_details, name='project_details'),
    path('edit_project/<int:pk>',UpdateProjectView.as_view(),name='update_project'),
    # path('review/<int:pk>',views.review_rate,name="review"),
    path('search/',views.search_for_project,name='search_term'),
    path('delete/<int:pk>',DeleteProjectView.as_view(),name="delete"),
    path('profile/<int:id>',views.my_profile,name='profile'),
]