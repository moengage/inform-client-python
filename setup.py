from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='informclient',
    version='0.0.1',
    author='Mohammad Tarique Anjum',
    author_email='mohammad.anjum@moengage.com',
    description="This Python Package helps you in sending notifications through MoEngage Inform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/moengage/inform-client-python',
    project_urls={
            "Bug Tracker": "Package issues URL",
    },
    license='BSD 2-clause',
    install_requires=['StrEnum~=0.4.9',
                      'urllib3~=1.26.13',
                      'jsonschema~=4.17.3'
                      ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Customer Service',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
    ],
    package_dir={"": "moengage"},
    packages=find_packages(where="moengage"),
    python_requires=">=3.9"
)
