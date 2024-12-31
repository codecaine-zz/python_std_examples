import os
from pathlib import Path
from html import escape
import markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import json

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

def save_json_file(content, output_file):
    output_dir = Path("json_version")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / output_file
    with open(output_path, 'w') as f:
        json.dump(content, f, indent=4)

if __name__ == "__main__":
    directory = "standard_library_documents"
    output_file = "index.json"

    markdown_files_by_category = get_markdown_files_by_category(directory)
    json_content = convert_markdown_to_json(markdown_files_by_category)
    save_json_file(json_content, output_file)
    print(f"JSON file generated: json_version/{output_file}")
