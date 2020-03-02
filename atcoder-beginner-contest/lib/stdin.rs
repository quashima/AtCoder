// Standard input
fn read () {
    // Standard input
    let mut input  = String::new();

    io::stdin().read_line(&mut input).unwrap();
    let mut array = input.split_whitespace();

    println!("{}", array.next().unwrap());
}
