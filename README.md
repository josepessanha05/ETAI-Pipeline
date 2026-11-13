# Baseline Predictive Pipeline -- ETAI

20231690 - José Pessanha

## Week 2


Logistic Regression

Train accuracy: 0.679
Test accuracy:  0.678

Decision Tree

Train accuracy: 0.829
Test accuracy:  0.626

Current best model: Linear Regression - current decision tree model is overfitting



## Week 3


Logistic Regression

Train accuracy: 0.676
Test accuracy:  0.657

Decision Tree

Train accuracy: 0.792
Test accuracy:  0.611

Current pre-processing slightly worsens previous results, though the logistic regression remains the best overall model.


## Week 4

Dummy (baseline)

fold  train  validation    gap
    1  0.549       0.549  0.000
    2  0.549       0.549 -0.000
    3  0.549       0.549 -0.000
    4  0.549       0.549 -0.000
    5  0.549       0.549 -0.000


Logistic Regression

fold  train  validation    gap
    1  0.675       0.682 -0.007
    2  0.680       0.653  0.027
    3  0.674       0.674 -0.000
    4  0.671       0.691 -0.020
    5  0.675       0.666  0.010


Decision Tree

 fold  train  validation   gap
    1  0.801       0.620 0.181
    2  0.806       0.604 0.202
    3  0.798       0.647 0.151
    4  0.801       0.634 0.167
    5  0.801       0.624 0.177

Random Forest

fold  train  validation   gap
    1  0.801       0.628 0.173
    2  0.806       0.618 0.188
    3  0.798       0.633 0.165
    4  0.801       0.650 0.151
    5  0.801       0.627 0.174

Cross-validation and preprocessing changes improved previous results. Logistic Regression remains the best model, as both the decision tree and random forests overfit the data.




## Week 6


Logistic Regression

fold  train  validation    gap  inner_best  model__C model__solver  model__max_iter
    1  0.677       0.684 -0.007       0.675     0.369         lbfgs             1000
    2  0.681       0.652  0.029       0.683     0.168         lbfgs             2000
    3  0.677       0.675  0.002       0.674     0.053         lbfgs             2000
    4  0.674       0.690 -0.016       0.670     0.075         lbfgs             1000
    5  0.676       0.662  0.014       0.674     1.941         lbfgs             3000


Decision Tree

fold  train  validation    gap  inner_best  model__max_depth  model__min_samples_leaf model__criterion
    1  0.686       0.673  0.013       0.678                 9                       95             gini
    2  0.690       0.663  0.028       0.687                18                       76          entropy
    3  0.684       0.688 -0.004       0.674                 8                       71          entropy
    4  0.682       0.687 -0.006       0.675                17                       97             gini
    5  0.688       0.681  0.007       0.673                10                       55          entropy


Random Forest 

fold  train  validation    gap
    1  0.698       0.678  0.020
    2  0.702       0.659  0.043
    3  0.693       0.697 -0.003
    4  0.696       0.693  0.002
    5  0.697       0.679  0.019

Train       mean = 0.697   std = 0.003
Validation  mean = 0.681   std = 0.015
Gap         mean = +0.016   std = 0.018


Oblique Random Forest

 fold  train  validation    gap
    1  0.694       0.686  0.008
    2  0.699       0.659  0.040
    3  0.691       0.692 -0.001
    4  0.688       0.693 -0.005
    5  0.689       0.683  0.007

Train       mean = 0.692   std = 0.004
Validation  mean = 0.682   std = 0.014
Gap         mean = +0.010   std = 0.018


Adaboost

 fold  train  validation    gap
    1  0.685       0.670  0.015
    2  0.689       0.658  0.031
    3  0.680       0.695 -0.015
    4  0.677       0.682 -0.005
    5  0.676       0.689 -0.013

Train       mean = 0.681   std = 0.006
Validation  mean = 0.679   std = 0.015
Gap         mean = +0.002   std = 0.020

After tuning, logistic regression no longer yields the best results. Oblique Random Forest is now the best model, registering 0.692 accuracy in the training set and 0.682 in the validation set (very small overfit).



## Week 7


## Logistic Regression

Untuned


                   mean   std
accuracy          0.668 0.012
balanced_accuracy 0.665 0.012
precision         0.631 0.016
recall            0.634 0.019
f1                0.633 0.013
fbeta_2           0.634 0.016
roc_auc           0.719 0.014
average_precision 0.673 0.029

roc_auc: train-validation gap mean = +0.002

Out-of-fold predictions, development set (threshold 0.5):

        predicted 0  predicted 1
true 0         2205          965
true 1          951         1650


Tuned


                   mean   std
accuracy          0.676 0.016
balanced_accuracy 0.670 0.014
precision         0.650 0.023
recall            0.611 0.006
f1                0.630 0.012
fbeta_2           0.619 0.007
roc_auc           0.718 0.014
average_precision 0.672 0.028

roc_auc: train-validation gap mean = +0.002

Out-of-fold predictions, development set (threshold 0.5):

        predicted 0  predicted 1
true 0         2313          857
true 1         1011         1590

## Decision Tree

Untuned


                   mean   std
accuracy          0.662 0.022
balanced_accuracy 0.660 0.021
precision         0.624 0.034
recall            0.641 0.058
f1                0.630 0.025
fbeta_2           0.636 0.043
roc_auc           0.719 0.017
average_precision 0.667 0.029

roc_auc: train-validation gap mean = +0.029

Out-of-fold predictions, development set (threshold 0.5):

        predicted 0  predicted 1
true 0         2199          971
true 1          991         1610

Tuned


                   mean   std
accuracy          0.672 0.016
balanced_accuracy 0.667 0.015
precision         0.643 0.024
recall            0.617 0.032
f1                0.629 0.017
fbeta_2           0.622 0.025
roc_auc           0.720 0.014
average_precision 0.670 0.023

roc_auc: train-validation gap mean = +0.019

Out-of-fold predictions, development set (threshold 0.5):

        predicted 0  predicted 1
true 0         2273          897
true 1          995         1606


## Random Forest

Untuned


                   mean   std
accuracy          0.678 0.018
balanced_accuracy 0.672 0.017
precision         0.651 0.027
recall            0.616 0.020
f1                0.633 0.016
fbeta_2           0.623 0.017
roc_auc           0.724 0.014
average_precision 0.684 0.026

roc_auc: train-validation gap mean = +0.014

Out-of-fold predictions, development set (threshold 0.5):

        predicted 0  predicted 1
true 0         2308          862
true 1          998         1603

Tuned

                   mean   std
accuracy          0.675 0.017
balanced_accuracy 0.670 0.017
precision         0.644 0.021
recall            0.624 0.021
f1                0.634 0.018
fbeta_2           0.628 0.019
roc_auc           0.727 0.016
average_precision 0.688 0.023

roc_auc: train-validation gap mean = +0.019

Out-of-fold predictions, development set (threshold 0.5):

        predicted 0  predicted 1
true 0         2274          896
true 1          979         1622

## Oblique Random Forest

Untuned


                   mean   std
accuracy          0.682 0.014
balanced_accuracy 0.671 0.013
precision         0.685 0.028
recall            0.550 0.018
f1                0.610 0.012
fbeta_2           0.572 0.014
roc_auc           0.727 0.014
average_precision 0.686 0.028

roc_auc: train-validation gap mean = +0.022

Out-of-fold predictions, development set (threshold 0.5):

        predicted 0  predicted 1
true 0         2507          663
true 1         1170         1431

Tuned


                   mean   std
accuracy          0.680 0.013
balanced_accuracy 0.670 0.013
precision         0.675 0.020
recall            0.562 0.017
f1                0.613 0.015
fbeta_2           0.581 0.016
roc_auc           0.726 0.015
average_precision 0.685 0.024

roc_auc: train-validation gap mean = +0.024

Out-of-fold predictions, development set (threshold 0.5):

        predicted 0  predicted 1
true 0         2465          705
true 1         1140         1461


## Adaboost

Untuned


                   mean   std
accuracy          0.679 0.015
balanced_accuracy 0.666 0.014
precision         0.683 0.026
recall            0.538 0.021
f1                0.601 0.017
fbeta_2           0.562 0.018
roc_auc           0.723 0.013
average_precision 0.685 0.021

roc_auc: train-validation gap mean = +0.006

Out-of-fold predictions, development set (threshold 0.5):

        predicted 0  predicted 1
true 0         2518          652
true 1         1202         1399

Tuned


                   mean   std
accuracy          0.684 0.016
balanced_accuracy 0.673 0.016
precision         0.684 0.025
recall            0.559 0.028
f1                0.615 0.020
fbeta_2           0.580 0.025
roc_auc           0.727 0.015
average_precision 0.689 0.022

roc_auc: train-validation gap mean = +0.010

Out-of-fold predictions, development set (threshold 0.5):

        predicted 0  predicted 1
true 0         2497          673
true 1         1148         1453


## Gradient Boosting

Untuned


                   mean   std
accuracy          0.675 0.012
balanced_accuracy 0.663 0.013
precision         0.675 0.019
recall            0.540 0.031
f1                0.600 0.020
fbeta_2           0.562 0.027
roc_auc           0.724 0.015
average_precision 0.686 0.026

roc_auc: train-validation gap mean = +0.040

Out-of-fold predictions, development set (threshold 0.5):

        predicted 0  predicted 1
true 0         2493          677
true 1         1196         1405

Tuned


                   mean   std
accuracy          0.681 0.017
balanced_accuracy 0.671 0.018
precision         0.676 0.021
recall            0.563 0.033
f1                0.614 0.025
fbeta_2           0.582 0.030
roc_auc           0.727 0.016
average_precision 0.692 0.026

roc_auc: train-validation gap mean = +0.014

Out-of-fold predictions, development set (threshold 0.5):

        predicted 0  predicted 1
true 0         2466          704
true 1         1136         1465


## Hist Gradient Boosting

Untuned


                   mean   std
accuracy          0.679 0.014
balanced_accuracy 0.667 0.014
precision         0.680 0.026
recall            0.546 0.023
f1                0.605 0.016
fbeta_2           0.568 0.020
roc_auc           0.725 0.016
average_precision 0.689 0.028

roc_auc: train-validation gap mean = +0.030

Out-of-fold predictions, development set (threshold 0.5):

        predicted 0  predicted 1
true 0         2499          671
true 1         1182         1419

Tuned


                   mean   std
accuracy          0.683 0.016
balanced_accuracy 0.671 0.016
precision         0.682 0.028
recall            0.557 0.029
f1                0.612 0.020
fbeta_2           0.578 0.025
roc_auc           0.728 0.015
average_precision 0.691 0.024

roc_auc: train-validation gap mean = +0.010

Out-of-fold predictions, development set (threshold 0.5):

        predicted 0  predicted 1
true 0         2491          679
true 1         1153         1448

## Gaussian Naive Bayes

Untuned


                   mean   std
accuracy          0.621 0.010
balanced_accuracy 0.591 0.010
precision         0.701 0.039
recall            0.280 0.011
f1                0.400 0.013
fbeta_2           0.318 0.011
roc_auc           0.698 0.012
average_precision 0.646 0.025

roc_auc: train-validation gap mean = +0.001

Out-of-fold predictions, development set (threshold 0.5):

        predicted 0  predicted 1
true 0         2856          314
true 1         1872          729

Tuned

                   mean   std
accuracy          0.622 0.012
balanced_accuracy 0.588 0.012
precision         0.738 0.048
recall            0.250 0.014
f1                0.373 0.019
fbeta_2           0.288 0.016
roc_auc           0.705 0.011
average_precision 0.655 0.027

roc_auc: train-validation gap mean = +0.002

Out-of-fold predictions, development set (threshold 0.5):

        predicted 0  predicted 1
true 0         2937          233
true 1         1951          650

Seeing as the objective of the model is to minimize the ratio of false positives compared to the original model, the selection to be accounted for most is precision. If we look only at precision, the first choice would be the Naive Bayes model, however it focuses in precision so much to the extent it overpredicts the number of non-reoffenders, resulting in an extremely low recall (number of all the actual positive cases in the dataset). So, if we also look at the F1 score instead, which focuses on an harmonized balance between precision and recall, while still accounting mainly for precision, the current best model is Adaboost, as it scores an average precision of 0.684 with its current tuning, while maintaining a 0.01 roc-auc gap between training and validation.



## Week 8


## XGBoost (Tuning is activated)

No feature selection


                   mean   std
accuracy          0.682 0.016
balanced_accuracy 0.670 0.015
precision         0.683 0.027
recall            0.551 0.016
f1                0.610 0.016
fbeta_2           0.573 0.015
roc_auc           0.727 0.015
average_precision 0.691 0.023

roc_auc: train-validation gap mean = +0.012


        predicted 0  predicted 1
true 0         2503          667
true 1         1167         1434

              precision    recall  f1-score   support

           0       0.68      0.79      0.73      3170
           1       0.68      0.55      0.61      2601

    accuracy                           0.68      5771
   macro avg       0.68      0.67      0.67      5771
weighted avg       0.68      0.68      0.68      5771


Feature selection on



                   mean   std
accuracy          0.681 0.013
balanced_accuracy 0.671 0.013
precision         0.675 0.021
recall            0.565 0.022
f1                0.615 0.016
fbeta_2           0.584 0.019
roc_auc           0.725 0.012
average_precision 0.689 0.021

roc_auc: train-validation gap mean = +0.005


        predicted 0  predicted 1
true 0         2461          709
true 1         1131         1470

              precision    recall  f1-score   support

           0       0.69      0.78      0.73      3170
           1       0.67      0.57      0.62      2601

    accuracy                           0.68      5771
   macro avg       0.68      0.67      0.67      5771
weighted avg       0.68      0.68      0.68      5771


The model with feature selection activated shows a tradeoff between a slightly better recall and f1 score, at the cost of a slight decrease in precision. Keeping in mind improving its predecessor's precision is the main goal of the pipeline, the small increase in recall and f1 score is not enough to make up for the loss in precision. For that reason, for XGBoost, the better option would be to leave the features as they are.



## Week 9 - Beyond COMPAS (option A)

Note: "python main.py config_adult.py" to run using the new config file

## Changes made (includes some previous mistakes)

| Broke | Why | Fix |
|---|---|---|
| `?` stayed a category | Placeholders were only turned into NaN inside `_canonicalize_categories`, which only touches columns listed in `canonical_categories`. Adult has none. | Global placeholder pass over every text column in `clean_dataset` |
| Hardcoded `score_text` | `split_features_target` and `fairness_report` assumed COMPAS's own score exists | `data.reference_prediction` in the config, read by both functions |
| Fairness wording | "Did not reoffend" and "COMPAS's own score" are COMPAS-specific | Generic FPR/TPR/predicted-positive report per group, with an optional reference score |
| `age >= 18` rule | It would erase the 74 people aged 17 | Validity rules written per dataset (`age: {min: 17}`; no max on `capital_gain`, since 99999 is a real top code) |
| Target encoder leaked | `category_encoders.TargetEncoder` is not cross-fitted, so noise columns (`v19`-`v25`) can look informative to `VoteSelector` | New `target_cv` option using sklearn's cross-fitted `TargetEncoder`; COMPAS keeps `target` |
| `main.py` fixed config | It always loaded `config.yaml` | Config path taken from the command line (`python main.py config_adult.yaml`), defaulting to `config.yaml` |
| No predictions for the new people | The pipeline only evaluated on training data | New `src/predict.py` (`predict_new`), called after the final refit; same cleaning, no `drop_duplicate_rows`, 2,000 rows in = 2,000 out |
| Columns silently ignored | Anything not in `numeric_features` or `categorical_features` is dropped without an error | `check_feature_coverage` warns about unused columns in `X` |
| Leftover placeholders unnoticed | Nothing verified that `?` was gone after cleaning | `check_placeholders_left` guard in `main.py`, plus `check_cleaning.py` to confirm the missing counts 379, 381 and 86 |
| `RobustScaler` on skewed columns | `capital_gain` is 92% zeros, so the IQR is 0 and the column isn't really scaled | `scaler: "standard"` in `config_adult.yaml` (a log transform is an option to try) |
| Sensitive attribute choice | The notebook leaves open which of `race` and `sex` is audited | `sensitive_attr: "sex"` is audited and never a feature; `race` is included in the remaining features |

## XGBoost

# Untuned

                   mean   std
accuracy          0.864 0.011
balanced_accuracy 0.781 0.021
precision         0.766 0.035
recall            0.622 0.046
f1                0.686 0.030
fbeta_2           0.646 0.040
roc_auc           0.913 0.016
average_precision 0.805 0.027

roc_auc: train-validation gap mean = +0.026

# Tuned


                   mean   std
accuracy          0.858 0.010
balanced_accuracy 0.771 0.025
precision         0.756 0.027
recall            0.603 0.059
f1                0.669 0.035
fbeta_2           0.628 0.050
roc_auc           0.909 0.015
average_precision 0.791 0.027

roc_auc: train-validation gap mean = +0.009


## Hist Gradient Boosting

# Untuned


                   mean   std
accuracy          0.861 0.013
balanced_accuracy 0.774 0.023
precision         0.764 0.036
recall            0.608 0.047
f1                0.676 0.034
fbeta_2           0.634 0.042
roc_auc           0.911 0.017
average_precision 0.799 0.030

roc_auc: train-validation gap mean = +0.024

# Tuned


                   mean   std
accuracy          0.860 0.011
balanced_accuracy 0.771 0.021
precision         0.764 0.031
recall            0.601 0.043
f1                0.672 0.031
fbeta_2           0.627 0.038
roc_auc           0.911 0.016
average_precision 0.799 0.030

roc_auc: train-validation gap mean = +0.012


Features kept: 8 of 37: numeric__age, numeric__education_num, numeric__capital_gain, numeric__capital_loss, numeric__hours_per_week, categorical__marital_status, categorical__occupation, categorical__relationship


Both these models registered each of the target scores. The tuning settings reduced the overfitting effect on both models, while accuracy and the F1 score suffered a minor decrease. 
The hardest assumption to find was how placeholders are cleaned. _canonicalize_categories only converts ? to a missing value in columns listed in canonical_categories, which on COMPAS covered everything relevant, so the pipeline ran on Adult without any error, while ? stayed a real category. It was found only by checking value_counts(dropna=False) against the expected missing counts (379, 381, 86), and the issue then fixed with a pass over every text column in clean_dataset. 


## Project structure

```
.
├── main.py                # entry point: run the whole pipeline
├── config.yaml             # all tunable settings live here
├── requirements.txt
├── src/
│   ├── data.py             # loading
│   ├── preprocessing.py    # cleaning + train/test split
│   ├── model.py             # model construction
│   ├── evaluate.py         # accuracy metrics + fairness check
│   └── results.py          # saves each run's report to disk
├── results/                # created automatically -- one file per run (not tracked in git)
└── data/
    ├── compas_two_year_recidivism.csv
    └── README.md            # problem description + full data dictionary
```

## Pipeline progress

This table is updated after each practical class, so you can always see what changed in the pipeline and why -- it's a running log, not a fixed syllabus.

| Week | Practical class focus | Added to the pipeline |
|------|------------------------|------------------------|
| 2 | Introduction & baseline pipeline | Initial version: project structure, a single naive train/test split (no cross-validation), minimal preprocessing (drop rows with missing values, one-hot encode categoricals), logistic regression baseline, a first (deliberately simple) fairness check comparing our model's and COMPAS's own false-positive rate by race, train-vs-test accuracy reporting (to start spotting overfitting), and each run's full report saved automatically to `results/` |

## Environment setup

You only need to do this once per machine.

### macOS / Linux
```bash
python3 -m venv venv                 # creates an isolated Python environment in a folder called "venv"
source venv/bin/activate             # activates it -- packages install here, not system-wide, and stay out of your other projects
pip install -r requirements.txt      # installs the exact packages this project needs, into that environment
```

### Windows -- PowerShell
```powershell
python -m venv venv                  # creates an isolated Python environment in a folder called "venv"
venv\Scripts\activate                # activates it -- packages install here, not system-wide, and stay out of your other projects
pip install -r requirements.txt      # installs the exact packages this project needs, into that environment
```
If PowerShell blocks the activation script, run this once first:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### Windows -- cmd.exe
Same three steps as above, just with cmd's own activation command:
```cmd
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

Once the environment is active you'll see `(venv)` at the start of your prompt. To leave it later, run `deactivate` (same command on every OS).

### Every time after the first

Creating the environment and installing packages only needs to happen once, ever. Every other time you sit down to work -- a new terminal window, the next practical class, tomorrow -- you don't repeat any of the steps above. From the project's root folder, you just need to:

**macOS / Linux**
```bash
source venv/bin/activate
python main.py
```

**Windows**
```powershell
venv\Scripts\activate
python main.py
```

That's it -- activate, then run. If you don't see `(venv)` at the start of your prompt, the environment isn't active and `python main.py` may use the wrong Python (or fail to find a package) entirely.

## Running the pipeline

With the environment active (see above), from the project's root
folder, on any OS:
```bash
python main.py
```

This loads `config.yaml`, loads and preprocesses the data, trains the model, and prints:
- **train accuracy and test accuracy, side by side.** Comparing the two is how you catch overfitting: if the model looks much better on the data it was trained on than on data it's never seen, it has memorised rather than learned something that generalises. 
- a classification report on the test set
- a false-positive-rate-by-race comparison between our model and
  COMPAS's own score

All of this is also saved to a timestamped file in `results/` (e.g.`results/run_20260916_143012.txt`), so it doesn't just scroll past in your terminal -- open it later, or change something in `config.yaml` (like the model type) and compare the new file to the last one.
`results/` is created automatically the first time you run the
pipeline, and isn't tracked in git (see `.gitignore`) since it's
generated output, not source.

You're free to improve on this structure or restructure it entirely -- what matters is that your project stays runnable end-to-end with a single command, and that each piece (data, preprocessing, model, evaluation) stays easy to find and change independently.

## Dataset

See `data/README.md`.
