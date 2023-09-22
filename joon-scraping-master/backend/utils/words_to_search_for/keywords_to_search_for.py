# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
import pandas as pd
from backend.utils.sanitize.sanitize_replace_space_remove_special import sanitize_replace_space_remove_special_function
# ------------------------ imports end ------------------------


# ------------------------ keywords_to_search_for_function function start ------------------------
def keywords_to_search_for_function():
  localhost_print_function(' ------------------------ keywords_to_search_for_function function start ------------------------ ')
  # ------------------------ pandas start ------------------------
  df = pd.read_csv('backend/csv/input/keywords.csv')
  # ------------------------ pandas end ------------------------
  # ------------------------ manipulation start ------------------------
  column_names = df.columns.values.tolist()
  column_names_clean = []
  for i in column_names:
    i = sanitize_replace_space_remove_special_function(i)
    column_names_clean.append(i)
  
  keywords_dict= {}
  for i in range(len(column_names_clean)):
    column_name = column_names_clean[i]
    specific_col_all_rows = df.iloc[:,i].values.tolist()
    col_set = {'a'}
    for distinct_i in specific_col_all_rows:
      if distinct_i not in col_set and type(distinct_i) != float:
        col_set.add(distinct_i)
    col_set.remove('a')
    keywords_dict[column_name] = col_set
  # ------------------------ manipulation end ------------------------
  localhost_print_function(' ------------------------ keywords_to_search_for_function function end ------------------------ ')
  return keywords_dict
# ------------------------ keywords_to_search_for_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__keywords_to_search_for_function__':
#   keywords_to_search_for_function()
# ------------------------ call end ------------------------