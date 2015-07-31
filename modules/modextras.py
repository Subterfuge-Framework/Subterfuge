from django import template

register = template.Library()

def joinby(value, arg):
   return arg.join(value)
