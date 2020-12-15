import setuptools

setuptools.setup(
    name="doctumentation_test",
    version="1.0",
    author="MNO",
    author_email="tim.bauer@supperundsupper.com",
    description="A small example package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=[
        "numpy",
        "matplotlib"
    ],
)
