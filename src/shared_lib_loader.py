import os
import sys
import platform
from ctypes import cdll, c_char, c_int, POINTER

SO_RELATIVE_PATH = 'go'


def load_signer_lib():
    lib_file = _get_signer_lib_filename()
    signer_lib = _load_lib(lib_file)
    _set_signer_lib_types(signer_lib)
    return signer_lib


def load_validator_lib():
    lib_file = _get_validator_lib_filename()
    validator_lib = _load_lib(lib_file)
    _set_validator_lib_types(validator_lib)
    return validator_lib


def _check_system_requirements():
    os_name = platform.system().lower()
    is_64bits = sys.maxsize > 2**32

    if not is_64bits:
        raise Exception('Only amd64 systems supported.')

    if os_name not in ['linux', 'windows', 'darwin']:
        raise Exception('Platform %s not supported.' % os_name)


def _load_lib(filename):
    _check_system_requirements()
    source_path = os.path.dirname(os.path.abspath(__file__))
    library_path = os.path.join(source_path, SO_RELATIVE_PATH, filename)
    return cdll.LoadLibrary(library_path)


def _get_signer_lib_filename():
    os_name = platform.system().lower()
    if os_name == 'linux':
        filename = 'signer-linux-amd64.so'
    elif os_name == 'darwin':
        filename = 'signer-darwin-10.11-amd64.dylib'
    else:
        filename = 'signer-windows-10.0-amd64.dll'
    return filename


def _get_validator_lib_filename():
    os_name = platform.system().lower()
    if os_name == 'linux':
        filename = 'validator-linux-amd64.so'
    elif os_name == 'darwin':
        filename = 'validator-darwin-10.11-amd64.dylib'
    else:
        filename = 'validator-windows-10.0-amd64.dll'
    return filename


def _set_signer_lib_types(signer_lib):
    signer_lib.SignURL.restype = POINTER(c_char)
    signer_lib.SignURL.argtypes = [
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char),
        c_int
    ]
    signer_lib.SignRequest.restype = POINTER(c_char)
    signer_lib.SignRequest.argtypes = [
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char)
    ]


def _set_validator_lib_types(go_validator):
    go_validator.ValidateRequest.restype = POINTER(c_char)
    go_validator.ValidateRequest.argtypes = [
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char)
    ]


def _set_validator_lib_types(go_validator):
    go_validator.ValidateRequest.restype = POINTER(c_char)
    go_validator.ValidateRequest.argtypes = [
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char)
    ]


def _set_validator_lib_types(go_validator):
    go_validator.ValidateRequest.restype = POINTER(c_char)
    go_validator.ValidateRequest.argtypes = [
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char)
    ]



def _set_validator_lib_types(go_validator):
    go_validator.ValidateRequest.restype = POINTER(c_char)
    go_validator.ValidateRequest.argtypes = [
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char),
        POINTER(c_char)
    ]
