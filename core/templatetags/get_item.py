"""
core.get_item templatetag to support rendering dict items by variable key name
"""
from core.templatetags import register


@register.filter
def get_item(dictionary, key):
    """
    Returns the item having the given key in the dictionary
    @param dictionary:
    @param key:
    @return:
    """
    return dictionary.get(key)
