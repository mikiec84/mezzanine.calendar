from setuptools import setup, find_packages
import sys, os

version = '0.0.2'

setup(name='mezzanine-calendar',
    version=version,
    description="A Django Mezzanine Calendar App",
    long_description="""""",
    classifiers=[],
    keywords='',
    author='Aleksandr Vladimirskiy',
    author_email='sasha@butchershop.co',
    url='http://www.butchershop.co',
    license='BSD',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)

