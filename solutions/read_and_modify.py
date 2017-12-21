import pandas as pd

data_train = pd.read_csv(
    'data/titanic_train.csv',
    index_col='PassengerId',
    usecols=lambda col: col not in ('Cabin', 'Ticket'),
    dtype={
        'Pclass': 'category',
        'Sex': 'category',
        'Embarked': 'category'
    }
)
