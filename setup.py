import setuptools

setuptools.setup(
    name="elum",
    version="0.0.0",
    url="https://github.com/carlosp420/elum",

    author="Carlos Pena",
    author_email="mycalesis@gmail.com",

    description="Take a blast output file and complete it with metadata if the subject sequences are found in NCBI genbank.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
