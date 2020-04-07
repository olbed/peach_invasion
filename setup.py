import setuptools

with open('README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='peach_invasion',
    version='0.1.0',
    author='olbed',
    description='Peach invasion 2D game with pygame',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/olbed/peach_invasion',
    packages=setuptools.find_packages(),
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
