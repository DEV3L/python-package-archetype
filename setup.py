from setuptools import setup, find_packages

setup(
    name='package_archetype',
    packages=find_packages(),
    version='0.4',
    description='A simple lib that prints out hello world',
    author='Justin Beall',
    author_email='jus.beall@gmail.com',
    url='https://github.com/DEV3L/python-package-archetype',
    download_url='https://github.com/DEV3L/python-package-archetype/tarball/0.4',
    keywords=['dev3l', 'archetype', 'pypi', 'package'],  # arbitrary keywords
    install_requires=[
        'pytest==2.9.2'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    entry_points={
        'console_scripts': [
            'hello_world = package_archetype.hello_world:print_hello_world'
        ]},
)
