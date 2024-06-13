"""
A tool to search for text in files within specific directories.
"""

import os
import argparse
import time
from tabulate import tabulate
from colorama import Fore, init

init(autoreset=True)

def search_text_in_files(directory: str, text_list: list, omit_list: list):
    results = []
    for root, dirs, files in os.walk(directory):
        if not any(omit in root for omit in omit_list):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        found_words = [text for text in text_list if text in content]
                        if found_words:
                            results.append([root, file, ', '.join(found_words)])
                except UnicodeDecodeError:
                    continue
                except Exception as e:
                    print(f"{Fore.RED}Error reading {file_path}: {e}")
    return results

def main():
    parser = argparse.ArgumentParser(description="To search for text in files within a directory.")
    parser.add_argument('-p', '--path', type=str, required=True, help='Absolute or relative path of the directory.')
    parser.add_argument('-t', '--text', action='append', required=True, help='Text to search for in the files, can be specified multiple times.')
    parser.add_argument('-o', '--omit', action='append', help='Folder to exclude, can be specified multiple times.')
    args = parser.parse_args()

    text_list = args.text if args.text else []
    omit_list = args.omit if args.omit else []

    start = time.time()
    results = search_text_in_files(args.path, text_list, omit_list)
    end = time.time()

    if results:
        print(tabulate(results, headers=["Folder path", "File", "Found words"], tablefmt="grid"))
        print(f"{Fore.GREEN}Found: {len(results)} matches")
    else:
        print(f"{Fore.YELLOW}No matches found.")
    
    print(f"{Fore.CYAN}Search duration: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
