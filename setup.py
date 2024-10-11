from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()
    
setup(
    name="wsi-brazillian-portuguese-tokenizer",
    version="0.1.0",
    packages=find_packages(),  
    install_requires=required, 
    author="waltersilva5",
    author_email="waltersilva5@outlook.com",
    description="",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/WalterSilva5/wsi-brazillian-portuguese-tokenizer",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  
)
