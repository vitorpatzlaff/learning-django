from unittest.mock import patch

from django.urls import reverse

from .test_recipe_base import RecipeTestBase


class PageIntTest(RecipeTestBase):
    def test_if_recipe_renders_when_page_is_not_int(self):
        for i in range(8):
            kwargs = {'author_data': None, 'slug': f'r{i}'}
            self.make_recipe(**kwargs)

        with patch('recipes.views.PER_PAGE', new=3):
            response = self.client.get(reverse('recipes:home') + '?page=2')
            self.assertEqual(response.context['recipes'].number, 2)

            response = self.client.get(reverse('recipes:home') + '?page=not-int')
            self.assertEqual(response.context['recipes'].number, 1)
