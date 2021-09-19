"""
core.item_list to render a list of items in tabular format
"""
from core.templatetags import register


@register.inclusion_tag('core/item_list.html', takes_context=True)
def item_list(context, list_name):
    """
    Render a list of items in a tabular format
    @param context: dict containing context vars
    @param list_name: unique identifier for the list
    @return:
    """
    return {
        'items': context['list_items'][list_name],
        'headers': context['list_headers'][list_name],
    }
