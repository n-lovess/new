// This script loads and runs the functions in Sys.vm.
// The output file Sys.out will contain the values stored in SP
// and RAM[256] at the end of the execution of your Sys.vm.
// With the initial data supplied below, the output file should
// contain:
//
// | RAM[0] |RAM[256]|
// |    257 |     11 |
//
// If you change the initial value of SP on line 18 below, to get
// meaningful results in your Sys.out you should update lines 16,
// 23, and 24 accordingly.

load Sys.vm,
output-file Sys.out,
output-list RAM[0]%D1.6.1 RAM[256]%D1.6.1;

set sp 258,
set local 100,
set argument 200,
set this 1000,
set that 2000,
set RAM[256] 2050,
set RAM[257] 4,
set RAM[2050] -2,
set RAM[2051] 1,
set RAM[2052] 0,
set RAM[2053] 9,
repeat 65000 {
    vmstep;
}
output;