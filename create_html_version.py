import os
from pathlib import Path
from html import escape

def convert_markdown_to_html(markdown_files_by_category):
    # Define the HTML structure
    html_content = """
    <html>
    <head>
        <title>Python 3.12 Standard Library</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="A collection of standard library documents converted from markdown to HTML.">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css">
        <link rel="icon" href="favicon.png" type="image/png">
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 20px;
                background-color: #2e2e2e;
                color: #f4f4f4;
            }}
            h1, h2, h3 {{
                color: #f4f4f4;
                margin-top: 20px;
            }}
            ul {{
                list-style-type: none;
                padding: 0;
            }}
            li {{
                margin: 5px 0;
            }}
            a {{
                text-decoration: none;
                color: #1e90ff;
                border-bottom: 1px dashed #1e90ff;
                transition: color 0.3s, border-bottom-color 0.3s;
            }}
            a:hover {{
                color: #63a4ff;
                border-bottom-color: #63a4ff;
            }}
            pre {{
                background: #3e3e3e;
                padding: 10px;
                border: 1px solid #555;
                border-radius: 5px;
                overflow-x: auto;
                margin-top: 10px;
            }}
            code {{
                font-family: Consolas, "Courier New", monospace;
                color: #f4f4f4;
            }}
            button {{
                display: inline-block;
                margin-top: 10px;
                padding: 10px 15px;
                font-size: 14px;
                background-color: #1e90ff;
                color: #fff;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
            button:hover {{
                background-color: #1c86ee;
            }}
            #scrollToTopBtn {{
                position: fixed;
                bottom: 20px;
                right: 30px;
                display: none;
                padding: 10px 15px;
                font-size: 16px;
                background-color: #000;
                color: #fff;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                z-index: 1000;
            }}
            #scrollToTopBtn:hover {{
                background-color: #555;
            }}
            @media (max-width: 600px) {{
                body {{
                    padding: 10px;
                }}
                h1 {{
                    font-size: 24px;
                }}
                h2 {{
                    font-size: 20px;
                }}
                h3 {{
                    font-size: 18px;
                }}
                button {{
                    font-size: 12px;
                    padding: 8px 12px;
                }}
                #scrollToTopBtn {{
                    font-size: 14px;
                    padding: 8px 12px;
                }}
            }}
        </style>
    </head>
    <body>
        <h1>Python 3.12 Standard Library</h1>
        <hr>
        <ul>
            {category_links}
        </ul>
        <hr>
        {content_sections}
        
        <button id="scrollToTopBtn">Top</button>
    
        <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.3.0/marked.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
        <script>
            document.querySelectorAll('pre code').forEach((block) => {{
                hljs.highlightBlock(block);
            }});
            window.onscroll = function() {{
                var btn = document.getElementById("scrollToTopBtn");
                if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {{
                    btn.style.display = "block";
                }} else {{
                    btn.style.display = "none";
                }}
            }};
            document.getElementById("scrollToTopBtn").onclick = function() {{
                window.scrollTo({{ top: 0, behavior: 'smooth' }});
            }};
        </script>
    </body>
    </html>
    """.strip()

    category_links = ""
    content_sections = ""

    for category, files in markdown_files_by_category.items():
        safe_category = escape(category)
        category_links += f"<li><a href='#{safe_category}'>{safe_category}</a></li>"

    for category, files in markdown_files_by_category.items():
        safe_category = escape(category)
        content_sections += f"<h2 id='{safe_category}'>{safe_category}</h2><ul>"
        for file in files:
            safe_file = escape(file)
            file_path = Path(file)
            content_sections += f"<li><a href='#{safe_file}'>{escape(file_path.name)}</a></li>"
        content_sections += "</ul>"

        for file in files:
            safe_file = escape(file)
            file_path = Path(file)
            with file_path.open('r') as f:
                content = f.read()
            content_sections += f"""
<h3 id='{safe_file}'>{escape(file_path.name)}</h3>
<button onclick="history.back()">Back</button>
<pre><code>{escape(content)}</code></pre>
"""

    return html_content.format(category_links=category_links, content_sections=content_sections)

import markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
from markdown.extensions.codehilite import CodeHiliteExtension
import re

class EscapeHtml(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(EscapeHtmlPreprocessor(md), 'escape_html', 25)

class EscapeHtmlPreprocessor(Preprocessor):
    def run(self, lines):
        return [escape(line) for line in lines]

def get_markdown_files_by_category(directory):
    markdown_files_by_category = {}
    for root, dirs, files in os.walk(directory):
        if root == directory:
            continue
        category = os.path.relpath(root, directory)
        markdown_files = [os.path.join(root, file) for file in files if file.endswith(".md")]
        if markdown_files:
            markdown_files_by_category[category] = markdown_files
    return markdown_files_by_category

def save_html_file(content, output_file):
    output_dir = Path("html_version")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / output_file
    with open(output_path, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    directory = "standard_library_documents"
    output_file = "standard_library_documents.html"
    
    markdown_files_by_category = get_markdown_files_by_category(directory)
    html_content = convert_markdown_to_html(markdown_files_by_category)
    save_html_file(html_content, output_file)
    print(f"HTML file generated: html_version/{output_file}")
