import os
import unittest

from dkm_json_to_xlsx import json_to_xlsx


class JsonToXlsxTest(unittest.TestCase):
    def test_convert_json_to_xlsx(self):
        json_path=r"D:\projekte\ts\dkm-ts-ga-bsa-verbleib-stat\src\model\__jest__\m1714\DatenGrundlage_m1714.json"
        xlsx_path=r"D:\projekte\ts\dkm-ts-ga-bsa-verbleib-stat\src\model\__jest__\m1714\DatenGrundlage_m1714.xlsx"
        wrapped_json_path = r"D:\projekte\ts\dkm-ts-ga-bsa-verbleib-stat\src\model\__jest__\m1714\wrapped_DatenGrundlage_m1714.json"
        json_to_xlsx.wrap_arr_json_in_root_key(json_in_fp=json_path,json_out_fp=wrapped_json_path,root_key="rows")
        json_to_xlsx.convert_json_to_xlsx(wrapped_json_path, xlsx_path, arr_prop_name="rows")


if __name__ == '__main__':
    unittest.main()
