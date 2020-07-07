{
  imports = [
    ./modules/nfs-home.nix
  ];

  boot.graphenePatches.enable = true;

  networking.hostName = "martha";
  networking.retiolum = {
    ipv4 = "10.243.29.179";
    ipv6 = "42:0:3c46:5466:7dbe:f27a:673f:ea64";
  };

}
