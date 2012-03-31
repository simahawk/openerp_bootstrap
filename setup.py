from setuptools import setup, find_packages
import sys, os

version = '1.0a4'

def get_long_desc():
    toread = ['README.rst','HISTORY.txt']
    return '\n\n'.join([open(x).read() for x in toread])

setup(name='openerp_pastertemplates',
      version=version,
      description="Paster template for creating new OpenERP modules",
      long_description=get_long_desc(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='OpenERP paster',
      author='Simone Orsi',
      author_email='simahawk@gmail.com',
      url='',
      license='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'setuptools',
          'PasteScript',
          'Cheetah',
           # -*- Extra requirements: -*-
      ],

      entry_points="""
        # These will declare what templates paster create command can find
        # -*- Entry points: -*-
        [paste.paster_create_template]
        openerp_newmodule = openerp_pastertemplates.newmodule:NewModule
        """,
)
