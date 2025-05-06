@R0         // I pick R0 because it holds the first input bit pattern
D=M         // D = value from R0

@R1         // Now I grab R1, which has the second input bit pattern
D=D|M       // D = (R0 OR R1); combine bits with OR

@R2         // I’ll use R2 to store the final XOR result
M=D         // R2 = D; save that OR part first

@R0         // Back to R0 to recompute part of the XOR formula
D=M         // D = R0 again

@R1         // And re‑select R1 for the AND test
D=D&M       // D = (R0 AND R1); bits that are 1 in both

D=!D        // D = NOT D; invert so these bits become 0, rest 1

@R2         // Finally, combine with the OR result in R2
M=M&D       // R2 = R2 AND D; giving (R0 OR R1) AND NOT(R0 AND R1)