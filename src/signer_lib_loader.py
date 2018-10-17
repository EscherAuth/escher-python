import os
import sys
import platform
from ctypes import cdll, c_char, c_int, POINTER

SO_RELATIVE_PATH = 'go'

def load_signer_lib():
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
        filename = 'signer-linux-amd64.so'
    elif os_name == 'darwin':
        filename = 'signer-darwin-10.11-amd64.dylib'
    else:
        filename = 'signer-windows-10.0-amd64.dll'
    return filename


def _set_lib_types(go_signer):
    go_signer.SignURL.restype = POINTER(c_char)
    go_signer.SignURL.argtypes = [
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char),
        c_int
    ]

    go_signer.SignRequest.restype = POINTER(c_char)
    go_signer.SignRequest.argtypes = [
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char)
    ]
