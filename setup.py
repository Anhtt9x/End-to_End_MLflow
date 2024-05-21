import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-to_End_MLflow"
AUTHOR_USER_NAME = "Anhtt9x"
SRC_REPO = "cnnClassifier"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    description="A small package for CNN app",
    author=AUTHOR_USER_NAME,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)