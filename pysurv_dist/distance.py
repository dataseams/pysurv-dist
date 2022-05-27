"""Implementation of survival distance score and clinical independence score.

The survival distance score was defined in this paper:

https://psb.stanford.edu/psb-online/proceedings/psb20/Neums.pdf

The goal of the survival distance score is to measure the variation in survival
rate across time given a particular feature.

"""
import numpy as np
from numpy.typing import ArrayLike
from sksurv.util import Surv, check_y_survival
from sklearn.linear_model import LinearRegression


def _survival_distance_score(x: ArrayLike, y: Surv) -> float:
    score = 0
    event, time = check_y_survival(y)
    for t in np.sort(time.unique()):
        # get mean / variance of feature
        pass
    return score


def survival_distance_score(X: ArrayLike, y: Surv) -> dict:
    """Calculate survival distance score."""
    scores = {}
    for col in X.columns:
        scores[col] = _survival_distance_score(X[col], y)
    return scores


def _clinical_independence_score(x: ArrayLike, y: ArrayLike) -> float:
    """Calculate the score for clinical independence.

    Parameters
    ----------
    x : ArrayLike
        All but one attribute
    y : ArrayLike
        The attribute values we're fitting the linear regression for

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
    scores = [
        _clinical_independence_score(x=X.drop(col, axis=1), y=X[col])
        for col in X.columns
    ]
    return scores


def combine_sds_ci_scores(sds: dict, ci: dict, weight: float) -> dict:
    """Combine clinical independence and survival distance scores."""
    # check the keys are shared among both sds and ci

    # combine
    scores = {}
    return scores
