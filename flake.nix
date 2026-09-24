{
  description = "Smith Wiki development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

    pyproject-nix = {
      url = "github:pyproject-nix/pyproject.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    uv2nix = {
      url = "github:pyproject-nix/uv2nix";
      inputs.pyproject-nix.follows = "pyproject-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    pyproject-build-systems = {
      url = "github:pyproject-nix/build-system-pkgs";
      inputs.pyproject-nix.follows = "pyproject-nix";
      inputs.uv2nix.follows = "uv2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    {
      nixpkgs,
      pyproject-nix,
      uv2nix,
      pyproject-build-systems,
      ...
    }:
    let
      # nixpkgs 26.11 dropped x86_64-darwin.
      systems = [
        "aarch64-darwin"
        "aarch64-linux"
        "x86_64-linux"
      ];
      forAllSystems = nixpkgs.lib.genAttrs systems;
      workspace = uv2nix.lib.workspace.loadWorkspace { workspaceRoot = ./.; };
      overlay = workspace.mkPyprojectOverlay {
        sourcePreference = "wheel";
      };
      packagesFor = system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          pythonSet = (pkgs.callPackage pyproject-nix.build.packages {
            python = pkgs.python3;
          }).overrideScope
            (nixpkgs.lib.composeManyExtensions [
              pyproject-build-systems.overlays.wheel
              overlay
            ]);
          pythonEnv = pythonSet.mkVirtualEnv "smith-wiki-env" workspace.deps.default;
          sw = pkgs.writeShellApplication {
            name = "sw";
            runtimeInputs = (with pkgs; [
              awscli2
              coreutils
              gh
              git
              gnugrep
              jq
              secretspec
            ]) ++ [ pythonEnv ];
            text = builtins.readFile ./scripts/sw;
          };
        in
        { inherit pkgs pythonEnv sw; };
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
            packages = [
              p.sw
              p.pythonEnv
              p.pkgs.secretspec
              p.pkgs.uv
            ];
          };
        });
    };
}
