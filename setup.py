import setuptools

long_description="""
A ZMQ-based RPC tool-kit with built-in HTTP support for instrument control/data acquisition
or controlling generic python objects.
"""

setuptools.setup(
    name="hololinked-examples",
    version="0.1.0",
    author="Vignesh Vaidyanathan",
    author_email="vignesh.vaidyanathan@hololinked.dev",
    description="examples for hololinked, installed under folder name",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=['oceanoptics_spectrometer'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],    
    python_requires='>=3.7',
)
 