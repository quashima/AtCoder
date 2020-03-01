// Standard input
fn read () {
    let mut input  = String::new();

    io::stdin().read_line(&mut input)
        .expect("Failed to read line");

    let array: Vec<&str> = input.split(',').collect();
    println!("values: {:?}", array);
}
