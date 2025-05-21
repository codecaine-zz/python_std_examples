import os
from pathlib import Path
from html import escape
import markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import json
import argparse

class EscapeHtml(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(
            EscapeHtmlPreprocessor(md), 'escape_html', 25)

class EscapeHtmlPreprocessor(Preprocessor):
    def run(self, lines):
        return [escape(line) for line in lines]

def convert_markdown_to_json(markdown_files_by_category):
    data = {}
    sorted_categories = sorted(
        markdown_files_by_category.keys(), key=lambda s: s.lower())
    for category in sorted_categories:
        files = markdown_files_by_category[category]
        safe_category = escape(category)
        data[safe_category] = []
        sorted_files = sorted(files, key=lambda s: s.lower())
        for file in sorted_files:
            safe_file = escape(file)
            file_path = Path(file)
            with file_path.open('r') as f:
                content = f.read()
            file_html_content = markdown.markdown(content, extensions=[
                'fenced_code', 'codehilite'
            ])
            data[safe_category].append({
                'filename': escape(file_path.name),
                'content': file_html_content
            })
    return data

def get_markdown_files_by_category(directory):
    markdown_files_by_category = {}
    for root, dirs, files in os.walk(directory):
        if root == directory:
            continue
        category = os.path.relpath(root, directory)
        markdown_files = [os.path.join(root, file)
                          for file in files if file.endswith(".md")]
        if markdown_files:
            markdown_files_by_category[category] = markdown_files
    return markdown_files_by_category

def save_json_file(content, output_file, output_dir='json_version'):
    """Save JSON content to the given output_dir with specified filename"""
    dir_path = Path(output_dir)
    dir_path.mkdir(parents=True, exist_ok=True)
    output_path = dir_path / output_file
    with output_path.open('w') as f:
        json.dump(content, f, indent=4)

def main():
    parser = argparse.ArgumentParser(description='Convert markdown files to a JSON document.')
    parser.add_argument('-i', '--input-dir', default='standard_library_documents',
                        help='Directory containing module markdown files')
    parser.add_argument('-o', '--output-dir', default='json_version',
                        help='Directory to save JSON file')
    parser.add_argument('-f', '--filename', default='python_std_bible.json',
                        help='Name of the output JSON file')
    args = parser.parse_args()

    if not os.path.isdir(args.input_dir):
        print(f"Error: Input directory '{args.input_dir}' does not exist.")
        return

    files_by_cat = get_markdown_files_by_category(args.input_dir)
    if not files_by_cat:
        print(f"No markdown files found in '{args.input_dir}'.")
        return

    data = convert_markdown_to_json(files_by_cat)
    save_json_file(data, args.filename, args.output_dir)
    print(f"JSON file generated: {args.output_dir}/{args.filename}")

if __name__ == '__main__':
    main()
