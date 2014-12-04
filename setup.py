# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'waitress',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'couchdbkit',
    'filemagic',
]

setup(
    name='paulla.fish',
    version='0.0',
    description='paulla.fish',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
    author=u'',
    author_email='',
    url='',
    keywords='file sharing pyramid',
    packages=find_packages(),
    include_package_data=True,
    namespace_packages=['paulla'],
    zip_safe=False,
    install_requires=requires,
    tests_require=requires,
    test_suite="paulla.fish",
    entry_points="""\
    [paste.app_factory]
    main = paulla.fish:main
    [console_scripts]
    migration = paulla.fish.utils:migration
    """,
)
