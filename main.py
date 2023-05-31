def prepend_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        if line.startswith(('input', 'output')):
            comment = line.strip().split('//')[1].strip()
            prepend = [
                '//konju-chemmeen ' + comment,
                '//chemmeen-konju',
                '//chemmeen-konju'
            ]
            modified_lines.extend(prepend)
        modified_lines.append(line)

    with open(file_path, 'w') as file:
        file.write('\n'.join(modified_lines))


# Example usage
file_path = 'input.txt'  # Replace with the path to your file
prepend_lines(file_path)
