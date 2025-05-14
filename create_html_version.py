import os
from pathlib import Path
from html import escape
import markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor
import re


class EscapeHtml(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(
            EscapeHtmlPreprocessor(md), 'escape_html', 25)


class EscapeHtmlPreprocessor(Preprocessor):
    def run(self, lines):
        return [escape(line) for line in lines]


class AddCopyButtonPostprocessor(Postprocessor):
    def run(self, text):
        # Insert copy button after opening <pre> tag and before <code> tag
        pattern = r'(<pre[^>]*>)'
        replacement = r'\1<button class="copy-btn">Copy</button>'
        return re.sub(pattern, replacement, text)


class CopyButtonExtension(Extension):
    def extendMarkdown(self, md):
        md.postprocessors.register(
            AddCopyButtonPostprocessor(), 'add_copy_button', 25)


def convert_markdown_to_html(markdown_files_by_category):
    # Define the HTML structure
    html_content = """
    <html>
    <head>
        <title>Python 3.12 Standard Library Bible</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="A collection of standard library documents converted from markdown to HTML.">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css">
        <link rel="icon" href="favicon.png" type="image/png">
        <style>
            html {{ scroll-behavior: smooth; }}
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 20px;
                background-color: #f4f4f4;
                color: #2e2e2e;
            }}
            h1, h2, h3 {{
                color: #2e2e2e;
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
                background: #f4f4f4;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                overflow-x: auto;
                margin-top: 10px;
                position: relative;
            }}
            code {{
                font-family: Consolas, "Courier New", monospace;
                color: #2e2e2e;
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
            .copy-btn {{
                position: absolute;
                top: 10px;
                right: 10px;
                padding: 5px 10px;
                font-size: 12px;
                background-color: #1e90ff;
                color: #fff;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
            .copy-btn:hover {{
                background-color: #1c86ee;
            }}
            #sidebar {{
                position: fixed; top: 0; left: 0;
                width: 250px; height: 100%;
                overflow-y: auto; background: #fff;
                transform: translateX(-100%);
                transition: transform 0.3s ease; z-index:1000;
                padding:20px;
                border-right: 1px solid #ddd;
            }}
            #sidebar.open {{ transform: translateX(0); }}
            #menuToggle {{
                position: fixed; top:20px; left:20px; z-index:1001;
                background:#1e90ff; color:#fff; border:none; padding:8px 12px;
                border-radius:4px; cursor:pointer;
                font-size: 16px;
            }}
            #searchInput {{
                display:block; width:calc(100% - 20px);
                margin:60px auto 20px;
                padding:10px;
                border:1px solid #ccc; border-radius:4px;
                box-sizing: border-box;
            }}
            .container {{
                padding:20px;
                transition: margin-left 0.3s ease;
                margin-left: 0;
            }}
            #sidebar ul {{
                list-style-type: none;
                padding: 0;
            }}
            #sidebar li a {{
                display: block;
                padding: 8px 10px;
                color: #333;
                text-decoration: none;
                border-bottom: none;
                border-radius: 4px;
            }}
            #sidebar li a:hover {{
                background-color: #f0f0f0;
                color: #1e90ff;
            }}
            @media (prefers-color-scheme: dark) {{
                body {{
                    background-color: #2e2e2e;
                    color: #f4f4f4;
                }}
                h1, h2, h3 {{
                    color: #f4f4f4;
                }}
                pre {{
                    background: #3e3e3e;
                    border: 1px solid #555;
                }}
                code {{
                    color: #f4f4f4;
                }}
                #sidebar {{
                    background: #3e3e3e;
                    border-right: 1px solid #555;
                }}
                #sidebar li a {{
                    color: #f4f4f4;
                }}
                #sidebar li a:hover {{
                    background-color: #555;
                    color: #1e90ff;
                }}
                #searchInput {{
                    background-color: #555;
                    color: #f4f4f4;
                    border: 1px solid #777;
                }}
            }}
            @media (min-width: 768px) {{
                #menuToggle {{ display: none; }}
                #searchInput {{ display: none; }}
                #sidebar {{
                    transform: translateX(0);
                    position: sticky;
                    height: calc(100vh - 40px);
                    top: 20px;
                    margin-right: 20px;
                }}
                .container {{
                    margin-left: 270px;
                }}
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
                #menuToggle {{
                    padding: 6px 10px;
                    font-size: 14px;
                }}
                #sidebar {{
                    padding-top: 60px;
                }}
            }}
        </style>
    </head>
    <body>
        <button id="menuToggle">☰ Menu</button>
        <nav id="sidebar">
            <input type="search" id="searchInput" placeholder="Search categories…" />
            <ul>
                {category_links}
            </ul>
        </nav>
        <div class="container">
            <h1>Python 3.12 Standard Library Bible</h1>
            <hr>
            {content_sections}
        </div>
        
        <button id="scrollToTopBtn">Top</button>
    
        <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.3.0/marked.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
        <script>
            document.querySelectorAll('pre code').forEach((block) => {{
                hljs.highlightElement(block);
            }});
            
            var scrollToTopBtn = document.getElementById("scrollToTopBtn");
            window.onscroll = function() {{
                if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {{
                    scrollToTopBtn.style.display = "block";
                }} else {{
                    scrollToTopBtn.style.display = "none";
                }}
            }};
            scrollToTopBtn.onclick = function() {{
                window.scrollTo({{ top: 0, behavior: 'smooth' }});
            }};

            document.querySelectorAll('.copy-btn').forEach((button) => {{
                button.onclick = function() {{
                    var codeBlock = button.parentElement.querySelector('code');
                    var textArea = document.createElement('textarea');
                    textArea.value = codeBlock.innerText;
                    document.body.appendChild(textArea);
                    textArea.select();
                    document.execCommand('copy');
                    document.body.removeChild(textArea);
                    button.innerText = 'Copied!';
                    setTimeout(() => {{
                        button.innerText = 'Copy';
                    }}, 2000);
                }};
            }});

            document.getElementById('menuToggle').onclick = function() {{
                document.getElementById('sidebar').classList.toggle('open');
            }};

            document.getElementById('searchInput').onkeyup = function() {{
                let filter = this.value.toUpperCase();
                let ul = document.querySelector("#sidebar ul");
                let li = ul.getElementsByTagName('li');
                for (let i = 0; i < li.length; i++) {{
                    let a = li[i].getElementsByTagName("a")[0];
                    if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {{
                        li[i].style.display = "";
                    }} else {{
                        li[i].style.display = "none";
                    }}
                }}
            }};
        </script>
    </body>
    </html>
    """.strip()

    category_links = ""
    content_sections = ""

    sorted_categories = sorted(
        markdown_files_by_category.keys(), key=lambda s: s.lower())
    for category in sorted_categories:
        files = markdown_files_by_category[category]
        safe_category = escape(category)
        category_links += f"<li><a href='#{safe_category}'>{safe_category}</a></li>"

    for category in sorted_categories:
        files = markdown_files_by_category[category]
        safe_category = escape(category)
        sorted_files = sorted(files, key=lambda s: s.lower())
        content_sections += f"<h2 id='{safe_category}'>{safe_category}</h2><ul>"
        for file in sorted_files:
            safe_file = escape(file)
            file_path = Path(file)
            content_sections += f"<li><a href='#{safe_file}'>{escape(file_path.name)}</a></li>"
        content_sections += "</ul>"

        for file in sorted_files:
            safe_file = escape(file)
            file_path = Path(file)
            with file_path.open('r') as f:
                content = f.read()
            file_html_content = markdown.markdown(content, extensions=[
                'fenced_code', 'codehilite', CopyButtonExtension()
            ])
            content_sections += f"""
<h3 id='{safe_file}'>{escape(file_path.name)}</h3>
<button onclick="history.back()">Back</button>
{file_html_content}
"""

    return html_content.format(category_links=category_links, content_sections=content_sections)


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


def save_html_file(content, output_file):
    output_dir = Path("html_version")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / output_file
    with open(output_path, 'w') as f:
        f.write(content)


if __name__ == "__main__":
    directory = "standard_library_documents"
    output_file = "index.html"

    markdown_files_by_category = get_markdown_files_by_category(directory)
    html_content = convert_markdown_to_html(markdown_files_by_category)
    save_html_file(html_content, output_file)
    print(f"HTML file generated: html_version/{output_file}")
