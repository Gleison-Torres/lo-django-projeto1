from django.core.paginator import Paginator


class PaginationRecipe:
    def __init__(self, paginator_recipes, page_number, additional_url=''):
        self.paginator_recipes = Paginator(paginator_recipes, 6)
        self.page_number = page_number
        self.show_p = 5
        self.additional_url = additional_url

    def make_pagination(self):
        if self.paginator_recipes.num_pages < 4:
            self.show_p = self.paginator_recipes.num_pages + 1

        if self.page_number is None or int(self.page_number) < 3:
            if self.page_number is None:
                show_pages = list(range(1, self.show_p))
                context = {
                    'page_object': self.paginator_recipes.get_page(self.page_number),
                    'range_page': show_pages,
                    'additional_url': self.additional_url
                }
                return context
            show_pages = list(range(1, self.show_p))
            context = {
                'page_object': self.paginator_recipes.get_page(self.page_number),
                'range_page': show_pages,
                'current_page': int(self.page_number),
                'additional_url': self.additional_url
            }
            return context
        show_pages = list(range(1, self.show_p))
        middle_range = round(len(show_pages) / 2)
        range_start = int(self.page_number) - middle_range
        range_end = int(self.page_number) + middle_range
        total_pages = list(self.paginator_recipes.page_range)

        if int(self.page_number) >= self.paginator_recipes.num_pages - 1:
            range_start = self.paginator_recipes.num_pages - 4
            context = {
                'page_object': self.paginator_recipes.get_page(self.page_number),
                'range_page': total_pages[range_start: range_end],
                'current_page': int(self.page_number),
                'additional_url': self.additional_url
            }

            return context

        context = {
            'page_object': self.paginator_recipes.get_page(self.page_number),
            'range_page': total_pages[range_start: range_end],
            'current_page': int(self.page_number),
            'additional_url': self.additional_url
        }

        return context
