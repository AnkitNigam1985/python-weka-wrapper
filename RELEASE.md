PyPi
====

Preparation:
* run unit tests: `tests/wekatests/all_tests.py`
* increment version in `setup.py`
* increment versions/copyright in `doc/source/conf.py`
* update API documentation
  * cd python/weka
  * sphinx-apidoc -f -o ../../doc/source .
  * make sure that all modules are included in `index.rst` (apart from `modules.rst`)
* add new changelog section in `CHANGES.rst`
* commit/push all changes

Commands for releasing on pypi.org (requires twine >= 1.8.0):

```
find -name "*~" -delete
rm dist/*
python setup.py clean
python setup.py sdist
./venv/bin/twine upload dist/*
```

Commands for updating github pages:

```
find -name "*~" -delete
cd doc
make html
cd build/html
cp -R * ../../../../python-weka-wrapper.gh-pages/
cd ../../../../python-weka-wrapper.gh-pages/
git pull origin gh-pages
git add -A
git commit -a -m "updated documentation"
git rebase gh-pages
git push origin gh-pages
```


Github
======

Steps:
* start new release (version: `vX.Y.Z`)
* enter release notes, i.e., significant changes since last release
* upload `python-weka-wrapper-X.Y.Z.tar.gz` previously generated with `setyp.py`
* publish


MLOSS
=====

Steps:
* login
* goto project page https://mloss.org/software/view/548/
* click on `Update project`
* update `Version` and `Download URL`
* re-use release notes from Github release in `Changes since last revision`
* save


Google Group
============

* post release on the Google Group: https://groups.google.com/forum/#!forum/python-weka-wrapper
