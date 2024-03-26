from unittest import TestCase
from termo import Termo, Feedback, InvalidAttempt


class TermoTest(TestCase):

    def test_run(self):
        self.assertTrue(True)

    def test_all_right(self):
        termo = Termo('casa')
        result = termo.test('casa')
        expected = [
            ('c', Feedback.RIGHT_PLACE),
            ('a', Feedback.RIGHT_PLACE),
            ('s', Feedback.RIGHT_PLACE),
            ('a', Feedback.RIGHT_PLACE),
        ]
        self.assertTrue(result.win)
        self.assertListEqual(result.feedback, expected)

    def test_all_wrong_place(self):
        termo = Termo('abc')
        result = termo.test('cab')
        expected = [
            ('c', Feedback.WRONG_PLACE),
            ('a', Feedback.WRONG_PLACE),
            ('b', Feedback.WRONG_PLACE),
        ]
        self.assertFalse(result.win)
        self.assertListEqual(result.feedback, expected)

    def test_all_wrong(self):
        termo = Termo('casa')
        result = termo.test('pent')
        expected = [
            ('p', Feedback.WRONG),
            ('e', Feedback.WRONG),
            ('n', Feedback.WRONG),
            ('t', Feedback.WRONG),
        ]
        self.assertFalse(result.win)
        self.assertListEqual(result.feedback, expected)

    def test_valid_attempt(self):
        termo = Termo('casa')
        with self.assertRaises(InvalidAttempt):
            termo.test('abc')

    # def test_character_count(self):
    #     termo = Termo('casa')
    #     result = termo.test('asaa')
    #     expected = [
    #         ('a', Feedback.WRONG_PLACE),
    #         ('s', Feedback.WRONG_PLACE),
    #         ('a', Feedback.WRONG_PLACE),
    #         ('a', Feedback.WRONG),
    #     ]
