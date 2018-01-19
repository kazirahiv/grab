from django import template
import youtube_dl
register = template.Library()

@register.filter(name='get_title')
def get_title(dictionary):
    title  = dictionary['title']    
    return title
@register.filter(name='get_link')
def get_link(dictionary):
    link  = dictionary['link']    
    return link
