from unittest import TestCase
from unittest.mock import patch

import numpy as np
import pandas as pd

from pysurv_dist import distance


class TestClinicalIndependenceScore(TestCase):
    def setUp(self) -> None:
        self.data = pd.DataFrame(
            {
                "x1": range(10),
                "x2": [20, 22, 23.5, 24, 25, 28, 28, 29, 29.5, 30],
                "x3": range(50, 60),
            }
        )
        self.random_data = pd.DataFrame(
            {
                "x1": [1, 5, 10, 250, 55, 36, 1, 36, 42, 78],
                "x2": [20, 21.1, 21.9, 23, 24, 25, 26, 27, 28, 29],
            }
        )

    @patch("pysurv_dist.distance._clinical_independence_score")
    def test_happy_path_dataframe(self, mock_cg):
        expected_scores = np.array([1, 2, 3])
        mock_cg.side_effect = expected_scores
        scores = distance.clinical_independence_score(self.data)
        np.testing.assert_array_equal(scores, expected_scores)

    @patch("pysurv_dist.distance._clinical_independence_score")
    def test_happy_path_array(self, mock_cg):
        expected_scores = np.array([1, 2, 3])
        mock_cg.side_effect = expected_scores
        scores = distance.clinical_independence_score(self.data.values)
        np.testing.assert_array_equal(scores, expected_scores)

    @patch("pysurv_dist.distance._clinical_independence_score")
    def test_array_transposed(self, mock_cg):
        expected_scores = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        mock_cg.side_effect = expected_scores
        scores = distance.clinical_independence_score(self.data.values.T)
        np.testing.assert_array_equal(scores, expected_scores)

    def test__clinical_independence_score(self):
        score = distance._clinical_independence_score(
            self.data[["x1"]], self.data["x2"]
        )
        expected_score = 0.04324611
        self.assertAlmostEqual(score, expected_score, 8)

    def test__clinical_independence_score_random(self):
        score = distance._clinical_independence_score(
            self.random_data[["x1"]], self.random_data["x2"]
        )
        expected_score = 0.994
        self.assertAlmostEqual(score, expected_score, 3)
