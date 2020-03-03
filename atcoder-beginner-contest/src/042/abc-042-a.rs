/// # abc 042
/// https://atcoder.jp/contests/abc042
use std::io;

// A
fn main () {
    // Standard input
    let mut input  = String::new();

    io::stdin().read_line(&mut input).unwrap();
    let mut array = input.split_whitespace();

    let a: i32 = array.next().unwrap().parse().unwrap();
    let b: i32 = array.next().unwrap().parse().unwrap();
    let c: i32 = array.next().unwrap().parse().unwrap();

    // start
    let sum = a + b + c;
    if sum != 17 {
        println!("false");
        return;
    }

    let mut t_array = [a, b, c];
    t_array.sort();
    
    let mut count = 0;
    for elem in t_array.iter() {
        if *elem  == 5 {
            count += 1;
        }
    }

    if count == 2 {
        println!("true");
        return;
    }

    println!("false");
}

