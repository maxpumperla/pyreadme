from setuptools import setup
from setuptools import find_packages

setup(
    name='pyreadme',
    version='0.1',
    packages=find_packages(),
    install_requires=['requests', 'click', 'argcomplete', 'python-frontmatter'],
    extras_require={
        'tests': ['pytest', 'pytest-pep8', 'pytest-cov']
    },
    include_package_data=True,
    license='MIT',
    description='Python interface for the readme.io HTTP API',
    url='https://github.com/maxpumperla/pyreadme',
    entry_points={
        'console_scripts': [
            'pyreadme=pyreadme.cli:handle'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: MIT Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ]
)
