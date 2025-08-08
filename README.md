# Virtual Column Task - Solution

## 📋 Description

The `add_virtual_column()` function creates a new pandas DataFrame with an additional virtual column calculated based on a mathematical expression.

## 🚀 Usage

```python
import pandas as pd
from solution import add_virtual_column

# Sample data
df = pd.DataFrame({
    'quantity': [10, 3, 5],
    'price': [2, 5, 8]
})

# Add virtual column
result = add_virtual_column(df, "quantity * price", "total")
print(result)
```

**Output:**
```
   quantity  price  total
0        10      2     20
1         3      5     15
2         5      8     40
```

## ⚙️ Parameters

- `df` (pd.DataFrame): Any pandas DataFrame
- `role` (str): Mathematical expression (e.g. "column1 + column2")
- `new_column` (str): Name of the new column

## 🔧 Supported Operations

- **Addition**: `+`
- **Subtraction**: `-`  
- **Multiplication**: `*`
- **Parentheses**: `()` for grouping

## ✅ Validation

### Column names:
- Only letters (a-z, A-Z) and underscores (_)
- ❌ No digits, spaces, or special characters

## 👨‍💻 Author

Solution for Cloudfide recruitment task.
