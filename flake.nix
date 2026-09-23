{
  description = "Smith Wiki development environment";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { nixpkgs, ... }:
    let
      systems = [
        "aarch64-darwin"
        "aarch64-linux"
        "x86_64-darwin"
        "x86_64-linux"
      ];
      forAllSystems = nixpkgs.lib.genAttrs systems;
      packagesFor = system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          sw = pkgs.writeShellApplication {
            name = "sw";
            runtimeInputs = with pkgs; [
              curl
              coreutils
              gh
              git
              gnugrep
              jq
              python3
            ];
            text = builtins.readFile ./scripts/sw;
          };
        in
        { inherit pkgs sw; };
    in
    {
      packages = forAllSystems (system:
        let p = packagesFor system;
        in {
          inherit (p) sw;
          default = p.sw;
        });

      devShells = forAllSystems (system:
        let p = packagesFor system;
        in {
          default = p.pkgs.mkShellNoCC {
            packages = [ p.sw ];
          };
        });
    };
}
