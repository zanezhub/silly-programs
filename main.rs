use std::{io};
use ureq::{get, Error};
use scraper::{Html, Selector};

fn main() -> Result<(), Error>{
    let mut buf = String::new();
    let stdin = io::stdin();
    stdin.read_line(&mut buf).unwrap();

    match buf.as_str() {
        "\r\n" => {
            buf.clear();
            buf.push_str("https://chilangoskate.com/tienda/45-revistas-y-libros");
        },
        _ => {},
    }
    
    let response = 
        get(&buf)
            .call()?
            .into_string()?;

    let frag = Html::parse_document(&response);
    let h2_sel = Selector::parse("h2 > a").unwrap();

    for element in frag.select(&h2_sel) {
        println!("{:#?}" ,element.inner_html());
    }

    Ok(())
}
