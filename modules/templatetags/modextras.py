from django import template

register = template.Library()

@register.filter(name="joinby")
def joinby(value):
   #print value.replace("'", "").strip('[').strip(']').split(',')
   return value.replace("'", "").strip('[').strip(']').split(',')

@register.filter(name="expandtrack")
def expandtrack(value):
   print "visible"
   print value
   return value