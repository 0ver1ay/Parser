import os

def process_file(input_file):
    encodings = ['utf-8', 'cp1251']  # Add more encodings if necessary
    modified_content = []

    for encoding in encodings:
        try:
            # Read the content of the file with the current encoding
            with open(input_file, 'r', encoding=encoding, errors='replace') as file:
                content = file.read()

            # Remove HTML classes
            content = remove_html_classes(content)

            # Add table tags
            content = add_table_tags(content)

            modified_content.append(content)

            print(f"File processed successfully with encoding: {encoding}")
            return modified_content  # Exit the function if the file is processed successfully

        except UnicodeDecodeError:
            continue  # Try the next encoding if a decoding error occurs

    print(f"Unable to determine the correct encoding for the file: {input_file}")
    return modified_content


def remove_html_classes(content):
    import re
    # Remove HTML class attributes
    content = re.sub(r'class\s*=\s*"[^"]*"', '', content)

    # Remove colspan attributes
    # content = re.sub(r'colspan\s*=\s*"\d*"', '', content)

    # Remove height attributes
    content = re.sub(r'height\s*=\s*"[^"]*"', '', content)

    # Remove width attributes
    content = re.sub(r'width\s*=\s*"[^"]*"', '', content)

    # Remove HTML comments
    content = re.sub(r'<!--(.*?)-->', '', content, flags=re.DOTALL)

    # Delete <br> and </br> tags
    content = re.sub(r'<b\s*/?>', '', content)

    # Align text in <td> with colspan=2
    content = re.sub(
        r'<td([^>]*)colspan\s*=\s*"2"([^>]*)>',
        r'<td\1colspan="2"\2 style="text-align: center;">',
        content, flags=re.DOTALL
    )

    # Wrap text in <b> tags for <td> with colspan=2
    content = re.sub(
        r'<td([^>]*)colspan\s*=\s*"2"([^>]*)>(.*?)</td>',
        r'<td\1colspan="2"\2><b>\3</b></td>',
        content, flags=re.DOTALL
    )

    return content

def add_table_tags(content):

    # Add table tags around the content
    content = '<table class="colored_table">\n' + \
              '    <thead>\n' + \
              '        <tr>\n' + \
              '            <th>\n' + \
              '                Параметр\n' + \
              '            </th>\n' + \
              '            <th>\n' + \
              '                Значение\n' + \
              '            </th>\n' + \
              '        </tr>\n' + \
              '    </thead>\n' + \
              '    <tbody>\n' + \
              content + \
              '    </tbody>\n' + \
              '</table>'
    return content


def combine_files(modified_content, output_file):
    combined_content = ""
    for i, content in enumerate(modified_content):
        combined_content += content
        if i < len(modified_content) - 1:
            combined_content += '<br><br><br>\n'

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(combined_content)


def process_files(input_files):
    modified_content = []
    for input_file in input_files:
        content = process_file(input_file)
        modified_content.extend(content)
    return modified_content

# Get the current directory
directory = os.getcwd()

# Find files starting with 'html_input_' and ending with '.txt'
input_files = [filename for filename in os.listdir(directory) if filename.startswith('html_input_') and filename.endswith('.txt')]

output_file = 'result.txt'
modified_content = process_files(input_files)
combine_files(modified_content, output_file)

# Delete input_files
for input_file in input_files:
    file_path = os.path.join(directory, input_file)
    os.remove(file_path)