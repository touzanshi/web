from django.test import TestCase
from django.utils import timezone
from .models import Question
import datetime


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future(self):
        time = timezone.now() + datetime.timedelta(days=30)
        question = Question(pub_date=time)
        self.assertIs(question.was_published_recently(), False)

    def test_was_published_recently_with_old(self):
        time = timezone.now() + datetime.timedelta(days=1, seconds=1)
        question = Question(pub_date=time)
        self.assertIs(question.was_published_recently(), False)

    def test_was_published_recently_with_recent(self):
        time = timezone.now() + datetime.timedelta(hours=23, minutes=59, seconds=59)
        question = Question(pub_date=time)
        self.assertIs(question.was_published_recently(), False)
# Create your tests here.
