from setuptools import setup

import sys, os

with open('README.txt') as f:
    long_description = f.read()

setup(
    name="urlmap",
    version='0.1',
    description="""WSGI application dispatching calls to other WSGI applications""",
    long_description=long_description,

    classifiers=[
      "Development Status :: 2 - Pre-Alpha",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: MIT License",
      "Programming Language :: Python",
      "Programming Language :: Python 3.2",
      "Topic :: Internet :: WWW/HTTP",
      "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
      "Topic :: Software Development :: Libraries :: Python Modules",
      "Topic :: Internet :: WWW/HTTP :: WSGI",
      "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
      ],
    entry_points = """
      [paste.composite_factory]
      main = urlmap:urlmap_factory
    """,
    keywords='web application server wsgi',
    author="Szymon Pyżalski",
    author_email="szymon@pythonista.net",
    url="http://pythonpaste.org",
    package_dir = {'': 'src'},
    license="MIT",
    packages=['urlmap'],
    zip_safe=True,
    test_suite='nose.collector',
    tests_require=['nose>=0.11', 'WebTest>=1.3.3', 'PasteDeploy'],
)
