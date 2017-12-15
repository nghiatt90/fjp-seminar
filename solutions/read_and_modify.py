import pandas as pd

data = pd.read_csv(
    'data/titanic.csv',
    index_col='PassengerId',
    usecols=lambda col: col not in ('Cabin', 'Ticket'),
    dtype={
        'Pclass': 'category',
        'Sex': 'category',
        'Embarked': 'category'
    }
)
