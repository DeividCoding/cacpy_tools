import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cacpy_tools',
    version='0.0.2',
    author='Roni Hernandez',
    author_email='roni.hernandez.1999@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/RoniHernandez99/cacpy_tools',
    license='MIT',
    packages=['cacpy_tools'],
    install_requires=['numpy','matplotlib'],
)