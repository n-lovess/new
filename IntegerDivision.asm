@R1
D=M
@DIV_INVALID
D;JEQ
@R1
D=M
@R8
M=D
@R0
D=M
@R7
M=D
@R7
D=M
@X_NEG
D;JLT
@R5
M=0
@X_ABS_DONE
0;JMP
(X_NEG)
@R5
M=1
@R7
M=-M
(X_ABS_DONE)
@R8
D=M
@Y_NEG
D;JLT
@R6
M=0
@Y_ABS_DONE
0;JMP
(Y_NEG)
@R6
M=1
@R8
M=-M
(Y_ABS_DONE)
@R2
M=0
(DIV_LOOP)
@R7
D=M
@R8
D=D-M
@END_LOOP
D;JLT
@R7
M=D
@R2
M=M+1
@DIV_LOOP
0;JMP
(END_LOOP)
@R7
D=M
@R3
M=D
@R5
D=M
@R6
D=M-D
@QUOTIENT_SIGN_DONE
D;JEQ
@R2
M=-M
(QUOTIENT_SIGN_DONE)
@R5
D=M
@REMAINDER_SIGN_DONE
D;JEQ
@R3
M=-M
(REMAINDER_SIGN_DONE)
@R4
M=0
@END
0;JMP
(DIV_INVALID)
@R2
M=0
@R3
M=0
@R4
M=1
@END
0;JMP
(END)