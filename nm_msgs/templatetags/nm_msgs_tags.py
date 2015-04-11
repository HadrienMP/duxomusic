__author__ = 'hadrien'
from django import template


register = template.Library()


@register.assignment_tag(takes_context=True)
def nm_msgs(context, namespace=None):
    return __get_nm_msgs(context, namespace=namespace).get('categories', None)


@register.assignment_tag(takes_context=True)
def nm_success(context, namespace=None):
    return __get_nm_msgs(context, namespace=namespace, p_level='success').get('messages', None)


@register.assignment_tag(takes_context=True)
def nm_warnings(context, namespace=None):
    return __get_nm_msgs(context, namespace=namespace, p_level='warning').get('messages', None)


@register.inclusion_tag('nm_msgs/main.html', takes_context=True)
def nm_msgs_display(context, namespace=None):
    return __get_nm_msgs(context, namespace=namespace)


def __get_nm_msgs(context, namespace=None, p_level=None):
    # {u'newsletter': {u'info': [u'Message']}}
    request = context['request']
    session = request.session
    namespaces = session.get('namespaced_messages')
    categories = dict()

    if namespaces:
        if namespace and namespace in namespaces.keys():
            categories = namespaces[namespace]
            del session['namespaced_messages'][namespace]
            session.modified = True
        else:
            for key, levels in namespaces.items():
                for level, messages in levels.items():
                    levels = categories.get(level, list())
                    levels.extend(messages)
                    categories[level] = levels

            del session['namespaced_messages']

    return {
        'categories': categories,
        'messages': categories.get(p_level, list()),
    }