import os

# Directory to start the search
start_directory = "."

# Strings to find and replace
replacements = {
    "CUDA 12.5.props": "CUDA 12.6.props",
    "CUDA 12.5.targets": "CUDA 12.6.targets",
    "CUDA 12.5.xml": "CUDA 12.6.xml"
}

# Search through the directory structure
for dirpath, dirnames, filenames in os.walk(start_directory):
    for filename in filenames:
        # Check if the file is a .vcxproj file
        if filename.endswith(".vcxproj"):
            file_path = os.path.join(dirpath, filename)
            try:
                # Open the .vcxproj file and read its content
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                # Initialize a flag to track if any replacement was made
                modified = False

                # Loop over each replacement pair and perform replacements
                for old_string, new_string in replacements.items():
                    if old_string in content:
                        content = content.replace(old_string, new_string)
                        modified = True

                # If the file was modified, write the changes back to the file
                if modified:
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(content)
                    print(f"Replaced in: {file_path}")

            except Exception as e:
                print(f"Error processing {file_path}: {e}")
