import os
from setuptools import setup, find_packages

VERSION = '0.1a1'

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''
try:
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    CHANGES = ''

setup(name='kotti_jTweetAnywhere',
      version=VERSION,
      license='http://koansys.com/license.txt',

      install_requires=[
        'kotti',
      ],

      description="An addon that adds the jTweetsAnywhere widget to your Kotti site.",
      long_description='\n\n'.join([README, CHANGES]),
      keywords='twitter kotti cms pylons pyramid jTweetsAnywhere',


      author='Koansys, LLC',
      author_email='info@koansys.com',

      url='https://github.com/koansys/kotti_sitemap',

      packages=find_packages(),
      include_package_data=True,

      zip_safe=False,

      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
)
