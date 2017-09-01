import sys
import logging
from escherauth_go.escher_validator import EscherValidator
from escherauth_go.escher_signer import EscherSigner

API_KEY = 'suite_user-management_v1'
API_SECRET = 'eCuHbyzLCem7UMBzpYo700mpS7QCBoRY'
TEST_URL = 'https://escherauth.io/specification.html?param=value'
TEST_URL_PATH_QUERY = '/specification.html?param=value'
TEST_BODY = 'TEST BODY'

keyDB = [{
    'keyId': API_KEY,
    'secret': API_SECRET,
    'acceptOnly': 0
}]


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()

signer = EscherSigner(API_KEY, API_SECRET, 'eu/suite/ems_request')
validator = EscherValidator('eu/suite/ems_request', keyDB)

logger.info('URL Signing test')
signed_url = signer.signURL('GET', TEST_URL)
signed_url_result = validator.validateURL('GET', signed_url)
assert signed_url_result == API_KEY
logger.info('PASS')

logger.info('Request Signing test')
signed_headers = signer.signRequest(
    'POST',
    TEST_URL_PATH_QUERY,
    TEST_BODY,
    {'Host': 'escherauth.io'})
signed_request_result = validator.validateRequest(
    'POST',
    TEST_URL_PATH_QUERY,
    TEST_BODY,
    signed_headers)
assert signed_request_result == API_KEY
logger.info('PASS')
