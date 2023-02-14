# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['foo', 'say_hello']

# %% ../nbs/00_core.ipynb 3
def foo(): pass

# %% ../nbs/00_core.ipynb 4
from fastcore.test import *

def say_hello(to):
    "Say hello to somebody"
    return f'Hello {to}!'

test_eq(say_hello('Isaac'), 'Hello Isaac!')
