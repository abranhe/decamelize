import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "decamelize",
    packages = ["decamelize"],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    version = "0.1.1",
    description = "🐍  Convert a camelized string into snake_case",
    author = "Carlos Abraham",
    author_email = "abraham@abranhe.com",
    url = "https://abranhe.com",
    classifiers=(
        "Programming Language :: Python",
        "Natural Language :: English",
        "Environment :: Plugins",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ),
    project_urls={
        'Source': 'https://github.com/abranhe/decamelize',
    },
)
