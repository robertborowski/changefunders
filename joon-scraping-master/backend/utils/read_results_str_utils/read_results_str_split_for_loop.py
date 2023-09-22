# ------------------------ imports start ------------------------
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
# ------------------------ imports end ------------------------


# ------------------------ read_results_str_split_for_loop_function function start ------------------------
def read_results_str_split_for_loop_function():
  localhost_print_function(' ------------------------ read_results_str_split_for_loop_function function start ------------------------ ')
  # ------------------------ manipulation start ------------------------
  # just an example/test for total number of proof's aligns with columns marked as true in csv/excel  
  input_str = ',[[[-keywords_careers_href_1: https://www.chronicled.com/careers[[[-keyword_benefits_found_on_page: stipend[[[-keyword_benefits_found_on_page: reimbursement[[[-master_str_benefit_html_found: - img src="https://global-uploads.webflow.com/5e387f889619c769a1b2ed3d/5e387f889619c76b02b2f0ec_icon-gym-membership.svg" alt="gym stipend" class="icon"><h5>gym stipend<p>get your body strong after flexing your brains all day. chronicled offers a gym stipend for all team members.<p>we offer reimbursements for conference attendance and learning experiences. we encourage peer learning opportunities and provide access to resources to help you grow your skills.<[[[-keyword_category_found_on_page: gym[[[-keyword_category_found_on_page: learning[[[-keyword_category_found_on_page: desk[[[-scrape_benefit_category_proof: word: gym | phrase: master_str_benefit_html_found: - img src="https://global-uploads.webflow.com/5e387f889619c769a1b2ed3d/5e387f889619c76b02b2f0ec_icon-gym-membership.svg" alt="gym stipend" class="icon"><h5>gym stipend<p>get your body strong after flexing your brains all day. chronicled offers a gym stipend for all team members.<p>we offer reimbursements for conference attendance and learning experiences. we encourage peer learning opportunities and provide access to resources to help you grow your skills.<[[[-scrape_benefit_category_proof: word: learning | phrase: master_str_benefit_html_found: - img src="https://global-uploads.webflow.com/5e387f889619c769a1b2ed3d/5e387f889619c76b02b2f0ec_icon-gym-membership.svg" alt="gym stipend" class="icon"><h5>gym stipend<p>get your body strong after flexing your brains all day. chronicled offers a gym stipend for all team members.<p>we offer reimbursements for conference attendance and learning experiences. we encourage peer learning opportunities and provide access to resources to help you grow your skills.<'

  split_arr = input_str.split('[[[-')
  for i_str in split_arr:
    if 'proof' in i_str:
      localhost_print_function(i_str)
  # ------------------------ manipulation end ------------------------
  localhost_print_function(' ------------------------ read_results_str_split_for_loop_function function end ------------------------ ')
  return True
# ------------------------ read_results_str_split_for_loop_function function end ------------------------


# ------------------------ call start ------------------------
# if __name__ == '__main__':
#   read_results_str_split_for_loop_function()
# ------------------------ call end ------------------------