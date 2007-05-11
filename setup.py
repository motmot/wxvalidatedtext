from setuptools import setup

import os, sys
import motmot_utils

from motmot_utils import get_svnversion_persistent
version_str = '0.4.dev%(svnversion)s'
version = get_svnversion_persistent(
    os.path.join('wxvalidatedtext','version.py'),
    version_str)

setup(name='wxvalidatedtext',
      description='validated integer/float text entry field for wxPython',
      author='Andrew Straw',
      author_email='strawman@astraw.com',
      license='BSD',
      version=version,
      zip_safe=True,
      
      packages = ['wxvalidatedtext'],
      entry_points = {'gui_scripts': [
    'wxvalidatedtext_demo = wxvalidatedtext.demo:main',
    ]
                      },
      package_data = {'wxvalidatedtext_demo':['demo.xrc']},
      eager_resources = ['wxvalidatedtext/demo.xrc'],
      )
