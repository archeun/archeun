"""core.mixins"""


class ArchItemListViewMixin:
    """
    A mixin to enable functionality related to item_list templatetag
    """
    list_headers = {}

    # pylint: disable=no-self-use
    def get_list_context_data(self):
        """
        Returns the context data for the item_list
        @return:
        """
        return {
            'list_headers': self.list_headers,
            'list_items': self.get_list_items(),
        }

    def get_list_items(self):
        """
        Returns the items for the list as an array
        @return:
        """
        return []
