# **Laboratory 5**

Create your own  dataset.

**Goal**: Write a Python script that creates visual comparisons using matplotlib, seaborn, and pandas.


## **What You Need to Do**:
1. **Create a Dataset**: Makeup sales data for 3 product categories across 6 months. Add one column for sales and one for region. Tip: Introduce 1–2 missing or inconsistent values (e.g. a typo in a category name, a missing sales value).
2. **Clean the Data**
>* Fix category name typos (e.g. "Electrnics" → "Electronics")
>* Fill or remove missing values
>* Make sure "Sales" is numeric
3. **Make These Charts**:
>* A **bar chart**: Total sales by category
>* A **line chart**: Sales over months for each region
>* A **box plot**: Sales distribution by category
>* A **heatmap**: Average sales per region per month
4. **Customize Each Chart**: Add clear titles, axis labels, and color themes using sns.set_style() or plt.style.use().
5. **Bonus (Optional)**
>* Highlight the month with the highest total sales using an annotation
>* Save one chart as an image (e.g., plt.savefig("line_chart.png"))
