from setuptools import setup,  find_packages
setup(
    name='pget',
    version='0.1',
    description='Downloader of files from the Web using tor implemented with \
    twisted and txsocksx.',
    author='duy',
    author_email='duy at rhizoma dot tk',
    url='https://github.com/duy/pget',
    install_requires=[
        'Twisted == 13.2',
        'txsocksx == 1.13.0.1',
    ],
    setup_requires=[],
    entry_points = {
        'console_scripts' : ['pget = scripts.pget:main']
    },

    keywords = 'python twisted txsockx tor download',
    license = 'GPLv3+',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Topic :: Utilities',
    ],
)
