import sys
opcodes = {
    'ADD': 0,
    'SUB': 1,
    'AND': 2,
    'OR': 3,
    'SLT': 4,
    'LW': 8,
    'SW': 9,
    'ADDI': 10,
    'SUBI': 11,
    'SLTI': 12,
    'BNEQZ': 13,
    'BEQZ': 14,
    'HLT': 63
}

def register_to_bin(register):
    # Convert register number (e.g., R1) to a 6-bit binary string
    return format(int(register[1:]), '05b')

def immediate_to_bin(value, is_offset=False):
    if value.startswith('0b'):
        # Binary
        result = format(int(value, 2), '016b')
    elif value.startswith('0x'):
        # Hexadecimal
        result = format(int(value, 16), '016b')
    else:
        # Decimal
        result = format(int(value), '016b')
    
    if is_offset:
        return result
    else:
        return result

def assemble_instruction(instruction, label_positions, current_line):
    parts = instruction.split()
    opcode = parts[0].upper()

    if opcode not in opcodes:
        raise ValueError(f"Unknown opcode: {opcode}")

    binary_opcode = format(opcodes[opcode], '06b')

    if opcode == 'HLT':
        return binary_opcode + '0' * 26

    if opcode in ['ADD', 'SUB', 'AND', 'OR', 'SLT']:
        # R-type: opcode (6) | rs (5) | rt (5) | rd (5) | unused (11)
        rd = register_to_bin(parts[1])
        rs = register_to_bin(parts[2])
        rt = register_to_bin(parts[3])
        return binary_opcode + rs + rt + rd + '0' * 11

    if opcode in ['ADDI', 'SUBI', 'SLTI', 'LW', 'SW']:
        # I-type: opcode (6) | rs (5) | rt (5) | immediate (16)
        rt = register_to_bin(parts[1])
        rs = register_to_bin(parts[2])
        immediate = immediate_to_bin(parts[3])
        return binary_opcode + rs + rt + immediate

    if opcode in ['BNEQZ', 'BEQZ']:
        # Branch: opcode (6) | rs (5) | offset (16)
        rs = register_to_bin(parts[1])
        label = parts[2]
        if label not in label_positions:
            raise ValueError(f"Unknown label: {label}")
        offset = label_positions[label] - (current_line + 1)
        if offset < -32768 or offset > 32767:
            raise ValueError(f"Offset out of range: {offset}")
        offset_bin = format(offset & 0xFFFF, '016b')
        return binary_opcode + rs + '0'*5 + offset_bin 

    raise ValueError(f"Instruction format not supported: {instruction}")

def first_pass(program):
    label_positions = {}
    current_line = 0

    for line in program:
        line = line.strip()
        if line.endswith(':'):
            label = line[:-1]
            label_positions[label] = current_line
        elif line:
            current_line += 1

    return label_positions

def assemble_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        program = infile.readlines()

    label_positions = first_pass(program)
    with open(output_file, 'w') as outfile:
        current_line = 0
        for line in program:
            line = line.strip()
            if not line or line.endswith(':'):
                continue  # Skip labels and empty lines
            machine_code = assemble_instruction(line, label_positions, current_line)
            outfile.write(machine_code + '\n')
            current_line += 1

# Example usage:
input_file = sys.argv[1]
output_file = sys.argv[1].split('.')[0] + '.bin'

assemble_file(input_file, output_file)
