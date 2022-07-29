"""Implementation of survival distance score and clinical independence score.

The survival distance score was defined in this paper:

https://psb.stanford.edu/psb-online/proceedings/psb20/Neums.pdf

The goal of the survival distance score is to measure the variation in survival
rate across time given a particular feature.

"""
from typing import List

import numpy as np
import pandas as pd
from numpy.typing import ArrayLike
from sklearn.linear_model import LinearRegression
from sksurv.util import Surv, check_y_survival


def _survival_distance_score(x: ArrayLike, y: Surv) -> float:
    score = 0
    event, time = check_y_survival(y)
    for t in np.sort(time.unique()):
        # get mean / variance of feature
        pass
    return score


def survival_distance_score(X: pd.DataFrame, y: Surv) -> dict:
    """Calculate survival distance score."""
    scores = {}
    for col in X:
        scores[col] = _survival_distance_score(X[col], y)
    return scores


def _clinical_independence_score(x: pd.DataFrame, y: ArrayLike) -> float:
    """Calculate the score for clinical independence.

    Parameters
    ----------
    x : ArrayLike
        Multi-dimensional array, all of the other attributes we are using to
        assess the independence of y
    y : ArrayLike
        One-dimensional array, the attribute values we're fitting
        the linear regression for

    Returns
    -------
    score : float
        cg = 1 - R^2, R^2 being the coefficient of determination
    """
    reg = LinearRegression()
    reg.fit(x, y)
    score = 1 - reg.score(x, y)
    return score


def clinical_independence_score(X: ArrayLike) -> ArrayLike:
    """Calculate the clinical independence score.

    Train a linear regression model for each feature in X against all other
    features to measure how independent a given feature is compared to the
    other features provided.

    The clinical independence score for one feature is the following:
        1 - R^2

    The final result is a 1D array with clinical independence value for each
    feature

    If multi-dimensional array X is a numpy array, then we expect the shape of
    the array to be [n_rows, n_cols]. If shape is the opposite, the operation
    will fail.

    Parameters
    ----------
    X: ArrayLike
        All feature attributes
    y: ArrayLike
        Survival values

    Returns
    -------
    ArrayLike
        Clinical independence score for column in order of the features given
    """
    if isinstance(X, pd.DataFrame):
        X = X.values

    x_transpose = X.T
    scores = [
        _clinical_independence_score(
            x=np.delete(x_transpose, i, 0), y=x_transpose[i]
        )
        for i in range(x_transpose.shape[0])
    ]
    return np.array(scores)


def combine_sds_ci_scores(
    sds: List[float], ci: List[float], weight: float
) -> List[float]:
    """Combine clinical independence and survival distance scores.

    Assume that the clinical independence and survival distance score arrays
    are in the same order, i.e. element 0 references the same attribute.

    Parameters
    ----------
    sds : List[float]
        Survival distance scores
    ci : dict
        Clinical independence scores
    weight : float
        How much to weigh the survival distance over the clinical independence
        score during combination.

    Returns
    -------
    List[float]
        List of combined survival distance and clinical independence scores
    """
    # combine
    scores = []
    return scores


class SurvivalDistanceClinicalIndependenceTransformer:
    """Apply survival distance scoring and clinical independence scoring."""

    def __init__(
        self, clinical_weight: float, corr_threshold: float = 0.6
    ) -> None:
        self.clinical_weight = clinical_weight
        self.corr_threshold = corr_threshold
        self.survival_scores = np.array([])
        self.clinical_scores = np.array([])
        self.combined_scores = np.array([])

    def fit(self, df: ArrayLike) -> ArrayLike:
        """Fit transformer to input data."""
        pass

    def transform(self, df: ArrayLike) -> ArrayLike:
        """Transform data by combining correlated columns."""
        pass

    def fit_transform(self, df: ArrayLike) -> ArrayLike:
        """Fit and transform input data."""
        pass
