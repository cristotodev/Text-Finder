"""
Class responsible for processing the content of files
"""

import re

class FileProcessor:
    def __init__(self, use_regex=False, case_insensitive=False):
        self.use_regex = use_regex
        self.case_insensitive = case_insensitive

    def process_file(self, file_path: str, text_list: list) -> tuple[str, list] | None:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if self.case_insensitive:
                content = content.lower()
                text_list = [text.lower() for text in text_list]

            found_words = []
            for text in text_list:
                if self.use_regex:
                    if re.search(text, content):
                        found_words.append(text)
                else:
                    if text in content:
                        found_words.append(text)

            if found_words:
                return file_path, found_words
            
        return None
