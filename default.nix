{ pkgs ? import <nixpkgs-unstable> {} }:

pkgs.mkShell {
  packages = with pkgs; [ python3 typst ];
}
