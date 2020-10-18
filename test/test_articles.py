import unittest
from app.models import Articles

class articlesTest(unittest.TestCase):
    """
    Test class to test the behaviour of the articles class
    """
    def setUp(self,articles):
        """
        set up method that will run before every Test
        """
        self.new_articles = articles()

    def test_instance(self,articles):
        self.assertTrue(isinstance(self.new_articles,articles))
