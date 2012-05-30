from pyramid.threadlocal import get_current_registry
from kotti.tests import UnitTestBase

from kotti_jtweetanywhere import (render_widget_assets,
                                  render_profile_widget,
                                  render_widget_javascript)


def settings():
    return get_current_registry().settings


class TestAnalyticsWidget(UnitTestBase):
    def test_render_widget_assets(self):
        self.assert_(render_widget_assets(None, None).startswith('<!-- jTweetAnywhere'))

    def test_render_profile_widget(self):
        self.assert_(render_profile_widget(None, None).startswith('<div'))

    def test_render_widget_javascript(self):
        self.assert_(render_widget_javascript(None, None).startswith('<script'))

    def test_render_settings(self):
        html = render_widget_javascript(None, None)
        self.assert_(u"username: 'twitter_tester'," not in html)
        settings()['username'] = 'twitter_tester'
        html = render_widget_javascript(None, None)
        self.assert_(u"username: 'twitter_tester'," in html)
