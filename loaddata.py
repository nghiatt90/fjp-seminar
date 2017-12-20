import pandas as pd
import copy
import re


pd.set_option('max.rows', 14)

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


def get_title_from_name(name):
    m = re.search(' ([A-Za-z]*)\.', name)
    if not m:
        raise ValueError(f'Name doesn\'t match pattern: {name}')
    return m.group(1)


data_engineered = data.copy(deep=True)
data_engineered['Title'] = (data['Name'].apply(get_title_from_name)
                                        .astype('category')
                                        .cat.set_categories(('Mr', 'Mrs', 'Miss', 'Master', 'High Standing'))
                                        .fillna('High Standing'))

data_engineered['FamilySize'] = data_engineered['SibSp'] + data_engineered['Parch'] + 1
data_engineered.drop(columns=['Name', 'SibSp', 'Parch'], inplace=True)
