from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def is_active(context, url_name):
    request = context["request"]
    return (
        "text-black"
        if request.resolver_match and request.resolver_match.url_name == url_name
        else "text-gray-500"
    )
