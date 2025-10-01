import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """
    Unit tests for the emotion_detector function.
    """
    
    def test_joy_statement(self):
        """ Test for a statement that should result in 'joy'. """
        statement = "I am glad this happened"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_statement(self):
        """ Test for a statement that should result in 'anger'. """
        statement = "I am really mad about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_statement(self):
        """ Test for a statement that should result in 'disgust'. """
        statement = "I feel disgusted just hearing about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'disgust')
        
    def test_sadness_statement(self):
        """ Test for a statement that should result in 'sadness'. """
        statement = "I am so sad about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'sadness')
        
    def test_fear_statement(self):
        """ Test for a statement that should result in 'fear'. """
        statement = "I am really afraid that this will happen"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'fear')

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()