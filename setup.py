import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
setup(
    name = 'visualiser',   
    packages = ['visualiser'],
    version = '0.8',
    license='MIT',
    description = 'A terminal visualiser.',
    long_description=README,
    long_description_content_type='text/markdown',
    author = 'possiblyhamzah',
    author_email = 'possiblyhamzah@gmail.com',
    url = 'https://github.com/probablyhamzah/visualiser',
    download_url = 'https://github.com/probablyhamzah/visualiser/archive/v_08.tar.gz',
    keywords = ['visualiser', 'terminal'],
    install_requires=[
            'librosa',
            'pydub',
            'numpy',
            'pygame',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)