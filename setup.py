from setuptools import setup

setup(
    name='covid19_certificate_pos',
    version='1.0',
    license='GPL v3',
    author="Emmanuel C",
    author_email="manuco@users.noreply.github.com",
    long_description=open('README.txt').read(),
    py_modules=["attestation"],
    install_requires=[
        "python-escpos >= 3.0a, < 3.1",
        "PyQt5 < 5.15",
    ]
)
