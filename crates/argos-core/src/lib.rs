//! Regra de negócio do Argos, sem interface.

#[cfg(test)]
mod tests {
    #[test]
    fn crate_compila() {
        assert_eq!(env!("CARGO_PKG_NAME"), "argos-core");
    }
}
