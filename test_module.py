import unittest
import mean_var_std


# the test case
class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = mean_var_std.calculate([2,6,2,8,4,0,1,5,7])
        expected = {'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889], 'variance': [[9.555555555555557, 0.6666666666666666, 8.666666666666666], [3.555555555555556, 10.666666666666666, 6.222222222222221], 6.987654320987654], 'standard deviation': [[3.091206165165235, 0.816496580927726, 2.943920288775949], [1.8856180831641267, 3.265986323710904, 2.494438257849294], 2.6434171674156266]}
        self.assertEqual(actual, expected, "Expected different output when calling 'calculate()' with '[0,1,2,3,4,5,6,7,8]'")
    
    def test_calculate_with_few_digits(self):
        actual = mean_var_std.calculate([2,6,2,8,4,0,1,])
        expected = "List must contain nine numbers."
        self.assertEqual(actual, expected, "Expected calling 'calculate()' with a list of NOT length nine to return 'List must contain nine numbers.'")

if __name__ == "__main__":
    unittest.main()