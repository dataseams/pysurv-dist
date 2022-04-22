"""Implentation of survival distance score and clinical independence score."""
from numpy.typing import ArrayLike
from sksurv.utils import Surv


def survival_distance_score(X: ArrayLike, y: Surv) -> dict:
    """Calculate survival distance score."""
    pass


def clinical_indpendence_score(X: ArrayLike, y: Surv, **kwargs) -> dict:
    """Calculate the clinical indpendence score."""
    pass


def combine_sds_ci_scores(sds: dict, ci: dict, weight: float):
    """Combine clinical independence and survival distance scores."""
    pass
