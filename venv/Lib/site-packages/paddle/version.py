# THIS FILE IS GENERATED FROM PADDLEPADDLE SETUP.PY
#
full_version    = '1.8.3'
major           = '1'
minor           = '8'
patch           = '3'
rc              = '0'
istaged         = True
commit          = 'a44085bed80d72296118f3e97516bef340baf3aa'
with_mkl        = 'ON'

def show():
    if istaged:
        print('full_version:', full_version)
        print('major:', major)
        print('minor:', minor)
        print('patch:', patch)
        print('rc:', rc)
    else:
        print('commit:', commit)

def mkl():
    return with_mkl
