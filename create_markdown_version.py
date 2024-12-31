import os
from pathlib import Path

def merge_markdown_files(markdown_files_by_category):
    merged_content = ""
    sorted_categories = sorted(
        markdown_files_by_category.keys(), key=lambda s: s.lower())
    for category in sorted_categories:
        files = markdown_files_by_category[category]
        safe_category = category.replace("#", "").replace(" ", "_")
        merged_content += f"# {safe_category}\n\n"
        sorted_files = sorted(files, key=lambda s: s.lower())
        for file in sorted_files:
            file_path = Path(file)
            with file_path.open('r') as f:
                content = f.read()
            merged_content += f"## {file_path.name}\n\n"
            merged_content += content + "\n\n"
    return merged_content

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

def save_markdown_file(content, output_file):
    output_dir = Path("markdown_version")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / output_file
    with open(output_path, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    directory = "standard_library_documents"
    output_file = "python_std_bible.md"

    markdown_files_by_category = get_markdown_files_by_category(directory)
    merged_content = merge_markdown_files(markdown_files_by_category)
    save_markdown_file(merged_content, output_file)
    print(f"Markdown file generated: markdown_version/{output_file}")
