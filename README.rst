====================
kotti_jTweetAnywhere
====================

This is an extension to the Kotti CMS that allows you to add jTweetsAnywhere
widget to your Kotti site.

`Find out more about Kotti`_

Setting up the widget
=====================

To set up the profile widget to display on every page in Kotti on the
right hand side, add ``kotti_jTweetAnywhere.include_profile_widget`` to the
``kotti.includes`` setting in your Paste Deploy config::

  kotti.includes = kotti_jTweetAnywhere.include_profile_widget

To set the name of the user for which the widget is shown, set the
``kotti_jTweetAnywhere.profile_widget.user`` variable.  An example with some
other variables::

  kotti.includes = kotti_jTweetAnywhere.include_profile_widget
  kotti_jTweetAnywhere.profile_widget.user = koansys

.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti