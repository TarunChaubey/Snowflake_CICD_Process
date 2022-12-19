from setuptools import setup


## edit below variables as per your requirements -
REPO_NAME = "Snowflake CI CD pileline Sample"
AUTHOR_USER_NAME = "TarunChaubey"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Snowflake usecase",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="tarunchaubey09@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.6",
    install_requires=LIST_OF_REQUIREMENTS
)