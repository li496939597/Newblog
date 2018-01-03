from ..models import Post
from django import template

register = tempalte.Library()
@register.simple_tag
def get_recent_posts(num=8):
    return Post.objects.all().order_by('-created_time')[:num]