from django.template import Library

register = Library()

@register.filter
def get_item(list, index):
    return list[index-1]