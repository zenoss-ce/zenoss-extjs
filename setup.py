from setuptools import setup, find_packages

DESCRIPTION = "A Zope package providing ExtJS as a browser resource"
version = '4.1.3'

setup(name='zenoss.extjs',
      version=version,
      description=DESCRIPTION,
      long_description=DESCRIPTION,
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Zenoss, Inc.',
      author_email='dev@zenoss.com',
      url='http://www.zenoss.com',
      license='GPLv3 with FOSS Exception for Applications',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['zenoss'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools'],
      entry_points="",
      )
