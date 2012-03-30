from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='openerp_pastertemplates',
      version=version,
      description="Paster template for creating new OpenERP modules",
      long_description="""\
""",
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
