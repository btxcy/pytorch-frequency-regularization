from setuptools import setup, find_packages

setup(
    name='frereglite',
    version='0.1.0',
    description='Frequency Regularization Python Package Lite',
    url='https://github.com/guanfangdong/pytorch-frequency-regularization',
    author='Zhao, Chenqiu and Dong, Guanfang and Zhang, Shupei and Tan, Zijie and Basu, Anup',
    packages=['frereglite'],
    license="Apache License 2.0",
    install_requires=['numpy',
                      'torch',
                      ],
    python_requires=">=3.8, <3.12",

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
