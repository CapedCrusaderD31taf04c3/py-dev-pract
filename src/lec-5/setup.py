from setuptools import setup, find_packages

setup(
    name='package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
    ],  # Add any dependencies your package needs
    author='Practice with anil',
    author_email='your@email.com',
    description='Description of your package',
    long_description=open('README.md').read(),  # Add README file if available
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/my_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
