from finder import search_and_find_links
from config import final_base_query_list

def process_line(line):
    clean_line = line.strip()
    final_results = []
    for final_base_query in final_base_query_list:
        final_query = "{} {}".format(clean_line, final_base_query)
        search_links = search_and_find_links(final_query)
        final_results.append("{},{},{}".format(clean_line, final_base_query, search_links))
    return final_results

# Function to read from one file, process each line, and write to another file
def process_file(input_file_path, output_file_path):
    count = 1
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            try:
                print("Processing brand count: {}".format(count))
                processed_lines = process_line(line)
                for processed_line in processed_lines:
                    output_file.write("{}\n".format(processed_line))
                count = count + 1
            except:
                print("Error while processing: {}".format(line))
            output_file.write("{}\n".format("error while processing"))

# Example usage (paths need to be adjusted as per the actual file locations)
input_path = 'input_file.txt'
output_path = 'output_file.txt'

# Call the function
process_file(input_path, output_path)