from setuptools import setup

long_description = ''
with open('README.md', 'r') as fh:
    long_description += fh.read()

with open('LICENSE', 'r') as fh:
    long_description += fh.read()


setup(
    name='informclient',
    version='0.0.11rc7',
    author='MoEngage',
    author_email='support@moengage.com',
    description='This Python Package helps you in sending notifications through MoEngage Inform',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/moengage/inform-client-python',
    project_urls={
            'Bug Tracker': 'https://github.com/moengage/inform-client-python/issues',
    },
    install_requires=['StrEnum~=0.4.9',
                      'urllib3~=1.26.13',
                      'jsonschema~=4.17.3'
                      ],
    keywords=['MoEngage', 'Inform', 'MoEngage Inform', 'Customer Engagement', 'Transactional Alerts'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    py_modules=['informclient.informclient',
                'informclient.utils.api_description',
                'informclient.api.request.request_validator'],
    python_requires='>=3.9'
)
