const BIT_MASK: u64 = 0b111;

// const KNOWN_OUTPUT: [u64; 20] = [4,1,7,6,4,1,0,2,7,0,0,0,0,0,0,0,0,0,0,0];
const KNOWN_OUTPUT: [u64; 20] = [2,4,1,1,7,5,1,5,4,0,5,5,0,3,3,0,0,0,0,0];

fn main() {
    let start = std::time::Instant::now();

    let mut program_output: [u64; 20] = [0; 20];

    // assert!(run_program(64854237, &mut program_output));

    //          100000000000
    for i in 100000000000..1000000000000 {
        if i % 10000000 == 0 {
            println!("{}", i);
        }

        if run_program(i, &mut program_output) {
            println!("{}", i);
            break;
        }
    }

    println!("Run time: {:?}", start.elapsed());
}

#[inline(always)]
fn run_program(reg_a_initial: u64, out: &mut [u64; 20]) -> bool {
    let mut reg_a = reg_a_initial * 8;
    let mut out_pointer = 0;

    while reg_a > 7 {
        reg_a >>= 3;
        let reg_b = ((reg_a & BIT_MASK) ^ 1) ^ 5 ^ (reg_a >> ((reg_a & BIT_MASK) ^ 1));
        out[out_pointer] = reg_b & BIT_MASK;
        if out_pointer == 0 && out[out_pointer] != 2 {  // Manual optimisation for the real KNOWN_OUTPUT
            return false;
        }
        out_pointer += 1
    }
    return *out == KNOWN_OUTPUT
}