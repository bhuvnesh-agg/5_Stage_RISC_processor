  ADDI  R4  R0  0b0000000000001100  
  ADDI  R5  R0  0b0000000000000110 
  ADD   R7  R0  R0              
  ADD   R3  R0  R0              

  .Loop:
  LW    R3  R7  101
  ADD   R0  R0  R0
  ADD   R0  R0  R0
  SUB   R1  R5  R3
  ADD   R0  R0  R0
  ADD   R0  R0  R0
  BEQZ  R1  .Found
  SUB   R9  R4  R7
  ADD   R0  R0  R0
  ADD   R0  R0  R0
  BEQZ  R9  .Not_Found
  ADDI  R7  R7  0b0000000000000001 
  BNEQZ R1  .Loop

  .Found:
  ADDI  R31 R0  0b0000000000000001
  HLT

  .Not_Found:
  ADDI  R31 R0  0b0000000000000100
  HLT
