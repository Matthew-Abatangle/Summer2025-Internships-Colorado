#!/usr/bin/env python3
import argparse

def filter_table(lines, keyword):
    """
    Processes the file line-by-line. It assumes that the internship table is a block of lines
    that start with a pipe "|" character. The first two such lines (header and divider) are always kept.
    For subsequent table rows, only rows that contain the keyword (case-insensitive) are preserved.
    All non-table lines are kept unchanged.
    """
    filtered_lines = []
    in_table_block = False
    header_count = 0

    for line in lines:
        stripped = line.strip()
        # Check if this line looks like part of a Markdown table
        if stripped.startswith('|'):
            if not in_table_block:
                # Starting a new table block.
                in_table_block = True
                header_count = 0
            header_count += 1
            # Always keep the first two rows (header and divider)
            if header_count <= 2:
                filtered_lines.append(line)
            else:
                # For data rows, check for the keyword
                if keyword.lower() in line.lower():
                    filtered_lines.append(line)
                # Otherwise, skip this row.
        else:
            # If we hit a non-table line and we were in a table block, finish that block.
            in_table_block = False
            filtered_lines.append(line)
    return filtered_lines

def main():
    parser = argparse.ArgumentParser(
        description='Filter a Markdown table to only include rows with a specific keyword (default "Colorado").'
    )
    parser.add_argument('input_file', help='Path to the input Markdown file (e.g., README.md)')
    parser.add_argument('output_file', help='Path to the output Markdown file')
    parser.add_argument('--keyword', default='Colorado', help='Keyword to filter by (default: "Colorado")')
    args = parser.parse_args()

    with open(args.input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = filter_table(lines, args.keyword)

    with open(args.output_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == '__main__':
    main()
