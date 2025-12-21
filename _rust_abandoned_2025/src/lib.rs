pub mod template;

pub fn get_number_length(num: u64) -> u32 {
    num.ilog10() + 1
}

pub fn get_substring_from_number(num: u64, a: u32, b: u32) -> u64 {
    // Indexing out "substrings" of a number, without converting to a string
    // Indexed from the right handside, e.g. get_substring_from_number(123456, 0, 3) -> 456
    let ten_to_a = 10_u64.pow(a);
    let ten_to_b = 10_u64.pow(b);
    (num - ((num / ten_to_b) * ten_to_b)) / ten_to_a
}
