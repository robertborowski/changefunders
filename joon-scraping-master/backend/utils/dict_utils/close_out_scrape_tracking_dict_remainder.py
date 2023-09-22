# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
# ------------------------ imports end ------------------------


# ------------------------ close_out_scrape_tracking_dict_remainder_function function start ------------------------
def close_out_scrape_tracking_dict_remainder_function(scrape_tracking_dict):
  localhost_print_function(' ------------------------ close_out_scrape_tracking_dict_remainder_function function start ------------------------ ')

  # ------------------------ a start ------------------------
  current_max = 0
  total_cols_closed_out = 0

  for k, v in scrape_tracking_dict.items():
    item = k
    i_len_arr = len(v)
    
    if i_len_arr > current_max:
      current_max = i_len_arr
    
    if i_len_arr < current_max:
      scrape_tracking_dict[k].append(False)
      total_cols_closed_out += 1
      localhost_print_function(f'live_check_print_02.00: {k} = False, force closed out. Total cols closed out so far: {total_cols_closed_out}')
      
  # ------------------------ a end ------------------------

  localhost_print_function(' ------------------------ close_out_scrape_tracking_dict_remainder_function function end ------------------------ ')
  return scrape_tracking_dict
# ------------------------ close_out_scrape_tracking_dict_remainder_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__close_out_scrape_tracking_dict_based_reruns_function__':
#   close_out_scrape_tracking_dict_remainder_function()
# ------------------------ call end ------------------------