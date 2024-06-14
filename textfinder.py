import os
import argparse
import time
import multiprocessing
import json
import csv
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from tabulate import tabulate
from colorama import Fore, init

init(autoreset=True)

def search_text_in_file(file_path: str, text_list: list, use_regex: bool, case_insensitive: bool):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if case_insensitive:
                content = content.lower()
                text_list = [text.lower() for text in text_list]
            found_words = []
            for text in text_list:
                if use_regex:
                    if re.search(text, content):
                        found_words.append(text)
                else:
                    if text in content:
                        found_words.append(text)
            if found_words:
                return file_path, found_words
    except UnicodeDecodeError:
        pass
    except Exception as e:
        print(f"{Fore.RED}Error reading {file_path}: {e}")
    return None

def search_text_in_directory(directory: str, text_list: list, omit_list: list, num_threads: int, use_regex: bool, case_insensitive: bool):
    results = []
    file_paths = []

    for root, dirs, files in os.walk(directory):
        if not any(omit in root for omit in omit_list):
            for file in files:
                file_path = os.path.join(root, file)
                file_paths.append(file_path)

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = {executor.submit(search_text_in_file, file_path, text_list, use_regex, case_insensitive): file_path for file_path in file_paths}
        for future in as_completed(futures):
            result = future.result()
            if result:
                file_path, found_words = result
                results.append([os.path.dirname(file_path), os.path.basename(file_path), ', '.join(found_words)])

    return results

def threads_to_run(args_num_threads: int) -> int:
    num_threads = args_num_threads if args_num_threads > 0 else 1
    max_threads = multiprocessing.cpu_count()
    if num_threads > max_threads:
        print(f"{Fore.YELLOW}The specified number of threads ({num_threads}) exceeds the available CPUs ({max_threads}). Using {max_threads} threads instead.")
        return max_threads
    
    return num_threads

def save_results(results, output_format, output_file):
    if output_format == 'json':
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
    elif output_format == 'csv':
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Folder path", "File", "Found words"])
            writer.writerows(results)

def main():
    parser = argparse.ArgumentParser(description="To search for text in files within a directory.")
    parser.add_argument('-p', '--path', type=str, required=True, help='Absolute or relative path of the directory.')
    parser.add_argument('-t', '--text', action='append', required=True, help='Text to search for in the files, can be specified multiple times.')
    parser.add_argument('-o', '--omit', action='append', help='Folder to exclude, can be specified multiple times.')
    parser.add_argument('-n', '--num-threads', type=int, default=1, help='Number of threads to use for the search (default is 1).')
    parser.add_argument('-r', '--regex', action='store_true', help='Use regular expressions for searching.')
    parser.add_argument('-c', '--case-insensitive', action='store_true', help='Perform case insensitive search.')
    parser.add_argument('-f', '--output-format', type=str, choices=['json', 'csv'], help='Format to save the results (json or csv).')
    parser.add_argument('-O', '--output-file', type=str, help='File to save the results.')

    args = parser.parse_args()

    text_list = args.text if args.text else []
    omit_list = args.omit if args.omit else []
    num_threads = threads_to_run(args.num_threads)

    start = time.time()
    results = search_text_in_directory(args.path, text_list, omit_list, num_threads, args.regex, args.case_insensitive)
    end = time.time()

    if results:
        print(tabulate(results, headers=["Folder path", "File", "Found words"], tablefmt="grid"))
        print(f"{Fore.GREEN}Found: {len(results)} matches")
        if args.output_format and args.output_file:
            save_results(results, args.output_format, args.output_file)
            print(f"{Fore.CYAN}Results saved to {args.output_file}")
    else:
        print(f"{Fore.YELLOW}No matches found.")
    
    print(f"{Fore.CYAN}Number of Threads: {num_threads}")
    print(f"{Fore.CYAN}Search duration: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
