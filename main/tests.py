from django.test import TestCase

# Create your tests here.
from .models import *

# Create your tests here.
class AwaardsTestClass(TestCase):

    def setUp(self):
        '''
        Set up the classes
        '''
        self.new_user = User(id = 1,first_name = 'James', last_name ='Muriuki', username = 'james12',email ='james@moringaschool.com')
        # self.new_user.save()


        self.new_project = Project(id = 1,title='today',image = 'tall.jpg', description = 'posted',link="www.welcome.com",user = self.new_user, created_at = '1999-09-08')
        # self.new_project.save()

        self.new_profile = Profile(id = 10, user = self.new_user, bio = 'New here',project = self.new_project,profile_photo='image.jpg',gender='male',contact="0733333333",updated ='1901-08-09' ,created_at = '1900-08-09')
        # self.new_profile.save()


        self.rate_review = Rate(id=1,user_id = self.new_user.id,design = 1,usability = 1,content = 1,reviewed_project = self.new_project)
        # self.rate_review.save()

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Project.objects.all().delete()
        Rate.objects.all().delete()

    def test_instance_profile(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_instance_project(self):
        self.assertTrue(isinstance(self.new_project,Project))

    def test_instance_rate(self):
        self.assertTrue(isinstance(self.rate_review,Rate))

    def test_save_project(self):
        self.new_project.save_project()
        project = Project.objects.all()
        self.assertTrue(len(project)==1)

    def test_save_profile(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)==1)

    def test_save_rate(self):
        self.rate_review.save_rate()
        rate = Rate.objects.all()
        self.assertTrue(len(rate)==1)

    def test_delete_project(self):
        self.new_project.delete_project()
        project = Project.objects.all()
        self.assertTrue(len(project)==0)

    def test_delete_profile(self):
        self.new_profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)==0)

    def test_delete_rate(self):
        self.rate_review.delete_rate()
        rate = Rate.objects.all()
        self.assertTrue(len(rate)==0)

    def test_update_profile(self):
        self.new_profile.save_profile()
        profile = Profile.objects.last().id
        Profile.update_profile(profile,'old here')
        update_profile = Profile.objects.get(id = profile)
        self.assertEqual(update_profile.bio,'old here')

    def test_update_project(self):
        self.new_project.save_project()
        project = Project.objects.last().id
        Project.update_project(project,'tomorrow')
        updated_profile = Project.objects.get(id = project)
        self.assertEqual(updated_profile.title,'tomorrow')

    def test_update_review(self):
        self.rate_review.save_rate()
        review = Rate.objects.last().id
        Rate.update_review(review,2)
        updated_review = Rate.objects.get(id = review)
        self.assertEqual(updated_review.design,2)

    def test_search_by_title(self):
        self.new_project.save_project()
        projects = Project.search_by_title('today')
        self.assertTrue(len(projects)== 1)

    


    




