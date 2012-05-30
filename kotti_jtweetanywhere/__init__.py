from pyramid.renderers import render

from kotti.util import extract_from_settings
from kotti.views.slots import register
from kotti.views.slots import RenderRightSlot
from kotti.views.slots import RenderLeftSlot
from kotti.views.slots import RenderBeforeBodyEnd
from kotti.views.slots import RenderInHead

PROFILE_WIDGET_DEFAULTS = {
    'username': 'koansys',
    'count': 10,
    'rate_warning': "To avoid struggling with Twitter's rate limit, we stop loading data after 10 API calls."
    }


def render_widget_assets(context, request, name=''):
    return render('templates/widget_assests.pt', request)


def render_profile_widget(context, request, name=''):
    return render('templates/profile_widget.pt', request)


def render_widget_javascript(context, request, name=''):
    prefix = 'kotti_jtweetanywhere.profile_widget.'
    if name:
        prefix += name + '.'
    variables = PROFILE_WIDGET_DEFAULTS.copy()
    variables.update(extract_from_settings(prefix))
    return render('templates/widget_javascript.pt', variables, request)


def include_profile_widget(config, where=RenderRightSlot):  # pragma: no cover
    config.add_static_view(name='static', path='kotti_jtweetanywhere:static')
    register(RenderInHead, None, render_widget_assets)
    register(where, None, render_profile_widget)
    register(RenderBeforeBodyEnd, None, render_widget_javascript)


def include_profile_widget_left(config):  # pragma: no cover
    include_profile_widget(config, RenderLeftSlot)
