import os
import sys
import platform
from ctypes import cdll, c_char, POINTER

SO_RELATIVE_PATH = 'go'

def load_validator_lib():
    _check_system_requirements()
    lib_file = _get_lib_filename()
    return _load_lib(lib_file)

def _check_system_requirements():
    os_name = platform.system().lower()
    is_64bits = sys.maxsize > 2**32

    if not is_64bits:
        raise Exception('Only amd64 systems supported.')

    if os_name not in ['linux', 'windows', 'darwin']:
        raise Exception('Platform %s not supported.' % os_name)


def _load_lib(filename):
    source_path = os.path.dirname(os.path.abspath(__file__))
    library_path = os.path.join(source_path, SO_RELATIVE_PATH, filename)
    go_signer = cdll.LoadLibrary(library_path)

    _set_lib_types(go_signer)

    return go_signer


def _get_lib_filename():
    os_name = platform.system().lower()
    if os_name == 'linux':
        filename = 'validator-linux-amd64.so'
    elif os_name == 'darwin':
        filename = 'validator-darwin-10.11-amd64.dylib'
    else:
        filename = 'validator-windows-10.0-amd64.dll'
    return filename


def _set_lib_types(go_validator):
    go_validator.ValidateRequest.restype = POINTER(c_char)
    go_validator.ValidateRequest.argtypes = [
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char)
    ]
