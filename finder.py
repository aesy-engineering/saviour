from googlesearch import search
import time
from config import delay_in_seconds,number_of_results


def search_and_find_links(search_query):
    results = search(search_query, num_results=number_of_results)
    #print("Scanning the internet...")
    time.sleep(delay_in_seconds)
    yielded = list(results)
    return yielded