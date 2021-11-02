import unittest
import CustomFuncs
import TestMaterials


class Check_LineCleaner(unittest.TestCase):

    def test_NotVerbosePrint_01(self):
        self.assertEqual(CustomFuncs.LineCleaner(TestMaterials.t_01_request, 2), TestMaterials.t_01_responce)  # '&lt;' to '<' chk

    def test_NotVerbosePrint_02(self):
        self.assertEqual(CustomFuncs.LineCleaner(TestMaterials.t_02_request, 13), TestMaterials.t_02_responce) # '&pound;' to '£' chk

    def test_OutOfIdLim(self):
        self.assertEqual(CustomFuncs.LineCleaner(TestMaterials.t_03_request, 154), TestMaterials.t_03_responce)  # id 154 is absolutely out of range


class Check_BlockParser(unittest.TestCase):
    def test_ParseSomeNews_01(self):
        self.assertEqual(CustomFuncs.BlockParser(TestMaterials.t_04_request, 1), TestMaterials.t_04_responce)  # correct news format


    def test_ParseSomeNews_02(self):
        self.assertEqual(CustomFuncs.BlockParser(TestMaterials.t_05_request, 1), TestMaterials.t_05_responce)  # broken\lost data format

        
if __name__ == '__main__':
    unittest.main()