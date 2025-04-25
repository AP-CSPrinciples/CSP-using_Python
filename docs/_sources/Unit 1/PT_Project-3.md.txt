# Performance Task - Project 3


---

## 📊 Python Charts & Graphs Project Guide

🧠 Project Overview  
In this project, teams of **2–3 students** will explore real-world data and create **Python visualizations** using libraries like Matplotlib, Pandas, and Seaborn. You'll pick a topic, analyze a dataset, and create charts to communicate insights visually.

Project Tasks:
- Select a topic and explain **why** it interests you  
- Load, clean, and analyze your dataset  
- Create **at least 3 types of charts**  
- Write a summary of your insights and how the visuals helped you understand the data  

---

### ✅ Project Requirements

Your final Notebook (Jupyter, CoLab, other) should include:
- Clear explanation of your **topic and purpose**
- **Clean, labeled data** (no missing values)
- **Three+ chart types** (bar, line, scatter, pie, etc.)
- Labeled axes, meaningful titles, and legible visuals
- A **summary of your findings**

---

### 📚 Why Use Charts and Graphs?

Charts turn complex numbers into simple visuals. They help you:
1. **Understand Data Faster** – See trends or comparisons instantly
2. **Spot Patterns** – Detect increases, decreases, or outliers
3. **Compare Categories** – Visually contrast different values
4. **Communicate Clearly** – Make reports and presentations more engaging

---

### 🔍 Introduction to Python Charts

Python is ideal for data visualization. Libraries you'll use:
- **Matplotlib** – Basic charting
- **Pandas** – Built-in plotting support
- **Seaborn** – Advanced, stylish visuals

Just a few lines of code can turn a spreadsheet into an insightful chart.

---

### 📊 Types of Charts & When to Use Them

| Chart Type        | Use Case                                               | Python Example                                           |
|------------------|--------------------------------------------------------|----------------------------------------------------------|
| **Bar Chart**     | Compare quantities across categories                   | `data['col'].value_counts().plot(kind='bar')`           |
| **Pie Chart**     | Show proportions or percentages                        | `data['col'].value_counts().plot(kind='pie')`           |
| **Line Chart**    | Show trends over time                                  | `data.plot(x='Date', y='Value', kind='line')`           |
| **Histogram**     | Show distribution of one variable                      | `data['col'].plot(kind='hist')`                         |
| **Scatter Plot**  | Show relationship between two variables                | `data.plot(kind='scatter', x='X', y='Y')`                |
| **Box Plot**      | Show data spread and detect outliers                   | `data.boxplot(column='Value', by='Group')`              |
| **Heatmap (Seaborn)** | Show correlation or intensity                      | `sns.heatmap(data.corr(), annot=True)`                  |

---

### 📚 Suggested Dataset Topics

Your dataset should have:
- **200+ rows**
- **At least 4 columns** (e.g., category, value, date, region)

🎓 Education
- [Student Performance (Kaggle)](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

🌍 Demographics & Income
- [U.S. Census Income Data (UCI)](https://archive.ics.uci.edu/ml/datasets/adult)

🏀 Sports
- [NBA Player Stats (Basketball Reference)](https://www.basketball-reference.com/leagues/)

🍟 Health & Nutrition
- [Fast Food Nutrition (Kaggle)](https://www.kaggle.com/datasets/brandenciranni/fast-food-nutrition)

🎬 Pop Culture
- [IMDb Top 1000 Movies (Kaggle)](https://www.kaggle.com/datasets/iamsouravbanerjee/top-1000-imdb-movies)

---

### 📘 Jupyter Notebook Starter Template

Step 1: Import Libraries
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

Step 2: Load Your Dataset
```python
data = pd.read_csv('your_dataset.csv')
data.head()
```

Step 3: Explore the Data
```python
print(data.columns)
print(data.describe())
print(data.isnull().sum())
```

Step 4: Create Charts

**Bar Chart**
```python
data['Category'].value_counts().plot(kind='bar')
plt.title('Category Distribution')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
```

**Line Chart**
```python
data['Date'] = pd.to_datetime(data['Date'])
data.groupby('Date')['Value'].mean().plot(kind='line')
plt.title('Time Trend')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
```

**Scatter Plot**
```python
data.plot(kind='scatter', x='X_Column', y='Y_Column', alpha=0.6)
plt.title('X vs Y Relationship')
plt.show()
```

**Heatmap**
```python
# Seaborn
plt.figure(figsize=(8,6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
```

---

### 💡 Project Ideas

- **Trend Analysis** – Use line charts to show changes over time
- **Category Comparison** – Use bar/pie charts to compare groups
- **Correlation Study** – Use scatter plots for relationships
- **Distribution Analysis** – Use histograms/box plots to explore a variable
- **Geographic Comparison** – Use heatmaps if you have location data

---

💻 Jupyter vs Google Colab

| Feature         | **Jupyter Notebook**                 | **Google Colab**                          |
|----------------|--------------------------------------|-------------------------------------------|
| Setup          | Installed locally                    | Runs in browser                           |
| Sharing        | Manual (file-based)                  | Google Drive integration                  |
| Installation   | Required                             | None                                      |
| Speed          | Depends on your computer             | Uses Google’s servers                     |
| Best For       | Offline work, full control           | Beginners, Chromebooks, quick setup       |

**Recommendation**: Start with **Google Colab**—no install, easy to use, and perfect for teams!

---

#### 🎯 Grading Rubric (20 Points)

| Category                       | Points | Description                                      |
|-------------------------------|--------|--------------------------------------------------|
| Topic & Purpose               | 4      | Clear, thoughtful topic explanation              |
| Data Use & Cleaning           | 4      | Relevant dataset, cleaned and prepared           |
| Chart Variety & Accuracy      | 6      | At least 3 clear, well-labeled chart types       |
| Insight & Interpretation      | 4      | Analysis clearly explained and interpreted       |
| Collaboration & Presentation  | 2      | Teamwork, clear formatting, easy to follow       |

---


