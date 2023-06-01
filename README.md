# upskilling_

def get_port_names(verilog_file):

    with open(verilog_file, 'r') as f:

        lines = f.readlines()

    port_names = []

    for line in lines:

        line = line.strip()

        if line.startswith(('input', 'output')):

            port_name = line.split(':')[0].strip()

            port_names.append(port_name)

    return port_names

def get_prepend_text(port_name, prepend_file):

    with open(prepend_file, 'r') as f:

        prepend_lines = f.readlines()

    prepend_text = ''

    start_collecting = False

    for line in prepend_lines:

        line = line.strip()

        if not start_collecting and line.startswith(port_name):

            start_collecting = True

        elif start_collecting:

            if line.startswith(tuple(get_port_names(verilog_file))):

                break

            prepend_text += line

    return prepend_text

def prepend_text_to_file(verilog_file, prepend_file, output_file):

    port_names = get_port_names(verilog_file)

    with open(verilog_file, 'r') as verilog, open(prepend_file, 'r') as prepend, open(output_file, 'w') as output:

        verilog_lines = verilog.readlines()

        for line in verilog_lines:

            line = line.strip()

            if line.startswith(('input', 'output')):

                port_name = line.split(':')[0].strip()

                prepend_text = get_prepend_text(port_name, prepend_file)

                output.write(prepend_text + line + '\n')

# Usage

verilog_file = 'verilog_file.v'

prepend_file = 'prepend_file.txt'

output_file = 'output_file.txt'

prepend_text_to_file(verilog_file, prepend_file, output_file)
