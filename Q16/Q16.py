def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        
        total_lines = len(lines1)
        if len(lines2) > total_lines:
            total_lines = len(lines2)
        
        return total_lines

file1 = 'file1.txt'
file2 = 'file2.txt'
line_count = compare_files(file1, file2)
print(f"Total number of lines in the files: {line_count}")
