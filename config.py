queries = [
    "Chief Marketing Officer",
    "VP Marketing",
    "Director Marketing",
    "Marketing Manager"
]
number_of_results = 2
delay_in_seconds = 2
common_queries = "LinkedIn"

final_base_query_list = ["{} {}".format(a, common_queries) for a in queries]

# Example usage (paths need to be adjusted as per the actual file locations)
input_path = 'input_file.txt'
output_path = 'output_file.csv'
output_path_xlsx = 'output_file.xlsx'
