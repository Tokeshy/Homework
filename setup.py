from setuptools import setup, find_packages


setup(
    name = 'rss_reader',
    version = '2.0',
    author = 'Vitali Herasimenia',
    author_email = 'NoMatter',
    packages = find_packages(),
    entry_points = {'console_scripts': ['rss-parser=rssparser.main:main'],}
)