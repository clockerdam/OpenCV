import unittest
from util.json_to_df import create_df, get_resume_dict_from_dataframe
from jsondiff import diff
import json


class TestUtil(unittest.TestCase):

    def test_json_pandas_conversion(self):
        resume = {}
        with open("test/example_resume.json") as f:
            try:
                resume = json.loads(f.read())
            except: 
                self.fail("Could not load the example file")

        df, md = create_df(resume)

        back = get_resume_dict_from_dataframe(df, md)

        self.assertEqual( diff(resume, back), {})

if __name__ == "__main__": 
    unittest.main()


