from pyramid.renderers import render

from kotti.util import extract_from_settings
from kotti.views.slots import register
from kotti.views.slots import RenderRightSlot
from kotti.views.slots import RenderLeftSlot

PROFILE_WIDGET_DEFAULTS = {
    'username': 'koansys',
    'count': 10,
    'rate_warning': "To avoid struggling with Twitter's rate limit, we stop loading data after 10 API calls."
    }


def render_profile_widget(context, request, name=''):
    prefix = 'kms_twitter.profile_widget.'
    if name:
        prefix += name + '.'
    variables = PROFILE_WIDGET_DEFAULTS.copy()
    variables.update(extract_from_settings(prefix))
    return render('templates/profile_widget.pt', variables, request)


def include_profile_widget(config, where=RenderRightSlot):  # pragma: no cover
    config.add_static_view(name='static', path='kms_twitter:static')
    register(where, None, render_profile_widget)


def include_profile_widget_left(config):  # pragma: no cover
    include_profile_widget(config, RenderLeftSlot)
