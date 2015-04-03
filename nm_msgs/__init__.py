__author__ = 'hadrien'
'''Utils to add simplistic flash messages to the session in a namespace'''


def info(*args, **kwargs):
    __add_message(level='info', *args, **kwargs)


def error(*args, **kwargs):
    __add_message(level='error', *args, **kwargs)


def success(*args, **kwargs):
    __add_message(level='success', *args, **kwargs)


def warning(*args, **kwargs):
    __add_message(level='warning', *args, **kwargs)


def __add_message(request, message=None, namespace='default', level='info', messages=None):
    if message or messages:

        if message:
            _messages = [message]
        else:
            _messages = messages

        if 'namespaced_messages' not in request.session or not request.session['namespaced_messages']:
            request.session['namespaced_messages'] = {namespace: {level: _messages}}
        else:
            namespaces = request.session['namespaced_messages']
            levels = namespaces.get(namespace, {level: list()})
            _level = levels.get(level, list())
            _level.extend(_messages)
            levels[level] = _level

            namespaces[namespace] = levels
            request.session['namespaced_messages'] = namespaces

        request.session.modified = True