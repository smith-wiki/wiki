{ pkgs, ... }:

let
  sw = pkgs.writeShellApplication {
    name = "sw";
    runtimeInputs = with pkgs; [
      awscli2
      coreutils
      gh
      git
      gnugrep
      jq
      python3
      secretspec
    ];
    text = builtins.readFile ./scripts/sw;
  };
in
{
  packages = [ sw pkgs.secretspec ];
}
