import unittest
import web_input as wi
import datetime


class TestValidationFunctions(unittest.TestCase):

    def test_date_validator(self):
        self.assertTrue(wi.date_validator(
                datetime.date.isoformat(datetime.date.today())))
        self.assertFalse(wi.date_validator(
                datetime.date.isoformat(datetime.date.today() + 
                                        datetime.timedelta(days=1))))
        self.assertTrue(wi.date_validator(wi.MINIMUM_DATE.strftime("%Y-%m-%d")))
        self.assertTrue(wi.date_validator((wi.MINIMUM_DATE-datetime.timedelta(days=-1)).strftime("%Y-%m-%d")))

    def test_duration_validator(self):
        # validate durations that are entered as seconds
        self.assertTrue(wi.duration_validator("1.123"))
        self.assertTrue(wi.duration_validator("59"))
        self.assertTrue(wi.duration_validator("80"))
        self.assertFalse(wi.duration_validator("-1"))
        self.assertFalse(wi.duration_validator("0"))

        # validate durations that are entered as mm:ss
        self.assertTrue(wi.duration_validator("1:59"))
        self.assertTrue(wi.duration_validator("2:00"))
        self.assertTrue(wi.duration_validator("61:45"))
        self.assertFalse(wi.duration_validator("1:60"))
        self.assertFalse(wi.duration_validator("1:-1"))
        self.assertFalse(wi.duration_validator("-1:59"))
        self.assertFalse(wi.duration_validator("1.23:1"))

        # validate durations that are entered as hh:mm:ss
        self.assertTrue(wi.duration_validator("1:21:30"))
        self.assertTrue(wi.duration_validator("24:21:12"))
        self.assertTrue(wi.duration_validator("1:00:00"))
        self.assertFalse(wi.duration_validator("1:01:-1"))
        self.assertFalse(wi.duration_validator("1:-1:01"))
        self.assertFalse(wi.duration_validator("-1:01:01"))
        self.assertFalse(wi.duration_validator("1:01:61"))
        self.assertFalse(wi.duration_validator("1:61:12"))

        # other possible invalid forms
        self.assertFalse(wi.duration_validator("1:23:49:12"))
        


if __name__ == '__main__':
    unittest.main()
