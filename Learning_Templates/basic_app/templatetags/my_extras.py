from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of 'arg' from the string!
    """
    return value.replace(arg, '')

#register.filter('cut', cut)
#('cut'= name by which you wanna call it in templates, cut=function name(i.e. above))