import queen
import unittest
class EightQueensTests(unittest.TestCase):
    def test(self, size=8):
        optimalFitness = 0
        bestFitness = queen.find_sequence(optimalFitness, size)
    
        self.assertTrue(not optimalFitness > bestFitness)
    
if __name__ == '__main__':
    unittest.main()