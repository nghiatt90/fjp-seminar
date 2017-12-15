import pandas as pd

pd.set_option('max.rows', 6)

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

data['Age'] = (data['Age'].fillna(data['Age'].mean())
                          .astype(int))
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
