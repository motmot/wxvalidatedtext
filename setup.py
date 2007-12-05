from setuptools import setup

import os, sys

setup(name='wxvalidatedtext',
      description='validated integer/float text entry field for wxPython',
      author='Andrew Straw',
      author_email='strawman@astraw.com',
      license='BSD',
      version='0.5.1', # keep in sync with wxvalidatedtext/wxvalidatedtext.py
      zip_safe=True,

      packages = ['wxvalidatedtext'],
      entry_points = {'gui_scripts': [
    'wxvalidatedtext_demo = wxvalidatedtext.demo:main',
    ]
                      },
      package_data = {'wxvalidatedtext_demo':['demo.xrc']},
      eager_resources = ['wxvalidatedtext/demo.xrc'],
      )
