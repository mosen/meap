from setuptools import setup, find_packages
setup(
    name="moeap",
    version="0.1",
    description="An EAPClient tool for 802.1x profiles",
    packages=find_packages(),
    author="mosen",
    license="MIT",
    url="https://github.com/mosen/moeap",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: MacOS X :: Cocoa',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='802.1x EAP macOS framework',
    # install_requires=[
    #     'pyobjc-core',
    #     'pyobjc-framework-Cocoa'
    # ],
    entry_points={
        'console_scripts': [
            'moeap=moeap.cli:main'
        ]
    }
)


