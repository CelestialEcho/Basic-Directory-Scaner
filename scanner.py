import os

def scan_directory(directory, extensions):
    suspicious_files = []  # Initialize an empty list to store suspicious files
    for root, dirs, files in os.walk(directory):  # Iterate over the directory tree using os.walk
        for file in files:  # Iterate over files in the current directory
            if file.endswith(extensions):  # Check if the file has one of the specified extensions
                suspicious_files.append(os.path.join(root, file))  # Add the full path of suspicious files to the list
    return suspicious_files  # Return the list of suspicious files

if __name__ == "__main__":
    directory_to_scan = input("Enter the directory path to scan: ")
    extensions_to_scan = input("Enter the file extensions to scan (comma-separated with spaces): ").split(", ")
    suspicious_files = scan_directory(directory_to_scan, tuple(extensions_to_scan))
    if suspicious_files:
        print("The following suspicious files were found:")
        for file in suspicious_files:
            print(file)
    else:
        print("No suspicious files were found.")
