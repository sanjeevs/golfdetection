from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="golfdetection",
    version="0.0.1",
    description="Use open cv to detect critical elements in a golf swing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
    url="https://github.com/sanjeevs/golfdetect",
    author="Sanjeev Singh",
    author_email="snjvsingh123@gmail.com",
    entry_points={
        'console_scripts' : [
            'golfeditor=golfdetection.golfeditor:main',
            'merge_setup=golfdetection.merge_setup:main'
        ]
    },
    install_requires = ['opencv-python'],
    packages = ['golfdetection'],
    extras_require = {
        "dev": [
            "pytest >= 3.7",
            "check-manifest",
            "twine",
        ],
    }
)