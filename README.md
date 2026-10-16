# Baseline Predictive Pipeline -- ETAI

20231690 - José Pessanha

Week 2


Logistic Regression

Train accuracy: 0.679
Test accuracy:  0.678

Decision Tree

Train accuracy: 0.829
Test accuracy:  0.626

Current best model: Linear Regression - current decision tree model is overfitting



Week 3


Logistic Regression

Train accuracy: 0.676
Test accuracy:  0.657

Decision Tree

Train accuracy: 0.792
Test accuracy:  0.611

Current pre-processing slightly worsens previous results, though the logistic regression remains the best overall model.


Week 4

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




Week 6


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
