const BIT_MASK: u64 = 0b111;

fn main() {
    let start = std::time::Instant::now();

    // let known_output_1: [u64; 20] = [4,1,7,6,4,1,0,2,7,0,0,0,0,0,0,0,0,0,0,0];
    let known_output_2: [u64; 20] = [2,4,1,1,7,5,1,5,4,0,5,5,0,3,3,0,0,0,0,0];

    let mut program_output: [u64; 20] = [0; 20];

    // run_program(64854237, &mut program_output);
    // println!("{:?}", program_output);
    // assert!(program_output == known_output_1);

    //          10000000000
    for i in 1..10000000000 {
        run_program(i, &mut program_output);

        if i % 100000 == 0 {
            println!("{}", i);
        }

        if program_output == known_output_2 {
            println!("{}", i);
            break;
        }
    }

    println!("Run time: {:?}", start.elapsed());
}

#[inline(always)]
fn run_program(reg_a_initial: u64, out_vec: &mut [u64; 20]) {
    let mut reg_a = reg_a_initial * 8;
    let mut out_pointer = 0;

    while reg_a > 7 {
        reg_a >>= 3;
        let reg_b = ((reg_a & BIT_MASK) ^ 1) ^ 5 ^ (reg_a >> ((reg_a & BIT_MASK) ^ 1));
        out_vec[out_pointer] = reg_b & BIT_MASK;
        if out_pointer == 0 && out_vec[out_pointer] != 2 {
            return;
        }
        out_pointer += 1
    }
}