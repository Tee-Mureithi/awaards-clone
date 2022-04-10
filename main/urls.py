from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, ProjectDetailView,DeleteProjectView,UpdateProjectView,EditProfileView,ProfileList,ProjectList
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.login_user,name='login_user'),
    path('register/',views.register_user,name='register'),
    path('logout/',views.logout_user,name='logout'),
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
    path('api-token-auth/', obtain_auth_token),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)