from setuptools import setup, find_packages

setup(name='motmot.wxvalidatedtext',
      description='validated integer/float text entry field for wxPython',
      long_description = \
"""
This is a subpackage of the motmot family of digital image utilities.
""",
      author='Andrew Straw',
      author_email='strawman@astraw.com',
      license='BSD',
      url='http://code.astraw.com/projects/motmot',
      version='0.5.3', # sync with motmot/wxvalidatedtext/wxvalidatedtext.py
      zip_safe=True,

      namespace_packages = ['motmot'],
      packages = find_packages(),
      entry_points = {'gui_scripts': [
    'wxvalidatedtext_demo = motmot.wxvalidatedtext.demo:main',
    ]
                      },
      package_data = {'wxvalidatedtext_demo':['demo.xrc']},
      eager_resources = ['motmot/wxvalidatedtext/demo.xrc'],
      )
