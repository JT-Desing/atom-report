import io
import json
import os
import sys
import types
import unittest

os.environ.setdefault("SOURCE_BUCKET", "test-bucket")

fake_boto3 = types.ModuleType("boto3")
fake_boto3.client = lambda name: object()
sys.modules.setdefault("boto3", fake_boto3)

fake_botocore = types.ModuleType("botocore")
fake_exceptions = types.ModuleType("botocore.exceptions")
fake_exceptions.ClientError = type("ClientError", (Exception,), {})
sys.modules.setdefault("botocore", fake_botocore)
sys.modules.setdefault("botocore.exceptions", fake_exceptions)

import app


class FormatTests(unittest.TestCase):
    def test_csv_semicolon(self):
        rows = app._read_records("reporte.csv", b"id;agente\n1;Ana\n")
        self.assertEqual(rows, [{"id": "1", "agente": "Ana"}])

    def test_json_list_and_wrapper(self):
        self.assertEqual(app._read_records("reporte.json", b'[{"id": 1}]'), [{"id": 1}])
        wrapped = json.dumps({"records": [{"id": 2}]}).encode()
        self.assertEqual(app._read_records("reporte.json", wrapped), [{"id": 2}])

    def test_json_lines(self):
        rows = app._read_records("reporte.jsonl", b'{"id": 1}\n{"id": 2}\n')
        self.assertEqual([row["id"] for row in rows], [1, 2])

    def test_excel(self):
        from openpyxl import Workbook
        workbook = Workbook()
        sheet = workbook.active
        sheet.append(["id", "agente"])
        sheet.append([1, "Ana"])
        stream = io.BytesIO()
        workbook.save(stream)
        rows = app._read_records("reporte.xlsx", stream.getvalue())
        self.assertEqual(rows, [{"id": 1, "agente": "Ana"}])


if __name__ == "__main__":
    unittest.main()
