use clap::Parser;

/// Argos: canvas de agentes do Hades, reescrito em Rust.
#[derive(Parser)]
#[command(name = "argos", version, about)]
struct Cli {}

fn main() {
    Cli::parse();
}
