from pythonforandroid.recipe import CythonRecipe


class X13HashRecipe(CythonRecipe):

    url = ('https://files.pythonhosted.org/packages/63/f9/e102598fe45590ac7fab8bc0b473b1ebdb794fd580a227a497f1c6fb4f3f/sperocoin-x13-hash-{version}.tar.gz')
    md5sum = '4ca8356bb24f76f0c369bca64219626c'
    version = '1.0.5'
    depends = ['python3', 'setuptools']
    call_hostpython_via_targetpython = False


recipe = X13HashRecipe()
