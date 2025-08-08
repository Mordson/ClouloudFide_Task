import pandas as pd
import re


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
 
    # Validate new_column name - must contain only letters and underscores
    if not re.match(r'^[a-zA-Z_]+$', new_column):
        return pd.DataFrame()
    
    # Validate existing column names - must contain only letters and underscores
    for col in df.columns:
        if not re.match(r'^[a-zA-Z_]+$', col):
            return pd.DataFrame()
    
    # Clean the role string by removing extra spaces
    role = role.strip()
    
    # Validate role - check for invalid characters
    # Only allow letters, underscores, spaces, +, -, *, and parentheses
    if not re.match(r'^[a-zA-Z_\s+\-*()]+$', role):
        return pd.DataFrame()
    
    # Extract column names from the role
    # Find all sequences of letters and underscores
    column_names_in_role = re.findall(r'[a-zA-Z_]+', role)
    
    # Check if all column names in the role exist in the DataFrame
    for col_name in column_names_in_role:
        if col_name not in df.columns:
            return pd.DataFrame()
    
    try:
        # Create a copy of the DataFrame to avoid modifying the original
        result_df = df.copy()
        
        # Replace column names in the role with df['column_name']
        eval_expression = role
        for col_name in df.columns:
            # Use word boundaries to match exact column names
            pattern = r'\b' + re.escape(col_name) + r'\b'
            replacement = f"result_df['{col_name}']"
            eval_expression = re.sub(pattern, replacement, eval_expression)
        
        # Calculate the new column values 
        result_df[new_column] = eval(eval_expression)
        
        return result_df
        
    except Exception:
        # If any error occurs during evaluation, return empty DataFrame
        return pd.DataFrame()
