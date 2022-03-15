# How to generate documentation

Documentation _rst_ files are generated first using the following command:

```
sphinx-apidoc -o . ../
```

To generate the _html_ documentation to the _\_build_ folder, run:

```
make html
```

Finally, clean up the _\_build_ folder, run:

```
make clean
```
