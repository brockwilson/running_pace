import unittest
import web_input
import datetime


class TestValidationFunctions(unittest.TestCase):

    def test_date_validator(self):
        self.assertTrue(web_input.date_validator(
                datetime.date.isoformat(datetime.date.today())))
        self.assertFalse(web_input.date_validator(
                datetime.date.isoformat(datetime.date.today() + 
                                        datetime.timedelta(days=1))))
        self.assertTrue(web_input.date_validator(web_input.MINIMUM_DATE.strftime("%Y-%m-%d")))
        self.assertTrue(web_input.date_validator((web_input.MINIMUM_DATE-datetime.timedelta(days=-1)).strftime("%Y-%m-%d")))


if __name__ == '__main__':
    unittest.main()
