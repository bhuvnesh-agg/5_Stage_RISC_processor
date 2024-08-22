`include "mips.v"
module mips_tb;
reg clk1;
reg clk2;
integer file;
integer k, n, i, r;
reg [31:0] data;
mips32 cpu(.clk1(clk1), .clk2(clk2));

  initial begin
    clk1 = 0; clk2 =0;
    repeat (200)
      begin
        #5 clk1 = 1;  #5 clk1 = 0;
        #5 clk2 =1; #5 clk2 =0;
        // $display ("PC - %2d | R7 - %2d | R3 - %2d | R4 - %2d | R5 - %2d | R9 - %2d | MEM[101] - %2d", cpu.PC, cpu.regbank[7], cpu.regbank[3], cpu.regbank[4], cpu.regbank[5], cpu.regbank[9], cpu.mem[101]);
      end
    $display ("Index of Key %2d is: %2d", cpu.regbank[5], cpu.regbank[7]);
    end

  initial begin
    reg [8 * 40:1] filename;
    if ($value$plusargs("%s", filename)) begin
      file = $fopen(filename, "r");
    end
    else begin
      $display("usage: mips32 +<path/to/binary/file>");
      $finish;
    end

    if (file == 0) begin
      $finish;
    end

    i = 0;
    while (!$feof(file) && i < 1024) begin
      r = $fscanf(file, "%b\n", data);
      if (r) begin
        cpu.mem[i] = data;
        cpu.mem[100 + i] = i;
        i = i + 1;
      end
    end

    cpu.HALTED =0;
    cpu.PC=0;
    cpu.TAKEN_BRANCH=0;

    $fclose(file);
  end

  endmodule
