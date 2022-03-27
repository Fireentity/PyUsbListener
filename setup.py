from setuptools import setup, find_packages

setup(
    name='PyUsbListener',
    version='1.0.0',
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={
        "PyUsbListener": ["config/*.json"]
    },
    install_requires=["pyudev;python_version<'5.15.6'"],
    python_requires=">=3.8",
    url='',
    license='MIT',
    author='lorenzo',
    author_email='croceclaudio57@gmail.com',
    description='A simple usb listener in python',
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "PyUsbListener = PyUsbListener.main:start",
        ]
    }
)
