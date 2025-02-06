@R0
D=M    

@NEGATIVE
D;JLT  

@R2
M=0    
@R3
M=0    
@R0
D=M    
@R1
M=D    
@END
0;JMP 

(NEGATIVE)
@R2
M=1  

@R0
D=M    
@32768
D=D+A  
@CANNOT_COMPUTE
D;JEQ  

@R0
D=M    
D=-D  
@R1
M=D  
@R3
M=0    
@END
0;JMP  

(CANNOT_COMPUTE)
@R3
M=1   
@R0
D=M    
@R1
M=D   

(END)