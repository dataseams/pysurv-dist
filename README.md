# pysurv-dist
Python implementation of the survival distance score.

## Why pysurv-dist?

Feature selection in a Survival Analysis (SA) context is more complex than feature selection in a standard classification or regression problem.
This is because you have 2 attributes of the target:

    - time observed: integer or float
    - experienced event at end of time observed(censored): boolean

Historically, there are a number of ways that feature selection in a SA context has been done, for example:

    - Logrank test: statistical comparison of the survival curves of more than one group, applies to categorical features only
    - Cox Proportional Hazards model with regularization: select features based on model results, for example pick the features that are statistically significant and have a nonzero coefficient
    - Domain Expertise, particularly in a medical setting
    - Dimension reduction techniques (PCA, SVD, etc.)

This library implements a new method of feature selection that applies to categorical and continuous features, based Nuems et al.'s paper, [Improving survival prediction using a novel feature selection and feature reduction framework based on the integration of clinical and molecular data.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6941850/).
This method was built to anlayze and reduce large feature spaces with the original use case being high-dimensional sparse gene expression datasets.
 
The strength of this method is that it incorporates the time and variance of the features with respect to the survival curve, as well as provides an interpretable version of feature reduction.

## Concepts

1. Survival Distance Score (SDS)

This score assesses the variance of the feature over time with regards to the survival rate at a given time t.

    [insert formula]

For example, if an input feature was a person's age and we are at time t, we'd compare the mean age of persons that had experienced the event before t and after t, compared to persons that experienced the event at t.

2. Clinical Independence Score (CI)

Fits a linear regression model (with regularization) that asses the independence of a single feature against all other features in the feature space.
Formula:

    CI_x = 1 - R^2

By subtracting the R-squared value of the validation set, we observe that higher scores indicate greater independance from other features in the space. 
The idea is that in a large dimensional feature space, there could be many features that are highly correlated. This score is one of the gate criteria for feature reduction with its highly related features.


3. Survival Distance Score + Weighted Clinical Independence Score (SDSC)

Combination of the 2 scores allows us to rank the features according to:

    1. Discrimination between those at risk for experiencing the event though time observed
    2. Uniqueness or collinearity of features against others in the feauture space


4. Feature reduction

Features that have low CI scores will be combined together with this formula:

    [insert formula]

During reduction, the features in a given group are weighted according to their SDSC values.

# References

[Neums L, Meier R, Koestler DC, Thompson JA. Improving survival prediction using a novel feature selection and feature reduction framework based on the integration of clinical and molecular data. Pac Symp Biocomput. 2020;25:415-426.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6941850/)
