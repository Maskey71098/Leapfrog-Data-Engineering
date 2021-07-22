# Leapfrog-Data-Engineering

## Installation   
```
pip install pandas   
```
___

## Library Used   

**Pandas** is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.   
Read the documentation [here][1].   

[1]:<https://pandas.pydata.org/docs/> "here"   

___

### **Step 1** : Importing the library   

```
import pandas as pd
```   
<br>

### **Step 2** : Importing the dataset   
```
dataset = pd.read_csv('Data.csv')
```   
>Note: The dummy dataset created for this problem is named 'Data.csv'.  

<br>

![Dummy Dataset](https://raw.githubusercontent.com/Maskey71098/Leapfrog-Data-Engineering/main/assets/dataset.png "Dummy Dataset")   

<br>

### **Step 3** : Selecting the specific criteria i.e Extracting students failed in both maths and science   

```
specific_criteria = dataset[(dataset['science'] < 50) & (dataset['maths'] < 50)]
```
>Interpretation: Inside dataset, select rows whose "science" column has less than 50 value AND "maths" has less than 50 value.   

<br>

### **Step 4** : Printing the output   
 ```
 print(specific_criteria)
 ```
<br>

![Output](https://raw.githubusercontent.com/Maskey71098/Leapfrog-Data-Engineering/main/assets/output.png "Output")   

___
___
