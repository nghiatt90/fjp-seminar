import pandas as pd


# Chạy lại code từ đầu để đảm bảo không bị ảnh hưởng bởi code exercise
pd.set_option('max.rows', 6)

data = pd.read_csv('data/titanic_train.csv')
data.set_index('PassengerId', inplace=True)
data.drop(columns=['Cabin', 'Ticket'], inplace=True)
data['Age'].fillna(data['Age'].mean(), inplace=True)

# Ở đây mình chọn input giá trị vào 2 ô thiếu
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.info()
