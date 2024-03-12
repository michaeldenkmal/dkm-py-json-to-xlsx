import unittest

from dkm_json_to_xlsx import json_to_xlsx


class JsonToXlsxTest(unittest.TestCase):
    def test_convert_json_to_xlsx(self):
        json_path=r"D:\projekte\ts\dkm-ts-ga-bsa-verbleib-stat\src\model\__jest__\m1704\DatenGrundlage_m1704.json"
        xlsx_path=r"D:\projekte\ts\dkm-ts-ga-bsa-verbleib-stat\src\model\__jest__\m1704\DatenGrundlage_m1704.xlsx"
        json_to_xlsx.convert_json_to_xlsx(json_path, xlsx_path, arr_prop_name="rows")


if __name__ == '__main__':
    unittest.main()
