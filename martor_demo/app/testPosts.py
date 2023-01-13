from django.test import TestCase
from app.models import Post


class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="My title", description="TP", wiki="post done")
        self.assertEqual(post.title, "My title")
        self.assertEqual(post.description, "TP")
        self.assertEqual(post.wiki, "post done")
