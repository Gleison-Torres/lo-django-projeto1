from django.test import TestCase
from django.urls import reverse, resolve
from home.views import index, search_recipe, recipe, category_recipe


class TestAppHomeUrls(TestCase):

    def test_home_url_is_correct(self):
        self.assertEqual(reverse('index'), '/')

    def test_search_url_is_correct(self):
        self.assertEqual(reverse('search'), '/recipe/search/')

    def test_recipe_url_is_correct(self):
        self.assertEqual(reverse('rec', kwargs={'pk': 1}), '/recipe/1/')

    def test_recipe_categories_url_is_correct(self):
        self.assertEqual(reverse('cat', kwargs={'pk': 1}), '/recipe/categories/1/')


class TestFunctionUrls(TestCase):

    def test_function_home_url_is_correct(self):
        view = resolve('/')
        self.assertIs(view.func, index)

    def test_function_search_url_is_correct(self):
        view = resolve('/recipe/search/')
        self.assertIs(view.func, search_recipe)

    def test_function_recipes_url_is_correct(self):
        view = resolve('/recipe/1/')
        self.assertIs(view.func, recipe)

    def test_function_categories_recipe_url_is_correct(self):
        view = resolve('/recipe/categories/1/')
        self.assertIs(view.func, category_recipe)


class TestStatusCodeUrl(TestCase):

    def test_url_home_status_code_200(self):
        url = self.client.get(reverse('index'))
        self.assertEqual(url.status_code, 200)

    def test_url_search_status_code_200_ok(self):
        url = self.client.get(reverse('search'))
        self.assertEqual(url.status_code, 200)
