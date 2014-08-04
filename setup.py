#!/bin/env python
# -*- coding: utf-8 -*-

'''Django package for DataTables:
able enhancing plug-in for the jQuery Javascript library'''

from setuptools import setup

setup(
    name='django-datatables',
    version='1.10.2',
    url='http://datatables.com',
    description=globals()['__doc__'],
    author='Jaime Pillora',
    maintainer='Renat Galimov',
    maintainer_email='renat2017@gmail.com',
    license='MIT License',
    keywords=['django', 'datatables'],
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['django_datatables'],
    package_data={'django_datatables': ['static/django_datatables/js/*',
                                        'static/django_datatables/css/*',
                                        'static/django_datatables/images/*',
                                        'static/django_datatables/bootstrap/3/*',
                                        'static/django_datatables/bootstrap/images/*',]}
)
