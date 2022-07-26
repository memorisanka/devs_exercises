from ..functionality import is_prime


class TestIsPrime:
    def test_should_return_true_if_number_is_prime(self):
        assert is_prime(13) == True
        assert is_prime(2) == True
        assert is_prime(67) == True

    def test_should_return_false_if_number_is_not_prime(self):
        assert is_prime(1) == False
        assert is_prime(21) == False
        assert not is_prime(21) == True





