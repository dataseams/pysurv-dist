"""Implentation of survival distance score and clinical independence score."""
from numpy.typing import ArrayLike
from sksurv.utils import Surv


def _survival_distance_score(x: ArrayLike, y: Surv) -> float:
    score = 0
    return score


def survival_distance_score(X: ArrayLike, y: Surv) -> dict:
    """Calculate survival distance score."""
    scores = {}
    for col in X.columns:
        scores[col] = _survival_distance_score(X[col], y)
    return scores


def _clinical_independence_score(x: ArrayLike, y: ArrayLike) -> float:
    score = 0
    return score


def clinical_indpendence_score(X: ArrayLike, y: Surv, **kwargs) -> dict:
    """Calculate the clinical indpendence score.

    Train a linear regression model for each column in X against every other
    column.

    The clinical independence score is the following:

        1 - R**2
    """
    scores = {}
    for col in X.columns:
        scores[col] = _clinical_independence_score(X[col], y)
    return scores


def combine_sds_ci_scores(sds: dict, ci: dict, weight: float) -> dict:
    """Combine clinical independence and survival distance scores."""
    # check the keys are shared among both sds and ci

    # combine
    scores = {}
    return scores
