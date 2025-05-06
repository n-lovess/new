@R0          // I pick R0 because it holds the number I want to check
D=M          // D register = the value from R0

@NEGATIVE    // If that value is negative, I’ll jump down to the NEGATIVE section
D;JLT        // If D < 0, go to (NEGATIVE)

@R2          // Now I’m at the “not negative” path, so I use R2 as a flag
M=0          // R2 = 0; mark that the input was not negative

@R3          // I also reset an overflow flag in R3
M=0          // R3 = 0; no overflow issue so far

@R0          // Back to R0, I need to copy the original number
D=M          // D = input value

@R1          // R1 is my output register for the absolute value
M=D          // R1 = D; store the same value (it’s already positive)

@END         // That’s it for the positives so I jump to the end
0;JMP        // goto (END)

(NEGATIVE)   // Label: handling the negative case now
@R2          // Mark that it was negative
M=1          // R2 = 1; I spotted a negative input

@R0          // I need to check if it’s the most negative number
D=M          // D = original value

@32768       // Special constant to test for -32768
D=D+A        // D + 32768

@CANNOT_COMPUTE
D;JEQ        // If result equals 0, it was -32768, so overflow

@R0          // For other negatives, I grab the value again
D=M          // D = original value

D=-D         // D = -D; I flip the sign to make it positive

@R1          // Store that positive result in R1
M=D          // R1 = D; absolute value done

@R3          // No overflow here
M=0          // R3 = 0; safe, I could compute

@END         // Finished with negative case too so I jump to the end
0;JMP        // goto (END)

(CANNOT_COMPUTE)
@R3          // It was -32768 which we can’t flip in 16-bit
M=1          // R3 = 1; mark “overflow / can’t compute”

@R0          // I still want to pass the original through
D=M          // D = original input

@R1          // I store it in R1 even though it’s still negative
M=D          // R1 = D; that’s the best we can do

(END)        // Label: all done, the program stops here