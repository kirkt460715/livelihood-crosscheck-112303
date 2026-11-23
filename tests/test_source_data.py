"""原始业务凭据的可读性和关系完整性。"""
import json
from pathlib import Path
import unittest

DATA = Path(__file__).resolve().parents[1] / "data"


def table(name):
    with (DATA / (name + ".json")).open(encoding="utf-8") as stream:
        return json.load(stream)


class SourceDataTest(unittest.TestCase):
def test_payment_candidates_point_to_obligations(self):
        names = {row["obligation"] for row in table("wages")}
        names.update(f'{row["obligation"]}/{household}'
                     for row in table("rent") for household in row["shares"])
        for row in table("payments"):
            self.assertLessEqual(set(row["confirmed"]), set(row["candidates"]))
            self.assertLessEqual(set(row["candidates"]), names)
            self.assertLessEqual(sum(row["confirmed"].values()), row["yuan"])

    def test_comparison_and_followup_share_source_records(self):
        self.assertEqual({row["period"] for row in table("rent")}, {"2024-Q2", "2025-Q2"})
        recent = {row["payment"]: row for row in table("payments")}
        for case in table("followups"):
            if case["receipt"]:
                self.assertEqual(recent[case["receipt"]]["date"][:7], case["date"][:7])
        alternatives = [row["household"] for row in table("identity") if row["choice_set"] == "R1"]
        self.assertEqual(set(alternatives), {"H21", "H22"})
