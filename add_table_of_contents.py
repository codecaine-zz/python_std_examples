#!/usr/bin/env python3
"""
Script to add Table of Contents to all markdown files in the standard_library_documents folder.
"""

import os
import re
from pathlib import Path


def extract_headings_from_md(content):
    """Extract headings from markdown content to generate table of contents."""
    headings = []
    lines = content.split("\n")

    for line in lines:
        # Look for markdown headings (###, ####, etc. but skip # and ##)
        if line.strip().startswith("###"):
            heading_text = line.strip().lstrip("#").strip()
            # Create anchor link (convert to lowercase, replace spaces with hyphens, remove special chars)
            anchor = re.sub(r"[^\w\s-]", "", heading_text.lower()).replace(" ", "-")
            anchor = re.sub(r"-+", "-", anchor).strip("-")
            headings.append((heading_text, anchor))
        elif line.strip().startswith("## ") and not line.strip().startswith(
            "## Table of Contents"
        ):
            # Also include ## level headings (but not our TOC)
            heading_text = line.strip().lstrip("#").strip()
            anchor = re.sub(r"[^\w\s-]", "", heading_text.lower()).replace(" ", "-")
            anchor = re.sub(r"-+", "-", anchor).strip("-")
            headings.append((heading_text, anchor))
        # Look for example patterns
        elif "Example" in line and ("###" in line or line.strip().startswith("```")):
            # Handle code block examples
            if "```" in line:
                continue
            heading_text = line.strip().lstrip("#").strip()
            if heading_text:
                anchor = re.sub(r"[^\w\s-]", "", heading_text.lower()).replace(" ", "-")
                anchor = re.sub(r"-+", "-", anchor).strip("-")
                headings.append((heading_text, anchor))

    return headings


def has_table_of_contents(content):
    """Check if the file already has a Table of Contents."""
    return "## Table of Contents" in content


def add_table_of_contents(file_path):
    """Add table of contents to a markdown file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Skip if already has TOC
        if has_table_of_contents(content):
            print(f"Skipping {file_path} - already has TOC")
            return

        # Extract headings
        headings = extract_headings_from_md(content)

        if not headings:
            print(f"No headings found in {file_path}")
            return

        # Generate TOC
        toc_lines = ["## Table of Contents", ""]
        for i, (heading_text, anchor) in enumerate(
            headings[:10], 1
        ):  # Limit to first 10 headings
            toc_lines.append(f"{i}. [{heading_text}](#{anchor})")

        toc_content = "\n".join(toc_lines) + "\n\n"

        # Find where to insert TOC (after the main title)
        lines = content.split("\n")
        insert_index = 1  # Default to after first line

        for i, line in enumerate(lines):
            if line.strip().startswith("# "):
                insert_index = i + 1
                break

        # Insert TOC
        lines.insert(insert_index, toc_content)
        new_content = "\n".join(lines)

        # Write back to file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"Added TOC to {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")


def main():
    """Main function to process all markdown files."""
    base_dir = Path("/Users/codecaine/python_std_examples/standard_library_documents")

    # Find all .md files
    md_files = list(base_dir.rglob("*.md"))

    print(f"Found {len(md_files)} markdown files")

    for md_file in md_files:
        add_table_of_contents(md_file)

    print("Finished processing all files")


if __name__ == "__main__":
    main()
