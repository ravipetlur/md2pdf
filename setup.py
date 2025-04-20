from setuptools import setup, find_packages

setup(
    name="md2pdf",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==3.0.2',
        'markdown2==2.4.12',
        'weasyprint==60.1',
        'python-docx==1.1.0',
        'markdown==3.5.2',
        'pydyf==0.8.0',
        'beautifulsoup4==4.12.3',
    ],
    entry_points={
        'console_scripts': [
            'md2pdf=cli:main',
        ],
    },
    author="Ravi Petlur",
    author_email="ravipetlur@gmail.com",
    description="A tool to convert Markdown files to PDF or DOCX",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ravipetlur/md2pdf",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
) 