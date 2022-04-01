"""Feature selection module.

Has scoring function and feature selection classes.
"""
from numpy import Arrayterator
import pandas as pd
from numpy.typing import ArrayLike
from sklearn.feature_selection._univariate_selection import (
    _BaseFilter as _BaseFilterSK,
)
from sksurv.utils import Surv

from .distance import (
    survival_distance_score,
    clinical_indpendence_score,
    combine_sds_ci_scores,
)


def score_function(X: ArrayLike, y: Surv) -> ArrayLike:
    """Generate survival distance score + clinical independence scores.

    Parameters
    ----------
    X : Union[pd.DataFrame, ArrayLike]
        _description_
    y : Surv
        _description_

    Returns
    -------
    Arraylike
        The survival distance scores for the input features.
    """
    # TODO: validate y, make sure that y has boolean and float/int tuple
    #  using sksurv checks
    sds = survival_distance_score(X, y)
    ci = clinical_indpendence_score(X)
    combined = combine_sds_ci_scores(sds=sds, ci=ci)
    return combined


class _BaseFilter(
    _BaseFilterSK,
):
    def _validate_data(
        self,
        X="no_validation",
        y="no_validation",
        reset=True,
        validate_separately=False,
        **check_params
    ):
        raise NotImplementedError

    def fit(self, X: ArrayLike, y: Surv):
        """Run score function on (X, y) and get the appropriate features.

        Parameters
        ----------
        X : ArrayLike
            The training input samples.
        y : Surv
            The target values (time observed, event indicator)
        """
        #
        pass


class SelectKBest(_BaseFilter):
    """Select K Best survival analysis features.

    Uses survival distance score + clinical analysis.

    Parameters
    ----------
    _BaseFilter : _type_
        _description_
    """

    def __init__(self, k: int, score_func=score_function):
        super().__init__(score_func=score_func)
        self.k = k


class FeatureReduction:
    def __init__(
        self, X: ArrayLike, scorer: SelectKBest, corr_threshold: float = 0.6
    ) -> None:
        self.X = X
        self.scorer = scorer  # pull out the feature names and scores
        self.corr_threshold = corr_threshold

    def _transform(self):
        """"""

    def transform(self):
        pass
