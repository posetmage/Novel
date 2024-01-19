import os

def update_layout_in_md_files(directory):
    """
    Recursively update the layout from 'layout: default' to 'layout: page' in all .md files.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)

                try:
                    # Read the content of the file with UTF-8 encoding
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Replace 'layout: default' with 'layout: page'
                    updated_content = content.replace('layout: default', 'layout: page')

                    # Write the updated content back to the file with UTF-8 encoding
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                except UnicodeDecodeError:
                    try:
                        # If UTF-8 fails, try with 'latin-1' encoding
                        with open(filepath, 'r', encoding='latin-1') as f:
                            content = f.read()

                        updated_content = content.replace('layout: default', 'layout: page')

                        with open(filepath, 'w', encoding='latin-1') as f:
                            f.write(updated_content)
                    except Exception as e:
                        # If another error occurs, print the error message
                        print(f"Error processing {file}: {e}")

# Path to the root directory
root_directory = "./"
update_layout_in_md_files(root_directory)

"Recursive update process is complete."