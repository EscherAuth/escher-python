# Escher - HTTP request signing lib

Python wrapper for the [Go implementation](https://github.com/EscherAuth/escher) of the [AWS4](http://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html) compatible [Escher](https://github.com/emartech/escher) HTTP request signing and authentication library.

## Installation

Via PIP:

```sh
pip install escherauth_go
```

## Usage

### Request Signing

```python
from escherauth_go.escher_signer import EscherSigner, EscherSignerError

try: 
    signer = EscherSigner('KEY', 'SECRET', 'credential/scope')
    signed_headers = signer.signRequest(
        'POST',
        '/test/path?param=test_query',
        'TEST BODY',
        {'Host': 'escherauth.io'})
except EscherSignerError as e:
    # Handle sign error
    print(e)
```

### URL Signing

```python
from escherauth_go.escher_signer import EscherSigner, EscherSignerError

try: 
    signer = EscherSigner('KEY', 'SECRET', 'credential/scope')
    signed_url = signer.signURL('GET', 'escherauth.io/specification.html?param=value')
except EscherSignerError as e:
    # Handle sign error
    print(e)
```

### Request Validation

```python
from escherauth_go.escher_validator import EscherValidator, EscherValidatorError

keyDB = [{
    'keyId': 'KEY',
    'secret': 'SECRET',
    'acceptOnly': 0
}]

try:
    validator = EscherValidator('credential/scope', keyDB)
    validated_key_id = validator.validateRequest(
        'POST',
        '/test/path?param=test_query',
        'TEST BODY',
        {'Host': 'escherauth.io', 'X-EMS-Date': '...', 'X-EMS-Auth': '...'}) # Signed headers
except EscherValidatorError as e:
    # Handle validation error
    print(e)
```

### URL Validation

```python
from escherauth_go.escher_validator import EscherValidator, EscherValidatorError

keyDB = [{
    'keyId': 'KEY',
    'secret': 'SECRET',
    'acceptOnly': 0
}]

try:
    validator = EscherValidator('credential/scope', keyDB)
    validated_key_id = validator.validateURL('GET', 'https://escherauth.io/specification.html?param=value&X-EMS-Date=...&X-EMS-Auth=...') # Signed URL
except EscherValidatorError as e:
    # Handle validation error
    print(e)
```