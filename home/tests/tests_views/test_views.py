from django.test import TestCase
from home.models import Category, Recipe, User
from django.urls import reverse


class ViewsTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Massa')

        self.author = User.objects.create_user(
            first_name='User',
            last_name='Teste',
            username='Teste20',
            email='teste@teste.com',
            password='Teste@123'
        )

        self.recipe = Recipe.objects.create(
            author=self.author,
            title='Macarrão Teste',
            description='Descrição da receita',
            time_recipe=60,
            order=20,
            step='Passo-a-passo da receita',
            recipe_category=self.category,
            active=True
        )

    def test_recipe_home_templates_loads_ok(self):
        response = self.client.get(reverse('index'))

        self.assertIn(self.recipe.title, response.content.decode('utf-8'))

    def test_recipe_not_found_if_not_recipe(self):
        Recipe.objects.get(id=1).delete()
        response = self.client.get(reverse('index'))
        self.assertIn('Não temos receitas cadastradas!', response.content.decode('utf-8'))



    #print(f'\033[7;35;40m Variavel View =====>>> {dir()} \033[m')




