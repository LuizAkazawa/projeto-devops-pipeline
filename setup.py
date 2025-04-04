from setuptools import setup, find_packages

setup(
    name="calculadora-devops",
    version="0.1.0",
    author="Luiz Akazawa",
    author_email="luizakazawa@outlook.com",
    description="Uma calculadora para demonstração de CI/CD",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)