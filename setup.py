from setuptools import setup, find_packages


setup(
    name = 'rss_reader',
    version = '3.0',
    author = 'Vitali Herasimenia',
    author_email = 'SonkJeferson@gmail.com',
    packages = find_packages(),
    entry_points = {'console_scripts': ['rss-parser=rssparser.main:main'],}
)