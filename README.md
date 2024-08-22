# 5 Stage Pipelined RISC processor with Custom Python Assembler

## Overview

This project implements a 5-stage pipelined Reduced Instruction Set Computer (RISC) processor, inspired by the MIPS32 architecture, using Verilog. While it does not fully implement the entire MIPS32 instruction set, it covers the core concepts and a subset of instructions necessary to demonstrate the principles of pipelining and RISC architecture.
Additionally, there is a custom Python Assembler that assembles code written in assembly into machine code that can be directly executed by this CPU.

## Usage Instructions
#### Assembling Code
Assembly code written in a `.asm` file can be assembled using the following command:
```python3 mips_new.py input.asm output.bin```

#### Compiling the Testbench
The testbench currently stores numbers starting from 0 from memory location 100. This can be changed inside the `mips_tb.v` file.
The testbench can be compiled by running the following command:
```iverilog -g2005-sv mips_tb.v mips32```

#### Executing Code
The generated binary can be used to execute the assembled on the CPU. This can be done by using the following command:
```./mips32 +<path/to/assembled/binary>```

## Features

- **Five Stages of Pipeline:**
  - **Instruction Fetch (IF):** Fetches instructions from memory.
  - **Instruction Decode (ID):** Decodes instructions and reads registers.
  - **Execution (EX):** Performs arithmetic, logic, or memory operations.
  - **Memory Access (MEM):** Handles data memory operations.
  - **Write Back (WB):** Writes results back to the register file.

- **Hazard Handling:**
  - Data forwarding and pipeline stalling to resolve data hazards.
  - Simple stalling to handle control hazards.

- **MIPS32-Based Instruction Set:**
  - Basic arithmetic operations (ADD, SUB, ADDI, SUBI, MUL).
  - Logical operations (AND, OR, SLT, SLTI).
  - Load and store instructions (LW, SW).
  - Branch and jump instructions (BEQZ, BNEQZ).
  - Control Instructions (HLT)

## Architecture

The processor is divided into five distinct stages, each responsible for a part of the instruction execution process. The pipeline architecture ensures that multiple instructions are processed simultaneously, significantly improving performance over a non-pipelined architecture.

### Pipeline Stages

1. **Instruction Fetch (IF):**
   - Fetches the next instruction from the instruction memory.
   - Calculates the address of the next instruction.

2. **Instruction Decode (ID):**
   - Decodes the fetched instruction.
   - Reads the required operands from the register file.
   - Performs sign-extension for immediate values.

3. **Execution (EX):**
   - Executes the operation specified by the instruction.
   - Performs ALU operations or calculates memory addresses for load/store instructions.

4. **Memory Access (MEM):**
   - Accesses data memory for load/store instructions.
   - Handles data forwarding when necessary.

5. **Write Back (WB):**
   - Writes the result of the instruction back to the register file.

### Data Path and Control Signals

- The design includes a complete data path to handle instruction flow through the pipeline.
- Control signals are generated to manage the operation of each stage appropriately.

## Instruction Set

This processor supports a subset of the MIPS32 instruction set, including:

### Arithmetic Instructions
- `ADD` - Add two registers and store the result in a register.
- `ADDI` - Add an immediate value to a register and store the result in another register.
- `SUB` - Subtract one register from another and store the result in a register.
- `SUBI` - Subtract an immediate value from a register and store the result in another register.
- `MUL` - Multiply two registers and store the result in a register.

### Logical Instructions
- `AND` - Perform a bitwise AND on two registers.
- `OR` - Perform a bitwise OR on two registers.
- `SLT` - Perform an Arithmetic Left Shift on a register by an amount given by another register and store the result in some other register.
- `SLTI` - Perform an Arithmetic Left Shift on a register by an immediate amount and store the result in some other register.

### Memory Instructions
- `LW` - Load a word from memory into a register.
- `SW` - Store a word from a register into memory.

### Control Flow Instructions
- `BEQZ` - Branch to a target address if a registers is equal to zero.
- `BNEQZ` - Branch to a target address if a registers is not zero.
- `HLT` - Tells the processor to halt until reset.
