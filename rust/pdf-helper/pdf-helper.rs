
use regex::Regex;

fn main() {
    // Statements here are executed when the compiled binary is called.

    // Print text to the console.
    println!("Hello GG");
    let re = Regex::new(r"^\d{4}-\d{2}-\d{2}$").unwrap();
    assert!(re.is_match("2014-01-01"));
}