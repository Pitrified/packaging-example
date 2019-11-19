# Deploy a package on PyPI

### Upload

Create the `dist` to upload

    python3 setup.py sdist bdist_wheel

Update it to the (test) index

    python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

Install the packageo

    python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps PACKAGE-NAME
