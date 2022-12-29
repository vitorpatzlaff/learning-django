from django.urls import reverse

from .test_recipe_base import RecipeTestBase


class PageIntTest(RecipeTestBase):
    def test_if_recipe_renders_when_page_is_not_int(self):
        self.make_recipe()

        response = self.client.get(reverse('recipes:home') + '?page=not-int')
        response_context_recipes = response.context['recipes']

        self.assertEqual(len(response_context_recipes), 1)
