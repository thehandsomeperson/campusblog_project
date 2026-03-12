from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.
class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='the_super_hero', password='the_best_hero')

    #This test is used for test whether we can create the object successfully
    def test_post_creation(self):
        post = Post.objects.create(author=self.user, title='title_test', content='content_test', status='published')
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.title, 'title_test')
        self.assertEqual(post.content, 'content_test')

    #This test is used for test whether the post list page can be load successfully
    def test_post_list_view(self):
        posts = self.client.get('/')
        self.assertEqual(posts.status_code, 200)

    #This test is used for test whether unauthorized users will be redirected to login page
    def test_create_post_requires_login(self):
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 302)

