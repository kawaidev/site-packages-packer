from setuptools import setup, find_packages

setup(
    name="site-packages-packer",
    version="0.0.7",
    description="Pack selected packages from site-packages and output license file",
    author="kawaidev",
    author_email="kawai.dev.py@gmail.com",
    url="https://github.com/kawaidev/site-packages-packer",
    packages=find_packages(),
    install_requires=["pip-licenses~=3.3.0"],
    entry_points={
        "console_scripts": [
            "pack-site-packages = site_packages_packer.core:main",
        ]
    },
    license="MIT",
    python_requires=">=3.7",
)
