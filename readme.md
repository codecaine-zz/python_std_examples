Python standard library code examples using AI

This application generates code examples for Python's standard library modules using AI. The code examples are generated using the qwen2.5-coder:3b model.

## How to Use

1. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Ensure the `ollama` service is running.
3. Run the main script to generate individual module examples:
   ```bash
   python main.py [--force]
   ```
   Use `--force` to overwrite existing example files.
4. The markdown files for each standard library module will be created under the `standard_library_documents` directory.
5. Optionally, generate a single merged markdown document:
   ```bash
   python create_markdown_version.py
   ```
   The combined file `markdown_version/python_std_bible.md` will be created.
6. Optionally, generate a JSON version:
   ```bash
   python create_json_version.py
   ```
   The file `json_version/python_std_bible.json` will be created.
7. Optionally, add table of contents to all markdown files:

   ```bash
   python add_table_of_contents.py
   ```

   This will automatically add a Table of Contents section to each markdown file in the `standard_library_documents` directory, making navigation easier within each document.

8. Optionally, generate an HTML version:

   ```bash
   python create_html_version.py
   ```

   The file `html_version/index.html` will be created with interactive navigation and copy buttons.
9. You can add or remove modules in `main.py` under the `standard_library` dictionary to customize the examples.

## Application Demo

Check out the demo of this application [here](https://codefreelance.net/apps/python_std_bible/).

### Development Notes

You can use Copilot edits to refactor the `standard_library_documents` to improve examples if needed.
