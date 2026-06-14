from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

titanic = sns.load_dataset('titanic')

titanic = titanic[['survived','sex','age']]

titanic['age']=titanic['age'].fillna(titanic['age'].mean(), inplace=True)
titanic['sex'] = le.fit_transform(titanic['sex'])

x = titanic.drop('survived', axis=1)
y = titanic['survived']

x_train, x_test, y_tr, y_test = train_test_split(
    x, y, test_size=0.3, random_state=48
)

model = GaussianNB()
model.fit(x_train, y_tr)

y_pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
x_train, x_test, y_tr, y_test = train_test_split(
    x, y, test_size=0.1, random_state=48
)

model = GaussianNB()
model.fit(x_train, y_tr)

y_pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, y_pred))