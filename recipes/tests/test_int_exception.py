from unittest.mock import patch

from django.urls import reverse

from .test_recipe_base import RecipeTestBase


class PageIntTest(RecipeTestBase):
    def test_if_recipe_renders_when_page_is_not_int(self):
        self.make_recipe_in_batch(8)

        with patch('recipes.views.site.PER_PAGE', new=3):
            response = self.client.get(reverse('recipes:home') + '?page=2')
            self.assertEqual(response.context['recipes'].number, 2)

            response = self.client.get(reverse('recipes:home') + '?page=not-int')
            self.assertEqual(response.context['recipes'].number, 1)
