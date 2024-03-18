from esteem import calculate_steem_messure
import pytest

answers = ['A','A','D','a','d','a','a','a','a', 'd']

def test_calculate_steem_messure():
    assert calculate_steem_messure(answers) == 21

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])