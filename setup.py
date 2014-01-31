from distutils.core import setup, Extension

module1 = Extension('rtest', sources = ['src/rtest.c'])

setup (name = 'RTest', version = '1.0', description = 'Optimized rtest',
       ext_modules = [module1])
       
