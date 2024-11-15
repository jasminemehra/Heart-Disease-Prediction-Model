#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing libraries
import pandas as pd


# In[2]:


#importing data set
df = pd.read_csv("heart.csv")
df


# In[3]:


# Taking care of missiong values


# In[4]:


# Taking care of duplicate values
df.duplicated().any


# In[5]:


# droping duplicate values
df = df.drop_duplicates()

# rechecking for duplicate values
df.duplicated().any()


# In[6]:


# pre processing
cat_val = []
cont_val = []

for column in df.columns:
    if df[column].nunique() <= 10:
        cat_val.append(column)
    else:
        cont_val.append(column)

print("Categorical-->",cat_val)
print("Continuous-->",cont_val)


# In[7]:


# Encoding Categorical Data
cat_val

# Checking for the need of encoding
print(df.cp.unique())
print(df.exang.unique())
print(df.sex.unique())
print(df.target.unique())


# In[8]:


#Removing "sex","exang" and "target" from cat_val as encoding is not required in them

cat_val.remove('sex')
cat_val.remove('target')
cat_val.remove('exang')
# dummies for'cp','fbc','restecg','slope','ca','thal'
df = pd.get_dummies(df,columns=cat_val,drop_first=True)


# In[9]:


df.head()


# In[10]:


# feature Scalling
df.head()


# In[11]:


from sklearn.preprocessing import StandardScaler

st = StandardScaler()
df[cont_val] = st.fit_transform(df[cont_val])

df.head()


# In[12]:


#-----------------training and testing data----------------------

x = df.drop('target',axis=1)
y = df['target']


# In[13]:


# Splitting of training and testing data  

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)


# In[14]:


#Applying------------ (Logistic Regression)----------------------

from sklearn.linear_model import LogisticRegression

log = LogisticRegression()
log.fit(x_train,y_train)

y_pred1 = log.predict(x_test)


# Accuracy
from sklearn.metrics import accuracy_score

print("Logistic Regression Accuracy:",accuracy_score(y_test,y_pred1))


# In[15]:


# SVC

from sklearn import svm

svm = svm.SVC()

svm.fit(x_train,y_train)
y_pred2 = svm.predict(x_test)

# Accuracy
print("Accuracy",accuracy_score(y_test,y_pred2))


# In[16]:


# Knn classifier

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(x_train,y_train)
y_pred3 = knn.predict(x_test)

# Accuracy
print("KNN Accuracy",accuracy_score(y_test,y_pred3))


# In[17]:


# checking for best k value
score = []

for k in range(1,40):
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    y_pred3=knn.predict(x_test)
    score.append(accuracy_score(y_test,y_pred3))


# In[18]:


score


# In[19]:


knn=KNeighborsClassifier(n_neighbors=2)
knn.fit(x_train,y_train)
y_pred=knn.predict(x_test)
print("Knn Accuracy--->",accuracy_score(y_test,y_pred))


# In[20]:


final_data = pd.DataFrame({'Models':['LR','SVM','KNN'],
                           'ACC':[accuracy_score(y_test,y_pred1),
                                 accuracy_score(y_test,y_pred2),
                                 accuracy_score(y_test,y_pred3)]})
final_data


# In[21]:


# Visualizing the accuracies

import seaborn as sns

sns.barplot(final_data['Models'],final_data['ACC'])


# In[22]:


# Random Forest Algorithm   

data = pd.read_csv("heart.csv")
data =data.drop_duplicates()

x=data.drop('target',axis=1)
y=data['target']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)


# In[23]:


from sklearn.ensemble import RandomForestClassifier
rf  =RandomForestClassifier()
rf.fit(x_train,y_train)


# In[24]:


y_pred4 = rf.predict(x_test)

print("RF",accuracy_score(y_test,y_pred4))


# In[25]:


# Visualizing the accuracies

import seaborn as sns
final_data = pd.DataFrame({'Models':['LR','SVM','KNN','RF'],
                           'ACC':[accuracy_score(y_test,y_pred1),
                                 accuracy_score(y_test,y_pred2),
                                 accuracy_score(y_test,y_pred3),
                                 accuracy_score(y_test,y_pred4)]})

sns.barplot(final_data['Models'],final_data['ACC'])


# In[26]:


# As Ranforest has the best accuracy we are goint to use it for our Model

x=data.drop('target',axis=1)
y=data['target']

rf = RandomForestClassifier()
rf.fit(x,y)


# In[27]:


# Saving model using joblib to use in the interface
import joblib

joblib.dump(rf,'model_joblib_heart')


# In[28]:


model = joblib.load('model_joblib_heart')


# In[29]:


data


# In[ ]:




