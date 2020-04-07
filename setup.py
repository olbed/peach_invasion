from setuptools import setup

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='peach_invasion',
    packages=['peach_invasion'],
    version='0.0.1',
    author='olbed',
    description='Peach invasion 2D game with pygame',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/olbed/peach_invasion',
    include_package_data=True,
    install_requires=[
        'pygame>=1.9.6,<2',
    ],
    entry_points={
        'console_scripts': [
            'peach_invasion = peach_invasion.main:run',
        ],
    },
)
