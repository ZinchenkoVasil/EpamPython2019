from Server.text.controllers import get_response

TEST_ACCOUNT_NAME = 'Vasia'
ASSERT_TEXT = 'Hello, Vasia'

def test_get_response():
    assert get_response(TEST_ACCOUNT_NAME) == ASSERT_TEXT