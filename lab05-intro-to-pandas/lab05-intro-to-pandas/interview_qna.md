# Interview Q&A – Pandas Basics (10 Questions)

**Q1:** How do you load CSV into Pandas?  
**A1:** `pd.read_csv("file.csv")`

**Q2:** What does `head()` return?  
**A2:** First 5 rows of a DataFrame (can specify `head(10)` for 10 rows).

**Q3:** How do you check the shape of a dataset?  
**A3:** `df.shape` → returns (rows, columns).

**Q4:** How to rename columns in Pandas?  
**A4:** `df.rename(columns={"old":"new"}, inplace=True)`

**Q5:** How to drop duplicates from a DataFrame?  
**A5:** `df.drop_duplicates(inplace=True)`

**Q6:** How do you handle missing values?  
**A6:** Use `df.dropna()` to remove or `df.fillna(value)` to replace.

**Q7:** What’s the difference between `iloc` and `loc`?  
**A7:** `iloc` = index-based (numeric), `loc` = label-based (column/row names).

**Q8:** How to filter rows where Age > 30?  
**A8:** `df[df["Age"] > 30]`

**Q9:** How do you merge two DataFrames?  
**A9:** `pd.merge(df1, df2, on="column_name")`

**Q10:** What’s the benefit of `describe()`?  
**A10:** Provides quick statistics (mean, std, min, max, quartiles) for numerical columns.
