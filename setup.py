from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in recruitment_app/__init__.py
from recruitment_app import __version__ as version

setup(
	name="recruitment_app",
	version=version,
	description="ujjwal kumar",
	author="ujjwal kumar",
	author_email="pathakujjwal93@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)