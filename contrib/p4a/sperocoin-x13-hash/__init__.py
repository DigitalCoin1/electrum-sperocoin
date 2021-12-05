from pythonforandroid.recipe import CythonRecipe


class X13HashRecipe(CythonRecipe):

    url = ('https://files.pythonhosted.org/packages/de/1a/77c05ebb8a160480d4a71d3c44eed10f6cae10a1639c27185d428329651c/sperocoin-x13-hash-{version}.tar.gz')
    md5sum = '4cd9816d8c071668e13958ecee7ae923'
    version = '1.0.6'
    depends = ['python3', 'setuptools']
    call_hostpython_via_targetpython = False


recipe = X13HashRecipe()
