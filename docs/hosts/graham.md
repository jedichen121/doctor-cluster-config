# graham

```
System:    Host: graham Kernel: 5.10.150 x86_64 bits: 64 compiler: gcc v: 11.3.0 
           parameters: initrd=\efi\nixos\86x00b1lcpwry8f1b5hzf2wh45wl1g5a-initrd-linux-5.10.150-initrd.efi 
           init=/nix/store/3afymvh0xb068a4inhqhavlzg1izbigi-nixos-system-graham-22.05.20221028.7269939/init 
           console=ttyS0,115200n8 console=tty0 panic=1 boot.panic_on_fail loglevel=4 
           Console: N/A DM: LightDM 1.30.0 Distro: NixOS 22.05 (Quokka) 
Machine:   Type: Server System: Dell product: PowerEdge R7515 v: N/A serial: BP0PSH3 Chassis: 
           type: 23 serial: BP0PSH3 
           Mobo: Dell model: 07PXPY v: A04 serial: .BP0PSH3.CNCMS0016O00V8. UEFI: Dell v: 2.5.5 
           date: 10/07/2021 
Memory:    RAM: total: 503.25 GiB used: 13.39 GiB (2.7%) 
           Array-1: capacity: 2 TiB slots: 16 EC: Multi-bit ECC max-module-size: 128 GiB 
           note: est. 
           Device-1: A1 size: 64 GiB speed: 3200 MT/s type: DDR4 
           detail: synchronous registered (buffered) bus-width: 64 bits total: 72 bits 
           manufacturer: 80AD80B380AD part-no: HMAA8GR7CJR4N-XN serial: 94D31F06 
           Device-2: A2 size: 64 GiB speed: 3200 MT/s type: DDR4 
           detail: synchronous registered (buffered) bus-width: 64 bits total: 72 bits 
           manufacturer: 80AD80B380AD part-no: HMAA8GR7CJR4N-XN serial: 94D31EC7 
           Device-3: A3 size: 64 GiB speed: 3200 MT/s type: DDR4 
           detail: synchronous registered (buffered) bus-width: 64 bits total: 72 bits 
           manufacturer: 80AD869D80AD part-no: HMAA8GR7AJR4N-XN serial: 2414B54A 
           Device-4: A4 size: 64 GiB speed: 3200 MT/s type: DDR4 
           detail: synchronous registered (buffered) bus-width: 64 bits total: 72 bits 
           manufacturer: 80AD869D80AD part-no: HMAA8GR7AJR4N-XN serial: 2414B4D9 
           Device-5: A5 size: 64 GiB speed: 3200 MT/s type: DDR4 
           detail: synchronous registered (buffered) bus-width: 64 bits total: 72 bits 
           manufacturer: 80AD80B380AD part-no: HMAA8GR7CJR4N-XN serial: 94D31EED 
           Device-6: A6 size: 64 GiB speed: 3200 MT/s type: DDR4 
           detail: synchronous registered (buffered) bus-width: 64 bits total: 72 bits 
           manufacturer: 80AD80B380AD part-no: HMAA8GR7CJR4N-XN serial: 94D31E77 
           Device-7: A7 size: 64 GiB speed: 3200 MT/s type: DDR4 
           detail: synchronous registered (buffered) bus-width: 64 bits total: 72 bits 
           manufacturer: 80AD869D80AD part-no: HMAA8GR7AJR4N-XN serial: 2414B4DB 
           Device-8: A8 size: 64 GiB speed: 3200 MT/s type: DDR4 
           detail: synchronous registered (buffered) bus-width: 64 bits total: 72 bits 
           manufacturer: 80AD863280AD part-no: HMAA8GR7AJR4N-XN serial: 23A24A1E 
           Device-9: A9 size: No Module Installed 
           Device-10: A10 size: No Module Installed 
           Device-11: A11 size: No Module Installed 
           Device-12: A12 size: No Module Installed 
           Device-13: A13 size: No Module Installed 
           Device-14: A14 size: No Module Installed 
           Device-15: A15 size: No Module Installed 
           Device-16: A16 size: No Module Installed 
PCI Slots: Slot: N/A type: x16 <OUT OF SPEC> PCIe Slot 3 status: In Use length: Long 
           Slot: 2 type: x16 PCI Express 3 PCIe Slot 2 status: In Use length: Long 
           Slot: 5 type: x16 PCI Express 3 PCIe Slot 5 status: In Use length: Long 
           Slot: N/A type: x16 <OUT OF SPEC> PCIe Slot 4 status: In Use length: Long 
           Slot: 1 type: x8 PCI Express 3 Mezzanine 1 status: In Use length: Long 
CPU:       Info: 64-Core model: AMD EPYC 7713P socket: SP3 bits: 64 type: MT MCP arch: Zen 3 
           family: 19 (25) model-id: 1 stepping: 1 microcode: A001173 cache: L2: 32 MiB 
           flags: avx avx2 lm nx pae sse sse2 sse3 sse4_1 sse4_2 sse4a ssse3 svm bogomips: 511077 
           Speed: 3094 MHz min/max: 1500/3721 MHz base/boost: 2000/3900 boost: enabled 
           volts: 1.8 V ext-clock: 2000 MHz Core speeds (MHz): 1: 3094 2: 3094 3: 3094 4: 3094 
           5: 3093 6: 3093 7: 3094 8: 3094 9: 3093 10: 3094 11: 3094 12: 3094 13: 3094 14: 3094 
           15: 3094 16: 3094 17: 3094 18: 3094 19: 3094 20: 3093 21: 3094 22: 3094 23: 3094 
           24: 3094 25: 3094 26: 3094 27: 3094 28: 3094 29: 3093 30: 3094 31: 3094 32: 3093 
           33: 3094 34: 3094 35: 3094 36: 3094 37: 3094 38: 3094 39: 3094 40: 3093 41: 3094 
           42: 3094 43: 3094 44: 3094 45: 3094 46: 3094 47: 3094 48: 3094 49: 3094 50: 3094 
           51: 3094 52: 3094 53: 3094 54: 3094 55: 3094 56: 3094 57: 3094 58: 3094 59: 3094 
           60: 3093 61: 3094 62: 3094 63: 3094 64: 3094 65: 3094 66: 3094 67: 3094 68: 3094 
           69: 3094 70: 3094 71: 3094 72: 3094 73: 3094 74: 3094 75: 3094 76: 3094 77: 3094 
           78: 3094 79: 3094 80: 3094 81: 3094 82: 3094 83: 3094 84: 3094 85: 3094 86: 3086 
           87: 3141 88: 3094 89: 3094 90: 3094 91: 3094 92: 3094 93: 3094 94: 3094 95: 3094 
           96: 3094 97: 3094 98: 3094 99: 3094 100: 3093 101: 3093 102: 3094 103: 3094 104: 3094 
           105: 3094 106: 3094 107: 3094 108: 3094 109: 3094 110: 3094 111: 3094 112: 3094 
           113: 3094 114: 3094 115: 3094 116: 3094 117: 3094 118: 3094 119: 3078 120: 3094 
           121: 3094 122: 3094 123: 3087 124: 3082 125: 3094 126: 3094 127: 3094 128: 3094 
           Vulnerabilities: Type: itlb_multihit status: Not affected 
           Type: l1tf status: Not affected 
           Type: mds status: Not affected 
           Type: meltdown status: Not affected 
           Type: mmio_stale_data status: Not affected 
           Type: retbleed status: Not affected 
           Type: spec_store_bypass 
           mitigation: Speculative Store Bypass disabled via prctl and seccomp 
           Type: spectre_v1 mitigation: usercopy/swapgs barriers and __user pointer sanitization 
           Type: spectre_v2 mitigation: Retpolines, IBPB: conditional, IBRS_FW, STIBP: always-on, 
           RSB filling, PBRSB-eIBRS: Not affected 
           Type: srbds status: Not affected 
           Type: tsx_async_abort status: Not affected 
Graphics:  Device-1: Matrox Systems Integrated Matrox G200eW3 Graphics driver: mgag200 v: kernel 
           bus-ID: c3:00.0 chip-ID: 102b:0536 class-ID: 0300 
           Display: server: X.org 1.20.14 driver: loaded: mgag200 note: n/a (using device driver) 
           tty: N/A 
           Message: Advanced graphics data unavailable in console for root. 
Audio:     Message: No device data found. 
Network:   Device-1: Broadcom BCM57416 NetXtreme-E Dual-Media 10G RDMA Ethernet vendor: Dell 
           driver: bnxt_en v: kernel port: 1000 bus-ID: 02:00.0 chip-ID: 14e4:16d8 class-ID: 0200 
           IF: enp2s0f0np0 state: up speed: 10000 Mbps duplex: full mac: 2c:ea:7f:af:57:18 
           IP v4: 131.159.102.9/24 type: dynamic scope: global 
           IP v6: 2a09:80c0:102::9/128 type: dynamic noprefixroute scope: global 
           IP v6: fe80::2eea:7fff:feaf:5718/64 scope: link 
           Device-2: Broadcom BCM57416 NetXtreme-E Dual-Media 10G RDMA Ethernet vendor: Dell 
           driver: bnxt_en v: kernel port: 1000 bus-ID: 02:00.1 chip-ID: 14e4:16d8 class-ID: 0200 
           IF: enp2s0f1np1 state: down mac: 2c:ea:7f:af:57:19 
           Device-3: Intel Ethernet E810-C for QSFP driver: ice v: kernel port: 1000 
           bus-ID: 81:00.0 chip-ID: 8086:1592 class-ID: 0200 
           IF: enp129s0f0 state: up speed: 100000 Mbps duplex: full mac: b4:96:91:a4:1c:f0 
           IP v4: 169.254.243.153/16 scope: link 
           IP v6: fe80::b696:91ff:fea4:1cf0/64 scope: link 
           Device-4: Intel Ethernet E810-C for QSFP driver: ice v: kernel port: 1000 
           bus-ID: 81:00.1 chip-ID: 8086:1592 class-ID: 0200 
           IF: enp129s0f1 state: up speed: 100000 Mbps duplex: full mac: b4:96:91:a4:1c:f1 
           IP v4: 169.254.29.105/16 scope: link 
           IP v6: fe80::b696:91ff:fea4:1cf1/64 scope: link 
           Device-5: Broadcom NetXtreme BCM5720 Gigabit Ethernet PCIe 
           vendor: Dell PowerEdge R6515/R7515 LOM driver: tg3 v: kernel port: 1000 bus-ID: c1:00.0 
           chip-ID: 14e4:165f class-ID: 0200 
           IF: eno8303 state: down mac: d0:8e:79:ba:02:20 
           Device-6: Broadcom NetXtreme BCM5720 Gigabit Ethernet PCIe 
           vendor: Dell PowerEdge R6515/R7515 LOM driver: tg3 v: kernel port: 1000 bus-ID: c1:00.1 
           chip-ID: 14e4:165f class-ID: 0200 
           IF: eno8403 state: down mac: d0:8e:79:ba:02:21 
           Device-7: Broadcom BCM57416 NetXtreme-E Dual-Media 10G RDMA Ethernet driver: bnxt_en 
           v: kernel port: 1000 bus-ID: c4:00.0 chip-ID: 14e4:16d8 class-ID: 0200 
           IF: enp196s0f0np0 state: up speed: 10000 Mbps duplex: full mac: e4:3d:1a:71:d6:b0 
           IP v4: 169.254.198.164/16 scope: link 
           IP v6: fe80::e63d:1aff:fe71:d6b0/64 scope: link 
           Device-8: Broadcom BCM57416 NetXtreme-E Dual-Media 10G RDMA Ethernet driver: bnxt_en 
           v: kernel port: 1000 bus-ID: c4:00.1 chip-ID: 14e4:16d8 class-ID: 0200 
           IF: enp196s0f1np1 state: up speed: 10000 Mbps duplex: full mac: e4:3d:1a:71:d6:b1 
           IP v4: 169.254.246.133/16 scope: link 
           IP v6: fe80::e63d:1aff:fe71:d6b1/64 scope: link 
           IF-ID-1: br-3050ab4aecf2 state: down mac: 02:42:5d:56:ba:36 
           IP v4: 172.20.0.1/16 scope: global broadcast: 172.20.255.255 
           IF-ID-2: br-4b6eeb1e3fb5 state: down mac: 02:42:7c:3e:6a:1d 
           IP v4: 172.18.0.1/16 scope: global broadcast: 172.18.255.255 
           IF-ID-3: br-73bd5d65cf4a state: down mac: 02:42:c9:ea:ed:34 
           IP v4: 172.21.0.1/16 scope: global broadcast: 172.21.255.255 
           IF-ID-4: br-cf2cd8ea9ee9 state: down mac: 02:42:79:c5:e1:02 
           IP v4: 172.19.0.1/16 scope: global broadcast: 172.19.255.255 
           IF-ID-5: br-db48a1acaae7 state: down mac: 02:42:cc:96:6c:01 
           IP v4: 172.22.0.1/16 scope: global broadcast: 172.22.255.255 
           IF-ID-6: docker0 state: down mac: 02:42:ef:ca:b8:f2 
           IP v4: 172.17.0.1/16 scope: global broadcast: 172.17.255.255 
           IF-ID-7: tinc.retiolum state: unknown speed: 10 Mbps duplex: full mac: N/A 
           IP v6: 42:0:3c46:ab64:fa7c:171a:c94a:ac19/16 scope: global 
           WAN IP: 131.159.102.9 
RAID:      Hardware-1: Broadcom / LSI MegaRAID SAS-3 3008 [Fury] driver: megaraid_sas 
           v: 07.714.04.00-rc1 port: 1000 bus-ID: 01:00.0 chip-ID: 1000.005f rev: 02 
           class-ID: 0104 
           Device-1: zroot type: zfs status: ONLINE level: linear size: 1.45 TiB free: 528 GiB 
           allocated: 960 GiB 
           Components: Online: N/A 
Drives:    Local Storage: total: raw: 3.46 TiB usable: 4.91 TiB used: 1.25 TiB (25.5%) 
           ID-1: /dev/nvme0n1 maj-min: 259:3 vendor: Dell model: Ent NVMe AGN MU AIC 1.6TB 
           size: 1.46 TiB block-size: physical: 512 B logical: 512 B rotation: SSD 
           serial: S61ANA0R501400 rev: 2.0.2 temp: 13 Celsius C scheme: GPT 
           SMART: yes health: PASSED on: 1y 17d 17h cycles: 18 read-units: 103,222,124 [52.8 TB] 
           written-units: 128,529,504 [65.8 TB] 
           ID-2: /dev/nvme1n1 maj-min: 259:2 vendor: Dell model: Ent NVMe AGN MU AIC 1.6TB 
           size: 1.46 TiB block-size: physical: 512 B logical: 512 B rotation: SSD 
           serial: S61ANA0R501120 rev: 2.0.2 temp: 13 Celsius C 
           SMART: yes health: PASSED on: 1y 17d 17h cycles: 19 read-units: 484 [247 MB] 
           ID-3: /dev/sda maj-min: 8:0 model: AL15SEB060NY size: 558.91 GiB block-size: 
           physical: 512 B logical: 512 B speed: <unknown> rotation: 10000 rpm serial: N/A 
           rev: EF06 temp: 17 C scheme: MBR 
           SMART: yes state: enabled 
Partition: ID-1: / raw-size: N/A size: 1.19 TiB used: 738.09 GiB (60.6%) fs: zfs 
           logical: zroot/root/nixos 
           ID-2: /boot raw-size: 500 MiB size: 499.7 MiB (99.95%) used: 88 MiB (17.6%) fs: vfat 
           block-size: 512 B dev: /dev/nvme0n1p1 maj-min: 259:4 
           ID-3: /home raw-size: N/A size: 896.17 GiB used: 368.79 GiB (41.2%) fs: nfs4 
           remote: nfs:/export/home 
           ID-4: /tmp raw-size: N/A size: 482.22 GiB used: 1.92 GiB (0.4%) fs: zfs 
           logical: zroot/root/tmp 
Swap:      Alert: No swap data was found. 
Sensors:   Message: No ipmi sensor data found. 
           System Temperatures: lm-sensors cpu: 50.2 C mobo: 38.0 C 
           Fan Speeds (RPM): lm-sensors N/A 
Info:      Processes: 1402 Uptime: N/A wakeups: 0 Init: systemd v: 250 target: graphical.target 
           tool: systemctl Compilers: gcc: 11.3.0 Packages: nix-default: 0 nix-sys: 830 lib: 192 
           nix-usr: 0 Client: Sudo v: 1.9.10 inxi: 3.3.04 
```
![hardware topology](graham.lstopo.svg)
