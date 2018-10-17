from setuptools import setup

setup(
    name='escherauth-go',
    description='Python wrapper for the Go implementation of the AWS4 compatible Escher HTTP request signing protocol.',
    version='0.1.5',
    author='Istvan Szenasi',
    author_email='szeist@gmail.com',
    license='MIT',
    url='http://escherauth.io/',
    download_url='https://github.com/EscherAuth/escher-python',
    zip_safe=False,
    packages=['escherauth_go'],
    py_modules=['escherauth_go.escher_signer', 'escherauth_go.escher_validator'],
    package_data={
        'escherauth_go': ['*.so', '*.dylib']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: MacOS :: MacOS X',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)