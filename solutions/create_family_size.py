data['FamilySize'] = data['SibSp'] + data['Parch'] + 1  # Cộng thêm cả bản thân người đó nữa
data.drop(columns=['SibSp', 'Parch'], inplace=True)