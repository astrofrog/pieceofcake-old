from setuptools import setup

entry_points = """
[console_scripts]
pieceofcake = pieceofcake.main:main
"""

setup(
    version='0.0.0',
    url="https://github.com/astrofrog/pieceofcake",
    name="pieceofcake",
    description='User-friendly wrapper around cookiecutter',
    packages=['pieceofcake'],
    install_requires=['requests', 'pygithub', 'click', 'colorama', 'cookiecutter', 'sphinx', 'numpydoc'],
    license='BSD',
    author='',
    author_email='',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points=entry_points
)
