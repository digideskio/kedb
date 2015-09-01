#!/usr/bin/env python

from distutils.core import setup
import os
import setuplib

packages, package_data = setuplib.find_packages('kedb')

setup(name='Django-kedb',
    version=__import__('kedb').__version__,
    description='Django-based kedb middleware.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Ales Komarek',
    author_email='mail@newt.cz',
    url='http://newt.cz/',
    license='BSD License',
    platforms=['OS Independent'],
    packages=packages,
    package_data=package_data,
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audikedbe :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
)