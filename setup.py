from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='0.0.1',
    description='A simple library to perform emotion detection on text.',
    author='<Your Name>',
    author_email='<Your Email>',
    packages=find_packages(),
    install_requires=[
        'requests'  # Add any other dependencies your package needs
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)