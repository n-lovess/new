@R1
D=M
@DIV_INVALID
D;JEQ

@R2
M=0
@R3
M=0

@R0
D=M
@NEG_X
D;JLT

@R1
D=M
@NEG_Y
D;JLT

(DIV_LOOP)
@R0
D=M
@R1
D=D-M
@END_DIV
D;JLT

@R0
M=D
@R2
M=M+1
@DIV_LOOP
0;JMP

(NEG_X)
@R0
D=-M
@R0
M=D
@NEG_Y_CHECK
0;JMP

(NEG_Y)
@R1
D=-M
@R1
M=D

(NEG_Y_CHECK)
@R0
D=M
@R2
D=M
@NEG_QUOTIENT
D;JLT

@END_DIV
0;JMP

(NEG_QUOTIENT)
@R2
M=-M

(END_DIV)
@R0
M=D

@R4
M=0
@END
0;JMP

(DIV_INVALID)
@R4
M=1
@END
0;JMP

(END)