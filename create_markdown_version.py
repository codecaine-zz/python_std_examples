import os
import argparse  # added for CLI arguments
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

def save_markdown_file(content, output_file, output_dir='markdown_version'):
    """Save merged markdown to the given output_dir with output_file name"""
    dir_path = Path(output_dir)
    dir_path.mkdir(parents=True, exist_ok=True)
    output_path = dir_path / output_file
    with output_path.open('w') as f:
        f.write(content)

def main():
    parser = argparse.ArgumentParser(description='Merge individual markdown files into one document.')
    parser.add_argument('-i', '--input-dir', default='standard_library_documents',
                        help='Directory containing module markdown files')
    parser.add_argument('-o', '--output-dir', default='markdown_version',
                        help='Directory to save merged markdown file')
    parser.add_argument('-f', '--filename', default='python_std_bible.md',
                        help='Name of the merged markdown file')
    args = parser.parse_args()

    if not os.path.isdir(args.input_dir):
        print(f"Error: Input directory '{args.input_dir}' does not exist.")
        return

    files_by_cat = get_markdown_files_by_category(args.input_dir)
    if not files_by_cat:
        print(f"No markdown files found in '{args.input_dir}'.")
        return

    merged = merge_markdown_files(files_by_cat)
    save_markdown_file(merged, args.filename, args.output_dir)
    print(f"Markdown file generated: {args.output_dir}/{args.filename}")

if __name__ == '__main__':
    main()
