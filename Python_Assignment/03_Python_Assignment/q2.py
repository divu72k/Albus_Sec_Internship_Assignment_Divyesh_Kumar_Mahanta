def extract_pattern_from_file(file_path, pattern):
    matches=[]
    total_count=0
    
    with open(file_path,'r') as file:
        for line in file:
            line_count=line.count(pattern)
            total_count+=line_count
            if line_count>0:
                matches.extend([line[i:i+line_count] for i in range(len(line)) if line.startswith(pattern)])
    
    return matches,total_count

file_path=input("enter the path of the file:")
pattern=input("enter the string pattern to be searched:")
matches,total_count=extract_pattern_from_file(file_path, pattern)
print("Total Occurrences:",total_count)
print("Matches:")
for match in matches:
    print(match)