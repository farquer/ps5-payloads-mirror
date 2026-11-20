# PS5 Payloads 镜像源

自动镜像常用的  PlayStation 5 payload，每日定时更新，plmgr 能一键安装和识别更新一键更新。

Fork 自 https://github.com/itsPLK/ps5-payloads-mirror. 

---

## 使用方式

可以在 payload manager 中将本仓库以多源方式添加.

### 本仓库扩展源

能直连 github 用 ：https://raw.githubusercontent.com/farquer/ps5-payloads-mirror/main/payloads_v2.json

需要 gh-proxy 加速用：https://gh-proxy.farquer.eu.org/https://raw.githubusercontent.com/farquer/ps5-payloads-mirror/main/payloads_ghproxy.json

### itsPLK 官方源国内加速

https://gh-proxy.farquer.eu.org/https://raw.githubusercontent.com/farquer/ps5-payloads-mirror/main/payloads_itsplk_ghproxy.json

（自建 ph-proxy，速度不快可以尝试换  https://cdn.jsdelivr.net/gh 代理）

---

## 注意

> [!CAUTION]
> **仅搬运和汇总，未经验证，需要阅读 payload 项目 readme, 风险自行承担。**
>
> **需要联网，但 y2jb 用户务必使用 nanodns 屏蔽 youtube，防止自动更新**

---

## 扩展源 Payload

<!-- PAYLOADS_START -->
| 图标 | 名称 | 版本 | 说明 | 支持固件 | 最近更新 | 源码 | 下载 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <img src="readme-icons/orbit-store-ps5.png" width="36" alt=""> | **orbit-store-ps5** | `v1.9.5` | 在 PS5 上选择游戏来源和格式，直接下载到主机或外接存储。 | 未声明 | `2026-11-19` | [源码](https://github.com/saawant12/orbit-store-ps5/releases) | [下载](https://github.com/farquer/ps5-payloads-mirror/releases/download/payloads-mirror/orbit-store-ps5_v1.9.5.elf) |
| <img src="readme-icons/kraken-mount.png" width="36" alt=""> | **kraken-mount** | `v0.3.0` | 从内置 SSD、M.2 和 USB 挂载 PS5 游戏 | 未声明 | `2026-11-18` | [源码](https://github.com/quer3q/kraken-mount/releases) | [下载](https://github.com/farquer/ps5-payloads-mirror/releases/download/payloads-mirror/kraken-mount_v0.3.0.elf) |
| <img src="readme-icons/PS5-Cleanup.jpg" width="36" alt=""> | **PS5-Cleanup** | `v1.2` | 清理已越狱 PS5 上的残留数据，无需重装系统或恢复出厂。 | 10.60–13.60（已测试，含 Slim 和 Pro） | `2026-11-18` | [源码](https://github.com/xXBneutzerNameXx/PS5-Cleanup/releases) | [下载](https://github.com/farquer/ps5-payloads-mirror/releases/download/payloads-mirror/PS5-Cleanup_v1.2.elf) |
| <img src="readme-icons/TITAN-CORE.jpg" width="36" alt=""> | **TITAN-CORE** | `v1.0.0` | 带原生 FPKG 引擎、外置硬盘安装和实时诊断的 PS5 游戏工作区。 | 未声明 | `2026-11-16` | [源码](https://github.com/devchmod/TITAN-CORE/releases) | [下载](https://github.com/farquer/ps5-payloads-mirror/releases/download/payloads-mirror/TITAN-CORE_v1.0.0.elf) |
| <img src="readme-icons/PrefBar.jpg" width="36" alt=""> | **PrefBar** | `v0.3.0` | 独立的游戏内性能叠加显示 | 7.XX–13.XX（7.XX 以下未验证） | `2026-11-13` | [源码](https://github.com/X1NONs/PrefBar/releases) | [下载](https://github.com/farquer/ps5-payloads-mirror/releases/download/payloads-mirror/PrefBar_v0.3.0.elf) |
| <img src="readme-icons/ZhiThemes.png" width="36" alt=""> | **ZhiThemes** | `v0.1.0-alpha` | 为真正的 PS5 主界面提供自定义主题 | 9.00–13.60 | `2026-11-12` | [源码](https://github.com/itsRealZhi/ZhiThemes/releases) | [下载](https://github.com/farquer/ps5-payloads-mirror/releases/download/payloads-mirror/ZhiThemes_v0.1.0-alpha.elf) |
| <img src="readme-icons/any-pad.png" width="36" alt=""> | **any-pad** | `v0.9.1-beta` | 通过主机自带蓝牙，把其他平台手柄当作虚拟 DualSense 在已越狱 PS5 上使用。 | 10.01 已测试 | `2026-10-12` | [源码](https://github.com/elmonomalvad0/any-pad/releases) | [下载](https://github.com/farquer/ps5-payloads-mirror/releases/download/payloads-mirror/any-pad_v0.9.1-beta.elf) |
| <img src="readme-icons/OmniPad-PS5.jpg" width="36" alt=""> | **OmniPad-PS5** | `v1.0.4-hotfix1` | 让第三方 USB 手柄以虚拟 DualSense 的方式在已越狱 PS5 上使用 | 7.00–13.60 | `2026-10-05` | [源码](https://github.com/diegobarbosaa/OmniPad-PS5/releases) | [下载](https://github.com/farquer/ps5-payloads-mirror/releases/download/payloads-mirror/OmniPad-PS5_v1.0.4-hotfix1.elf) |
<!-- PAYLOADS_END -->

---

## itsPLK 国内加速

基于 https://github.com/itsPLK/ps5-payloads-mirror/blob/main/payloads_v2.json

<!-- ITSPLK_START -->
| 图标 | 名称 | 版本 | 说明 | 支持固件 | 最近更新 | 源码 | 下载 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <img src="readme-icons-itsplk/ps5upload.png" width="36" alt=""> | **ps5upload** | `v12.6.8` | Fast, reliable transfers from your computer to your PS5 (requires PC app) | 未声明 | `2026-11-18` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/phantomptr/ps5upload/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps5upload_v12.6.8.elf) |
| <img src="readme-icons-itsplk/ps5-dump-forge.png" width="36" alt=""> | **ps5-dump-forge** | `v0.5.6` | A toolkit for working with PS5 game dumps | 未声明 | `2026-11-16` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/quer3q/ps5-dump-forge/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps5-dump-forge_v0.5.6.elf) |
| <img src="readme-icons-itsplk/NeoEnabler.png" width="36" alt=""> | **NeoEnabler** | `0.7.0` | Allows PS4 games with no PS4 Support to receive patches via illusionyy's ps-patch-system that can unlock higher resolutions | 未声明 | `2026-11-16` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/gasb07/NeoEnabler/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/NeoEnabler_0.7.0.elf) |
| <img src="readme-icons-itsplk/PS5Save.png" width="36" alt=""> | **PS5Save** | `v3` | USB save backup utility for jailbroken PS5’s | 未声明 | `2026-11-15` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/heni0xyz/PS5Save/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/PS5Save_v3.elf) |
| <img src="readme-icons-itsplk/ps4mount.png" width="36" alt=""> | **ps4mount** | `v0.8.0` | Play PS4 fake PKGs on a jailbroken PS5 straight from a USB drive, without installing them. | 未声明 | `2026-11-13` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/gasb07/ps4mount/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps4mount_v0.8.0.elf) |
| <img src="readme-icons-itsplk/garlic-savemgr.png" width="36" alt=""> | **garlic-savemgr** | `v1.15-beta23` | PS5 save decrypt/encrypt/browse with embedded web UI. | 未声明 | `2026-11-11` | [源码](https://git.etawen.dev/earthonion/garlic-savemgr/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/garlic-savemgr_v1.15-beta23.elf) |
| <img src="readme-icons-itsplk/ps5-web-file-manager.png" width="36" alt=""> | **ps5-web-file-manager** | `v1.14` | A file manager for PS5 with a web UI | 未声明 | `2026-11-10` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/owendswang/ps5-web-file-manager/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps5-web-file-manager_v1.14.elf) |
| <img src="readme-icons-itsplk/LiveShell.png" width="36" alt=""> | **LiveShell** | `v1.7.0` | Animated backgrounds for PS5 home screen. | 未声明 | `2026-11-10` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/ZiZc3/LiveShell/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/LiveShell_v1.7.0.elf) |
| <img src="readme-icons-itsplk/WebKit-Autoloader-Installer.svg" width="36" alt=""> | **WebKit-Autoloader-Installer** | `v0.7.1` | Installs WebKit Autoloader on homescreen (FW 7.00-13.60) | 未声明 | `2026-11-08` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-webkit-autoloader/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/WebKit-Autoloader-Installer_v0.7.1.elf) |
| <img src="readme-icons-itsplk/ftpsrv.jpg" width="36" alt=""> | **ftpsrv** | `v0.22` | A simple FTP server that accepts connections on port 2121 | 未声明 | `2026-11-08` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/ps5-payload-dev/ftpsrv/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ftpsrv_v0.22.elf) |
| <img src="readme-icons-itsplk/ShadowMountPlus.png" width="36" alt=""> | **ShadowMountPlus** | `1.7beta12` | A fully automated, background 'Auto-Mounter' payload for Jailbroken PlayStation 5 consoles. | 未声明 | `2026-11-08` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/drakmor/ShadowMountPlus/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ShadowMountPlus_1.7beta12.elf) |
| <img src="readme-icons-itsplk/CheatRunner.jpg" width="36" alt=""> | **CheatRunner** | `v0.18.1` | Web-based game cheat trainer | 未声明 | `2026-11-03` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/notmaj0r/CheatRunner/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/CheatRunner_v0.18.1.elf) |
| <img src="readme-icons-itsplk/zftpd.png" width="36" alt=""> | **zftpd** | `v1.7.0` | Zero-copy FTP/HTTP Server | 未声明 | `2026-10-28` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/seregonwar/zftpd/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/zftpd_v1.7.0.elf) |
| <img src="readme-icons-itsplk/WelcomeHubActivator.jpg" width="36" alt=""> | **WelcomeHubActivator** | `v1.2.0` | A PS5 ELF payload that enables the Welcome Hub. | 未声明 | `2026-10-23` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/ghost1372/WelcomeHubActivator/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/WelcomeHubActivator_v1.2.0.elf) |
| <img src="readme-icons-itsplk/elfldr.png" width="36" alt=""> | **elfldr** | `v0.27` | An ELF loader for jailbroken PS5s that accepts payloads on port 9021 | 未声明 | `2026-10-21` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/ps5-payload-dev/elfldr/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/elfldr_v0.27.elf) |
| <img src="readme-icons-itsplk/pldmgr.png" width="36" alt=""> | **pldmgr** | `v0.6.3` | A modern, web-based dashboard to easily manage, import, and automatically load payloads on your PS5. | 未声明 | `2026-10-19` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/pldmgr/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/pldmgr_v0.6.3.elf) |
| <img src="readme-icons-itsplk/ps5-exporter.jpg" width="36" alt=""> | **ps5-exporter** | `v0.3.1` | Prometheus exporter for a jailbroken PS5 | 未声明 | `2026-10-19` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/Marice/ps5-exporter/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps5-exporter_v0.3.1.elf) |
| <img src="readme-icons-itsplk/onionHEN.png" width="36" alt=""> | **onionHEN** | `v0.9.0` | A homebrew enabler and Toolbox for jailbroken PS5 consoles, built on etaHEN | 未声明 | `2026-10-15` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/aydencharles/onionHEN/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/onionHEN_v0.9.0.elf) |
| <img src="readme-icons-itsplk/ps-patch-system.jpg" width="36" alt=""> | **ps-patch-system** | `38108724867` | App patching system | 未声明 | `2026-10-11` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/illusionyy/ps-patch-system/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps-patch-system_38108724867.elf) |
| <img src="readme-icons-itsplk/PKG-Manager.png" width="36" alt=""> | **PKG-Manager** | `v1.5.1` | Browse and install PKGs from USB, disc, or SMB shares directly on your PS5 | 未声明 | `2026-10-10` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-pkg-manager/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/PKG-Manager_v1.5.1.elf) |
| <img src="readme-icons-itsplk/ps5-app-dumper.png" width="36" alt=""> | **ps5-app-dumper** | `v2.10` | A small utility to dump PS5 application files from the console's pfsmnt to a connected USB storage device. | 未声明 | `2026-10-03` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/EchoStretch/ps5-app-dumper/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps5-app-dumper_v2.10.elf) |
| <img src="readme-icons-itsplk/ps5debug-NG.jpg" width="36" alt=""> | **ps5debug-NG** | `1.3.2` | PS5 debugger payload - userland TCP wire-protocol server hosted inside SceShellCore. | 未声明 | `2026-09-23` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/Pharaoh2k/ps5debug-NG/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps5debug-NG_1.3.2.elf) |
| <img src="readme-icons-itsplk/kstuff-lite.png" width="36" alt=""> | **kstuff-lite** | `v1.11` | Lite version of kstuff | 未声明 | `2026-09-20` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/EchoStretch/kstuff-lite/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/kstuff-lite_v1.11.elf) |
| <img src="readme-icons-itsplk/ftpsrv-drakmor.png" width="36" alt=""> | **ftpsrv-drakmor** | `1.16-ng-stable` | drakmor's fork of ftpsrv | 未声明 | `2026-09-20` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/drakmor/ftpsrv/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ftpsrv-drakmor_1.16-ng-stable.elf) |
| <img src="readme-icons-itsplk/ps5-linux-loader.jpg" width="36" alt=""> | **ps5-linux-loader** | `v2.5` | Linux payload implementing HV exploits to run a custom bootloader | 未声明 | `2026-09-05` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/ps5-linux/ps5-linux-loader/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps5-linux-loader_v2.5.elf) |
| <img src="readme-icons-itsplk/ps5-date-time-sync.png" width="36" alt=""> | **ps5-date-time-sync** | `v1.0.0` | Automatically restores the system date and time using public NTP servers | 未声明 | `2026-08-24` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/kerrdec97/ps5-date-time-sync/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps5-date-time-sync_v1.0.0.elf) |
| <img src="readme-icons-itsplk/BFpilot.jpg" width="36" alt=""> | **BFpilot** | `v0.4.4` | Lightweight PS5 file manager, browser based | 未声明 | `2026-08-11` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/ItsBlurf/BFpilot/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/BFpilot_v0.4.4.elf) |
| <img src="readme-icons-itsplk/nanoDNS.png" width="36" alt=""> | **nanoDNS** | `0.4` | Local DNS proxy server | 未声明 | `2026-08-04` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/drakmor/nanoDNS/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/nanoDNS_0.4.elf) |
| <img src="readme-icons-itsplk/websrv.png" width="36" alt=""> | **websrv** | `v0.34` | A simple web server that accepts connections on port 8080 | 未声明 | `2026-08-02` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/ps5-payload-dev/websrv/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/websrv_v0.34.elf) |
| <img src="readme-icons-itsplk/shsrv.png" width="36" alt=""> | **shsrv** | `v0.20` | A simple telnet-like shell server for jailbroken PS5s that accepts connections on port 2323 | 未声明 | `2026-08-02` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/ps5-payload-dev/shsrv/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/shsrv_v0.20.elf) |
| <img src="readme-icons-itsplk/klogsrv.png" width="36" alt=""> | **klogsrv** | `v0.9` | A simple socket server that redirects /dev/klog to sockets connected on port 3232 | 未声明 | `2026-08-02` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/ps5-payload-dev/klogsrv/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/klogsrv_v0.9.elf) |
|  | **Lapy-JB-Daemon** | `v1.2` | Standalone homebrew jailbreak daemon for PS5. Mimics etaHEN's jailbreak-on-demand API. | 未声明 | `2026-06-01` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/PS5-Lapy-JB-Daemon/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/Lapy-JB-Daemon_v1.2.elf) |
| <img src="readme-icons-itsplk/BackPork.jpg" width="36" alt=""> | **BackPork** | `0.1` | Lets you sideload system libraries into PS5 games | 未声明 | `2026-04-30` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/BestPig/BackPork/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/BackPork_0.1.elf) |
| <img src="readme-icons-itsplk/etaHEN.jpg" width="36" alt=""> | **etaHEN** | `2.5B` | AIO HEN payload | 未声明 | `2025-12-25` | [源码](https://gh-proxy.farquer.eu.org/https://github.com/etaHEN/etaHEN/releases) | [下载](https://gh-proxy.farquer.eu.org/https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/etaHEN_2.5B.bin) |
<!-- ITSPLK_END -->
