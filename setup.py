from setuptools import setup, find_packages

setup(
    name='userdb',
    version='0.1.0',
    url="https://github.com/gauravr/userdb",
    classifiers=[
        'Programming Language :: Python',
        ],
    include_package_data=True,
    description='Helps to manage user sessions in python applications',
    long_description=open("README.rst").read(),
    packages=find_packages(),
    install_requires=[
        'redis'
      ],
    author='Shekhar Tiwatne',
    author_email='pythonic@gmail.com',
    license="http://www.opensource.org/licenses/mit-license.php",
    test_suite="tests",
    )

