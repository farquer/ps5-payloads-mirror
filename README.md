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
| <img src="readme-icons/kraken-mount.png" width="36" alt=""> | **kraken-mount** | `v0.3.1` | 从内置 SSD、M.2 和 USB 挂载 PS5 游戏 | 未声明 | `2026-11-20` | [源码](https://github.com/quer3q/kraken-mount/releases) | [下载](https://github.com/farquer/ps5-payloads-mirror/releases/download/payloads-mirror/kraken-mount_v0.3.1.elf) |
| <img src="readme-icons/orbit-store-ps5.png" width="36" alt=""> | **orbit-store-ps5** | `v1.9.5` | 在 PS5 上选择游戏来源和格式，直接下载到主机或外接存储。 | 未声明 | `2026-11-19` | [源码](https://github.com/saawant12/orbit-store-ps5/releases) | [下载](https://github.com/farquer/ps5-payloads-mirror/releases/download/payloads-mirror/orbit-store-ps5_v1.9.5.elf) |
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
| <img src="readme-icons-itsplk/WebKit-Autoloader-Installer.svg" width="36" alt=""> | **WebKit-Autoloader-Installer** | `v0.8.2` | 自动加载 WebKit 漏洞和 ELF payload。 | 5.00–13.60 | `2026-11-20` | [源码](https://github.com/itsPLK/ps5-webkit-autoloader/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/WebKit-Autoloader-Installer_v0.8.2.elf) |
| <img src="readme-icons-itsplk/ps5upload.png" width="36" alt=""> | **ps5upload** | `v12.6.13` | 把游戏、应用和自制程序传到已越狱 PS5，断线后可以续传。 | 1.00–14.10（5.10、9.60、13.60 已测试） | `2026-11-19` | [源码](https://github.com/phantomptr/ps5upload/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps5upload_v12.6.13.elf) |
| <img src="readme-icons-itsplk/elfldr.png" width="36" alt=""> | **elfldr** | `v0.28` | 给已越狱 PS5 用的 ELF 加载器，加载后在后台持续运行。 | 未声明 | `2026-11-19` | [源码](https://github.com/ps5-payload-dev/elfldr/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/elfldr_v0.28.elf) |
| <img src="readme-icons-itsplk/ps5-dump-forge.png" width="36" alt=""> | **ps5-dump-forge** | `v0.5.6` | 在 PS5、Windows、macOS 和 Linux 上转换并编辑游戏转储和多种封装格式。 | 未声明 | `2026-11-16` | [源码](https://github.com/quer3q/ps5-dump-forge/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps5-dump-forge_v0.5.6.elf) |
| <img src="readme-icons-itsplk/NeoEnabler.png" width="36" alt=""> | **NeoEnabler** | `0.7.0` | 让 PS4 游戏在 PS5 上以 PS4 Pro 模式和更高分辨率运行。 | 4.00–13.60（13.20、13.60 已测试） | `2026-11-16` | [源码](https://github.com/gasb07/NeoEnabler/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/NeoEnabler_0.7.0.elf) |
| <img src="readme-icons-itsplk/PS5Save.png" width="36" alt=""> | **PS5Save** | `v3` | 用 USB 自动备份已越狱 PS5 的游戏存档和文件。 | 未声明 | `2026-11-15` | [源码](https://github.com/heni0xyz/PS5Save/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/PS5Save_v3.elf) |
| <img src="readme-icons-itsplk/ps4mount.png" width="36" alt=""> | **ps4mount** | `v0.8.0` | 不安装到主机，直接从 USB 在已越狱 PS5 上运行 PS4 假 PKG。 | 5.50+（6.00 起常规注册，13.20 已测试） | `2026-11-13` | [源码](https://github.com/gasb07/ps4mount/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps4mount_v0.8.0.elf) |
| <img src="readme-icons-itsplk/garlic-savemgr.png" width="36" alt=""> | **garlic-savemgr** | `v1.15-beta23` | 在已越狱 PS5 上解密、加密和浏览存档，自带网页界面。 | 未声明 | `2026-11-11` | [源码](https://git.etawen.dev/earthonion/garlic-savemgr/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/garlic-savemgr_v1.15-beta23.elf) |
| <img src="readme-icons-itsplk/ps5-web-file-manager.png" width="36" alt=""> | **ps5-web-file-manager** | `v1.14` | 带网页界面的 PS5 文件管理器，用来把游戏转储从 USB 拷到内置存储。 | 未声明 | `2026-11-10` | [源码](https://github.com/owendswang/ps5-web-file-manager/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps5-web-file-manager_v1.14.elf) |
| <img src="readme-icons-itsplk/LiveShell.png" width="36" alt=""> | **LiveShell** | `v1.7.0` | 给 PS5 主界面使用可下载的动画壁纸。 | 未声明 | `2026-11-10` | [源码](https://github.com/ZiZc3/LiveShell/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/LiveShell_v1.7.0.elf) |
| <img src="readme-icons-itsplk/ftpsrv.jpg" width="36" alt=""> | **ftpsrv** | `v0.22` | 在已越狱 PS4 或 PS5 上运行的 FTP 服务器，端口 2121。 | 未声明 | `2026-11-08` | [源码](https://github.com/ps5-payload-dev/ftpsrv/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ftpsrv_v0.22.elf) |
| <img src="readme-icons-itsplk/ShadowMountPlus.png" width="36" alt=""> | **ShadowMountPlus** | `1.7beta12` | 在已越狱 PS5 后台自动挂载镜像。 | 全部已越狱固件（需 kstuff-lite v1.07+） | `2026-11-08` | [源码](https://github.com/drakmor/ShadowMountPlus/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ShadowMountPlus_1.7beta12.elf) |
| <img src="readme-icons-itsplk/CheatRunner.jpg" width="36" alt=""> | **CheatRunner** | `v0.18.1` | 在已越狱 PS5 上通过网页使用的金手指训练器。 | 未声明 | `2026-11-03` | [源码](https://github.com/notmaj0r/CheatRunner/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/CheatRunner_v0.18.1.elf) |
| <img src="readme-icons-itsplk/zftpd.png" width="36" alt=""> | **zftpd** | `v1.7.0` | 零拷贝 FTP 服务，同时提供主机 payload。 | 未声明 | `2026-10-28` | [源码](https://github.com/seregonwar/zftpd/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/zftpd_v1.7.0.elf) |
| <img src="readme-icons-itsplk/WelcomeHubActivator.jpg" width="36" alt=""> | **WelcomeHubActivator** | `v1.2.0` | 在 PS5 上启用 Welcome Hub。 | 10.00–13.60 | `2026-10-23` | [源码](https://github.com/ghost1372/WelcomeHubActivator/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/WelcomeHubActivator_v1.2.0.elf) |
| <img src="readme-icons-itsplk/pldmgr.png" width="36" alt=""> | **pldmgr** | `v0.6.3` | 用网页管理、导入并自动加载 PS5 payload。 | 未声明 | `2026-10-19` | [源码](https://github.com/itsPLK/pldmgr/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/pldmgr_v0.6.3.elf) |
| <img src="readme-icons-itsplk/ps5-exporter.jpg" width="36" alt=""> | **ps5-exporter** | `v0.3.1` | 给已越狱 PS5 用的 Prometheus 导出器。 | 13.60 已验证 | `2026-10-19` | [源码](https://github.com/Marice/ps5-exporter/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps5-exporter_v0.3.1.elf) |
| <img src="readme-icons-itsplk/onionHEN.png" width="36" alt=""> | **onionHEN** | `v0.9.0` | 面向 PS5 的一体化 HEN 和工具箱。 | 未声明 | `2026-10-15` | [源码](https://github.com/aydencharles/onionHEN/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/onionHEN_v0.9.0.elf) |
| <img src="readme-icons-itsplk/ps-patch-system.jpg" width="36" alt=""> | **ps-patch-system** | `38108724867` | 应用补丁系统。 | 未声明 | `2026-10-11` | [源码](https://github.com/illusionyy/ps-patch-system/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps-patch-system_38108724867.elf) |
| <img src="readme-icons-itsplk/PKG-Manager.png" width="36" alt=""> | **PKG-Manager** | `v1.5.1` | 在 PS5 上浏览并安装 USB、光盘或 SMB 共享中的 PKG。 | 未声明 | `2026-10-10` | [源码](https://github.com/itsPLK/ps5-pkg-manager/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/PKG-Manager_v1.5.1.elf) |
| <img src="readme-icons-itsplk/ps5-app-dumper.png" width="36" alt=""> | **ps5-app-dumper** | `v2.10` | 把 PS5 应用文件从 pfsmnt 导出到已连接的 USB 存储。 | 1.00–13.60 | `2026-10-03` | [源码](https://github.com/EchoStretch/ps5-app-dumper/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps5-app-dumper_v2.10.elf) |
| <img src="readme-icons-itsplk/ps5debug-NG.jpg" width="36" alt=""> | **ps5debug-NG** | `1.3.2` | 运行在已越狱 PS5 用户态里的调试 payload。 | 3.00–13.60（列出的点版本已完全验证） | `2026-09-23` | [源码](https://github.com/Pharaoh2k/ps5debug-NG/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps5debug-NG_1.3.2.elf) |
| <img src="readme-icons-itsplk/kstuff-lite.png" width="36" alt=""> | **kstuff-lite** | `v1.11` | kstuff 的精简版。 | 未声明 | `2026-09-20` | [源码](https://github.com/EchoStretch/kstuff-lite/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/kstuff-lite_v1.11.elf) |
| <img src="readme-icons-itsplk/ftpsrv-drakmor.png" width="36" alt=""> | **ftpsrv-drakmor** | `1.16-ng-stable` | drakmor 维护的 ftpsrv，在已越狱 PS4 或 PS5 上提供 FTP。 | 未声明 | `2026-09-20` | [源码](https://github.com/drakmor/ftpsrv/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ftpsrv-drakmor_1.16-ng-stable.elf) |
| <img src="readme-icons-itsplk/ps5-linux-loader.jpg" width="36" alt=""> | **ps5-linux-loader** | `v2.5` | 利用 HV 漏洞，在 PS5 Phat、Slim 和 Pro 上启动 Linux。 | Phat/Slim 3.00–7.61、11.00–13.60；Pro 11.00–13.60 | `2026-09-05` | [源码](https://github.com/ps5-linux/ps5-linux-loader/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps5-linux-loader_v2.5.elf) |
| <img src="readme-icons-itsplk/ps5-date-time-sync.png" width="36" alt=""> | **ps5-date-time-sync** | `v1.0.0` | 用公共 NTP 服务器恢复 PS5 的系统日期和时间。 | 未声明 | `2026-08-24` | [源码](https://github.com/kerrdec97/ps5-date-time-sync/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ps5-date-time-sync_v1.0.0.elf) |
| <img src="readme-icons-itsplk/BFpilot.jpg" width="36" alt=""> | **BFpilot** | `v0.4.4` | 在 PS5 上通过浏览器使用的轻量文件管理器。 | 11.60 已测试 | `2026-08-11` | [源码](https://github.com/ItsBlurf/BFpilot/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/BFpilot_v0.4.4.elf) |
| <img src="readme-icons-itsplk/nanoDNS.png" width="36" alt=""> | **nanoDNS** | `0.4` | 在 PS4 或 PS5 上运行的本地 DNS 代理。 | 未声明 | `2026-08-04` | [源码](https://github.com/drakmor/nanoDNS/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/nanoDNS_0.4.elf) |
| <img src="readme-icons-itsplk/websrv.png" width="36" alt=""> | **websrv** | `v0.34` | 在已越狱 PS5 上运行的简易网页服务器，端口 8080。 | 未声明 | `2026-08-02` | [源码](https://github.com/ps5-payload-dev/websrv/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/websrv_v0.34.elf) |
| <img src="readme-icons-itsplk/shsrv.png" width="36" alt=""> | **shsrv** | `v0.20` | 在已越狱 PS5 上提供类 telnet 的简易 shell，端口 2323。 | 未声明 | `2026-08-02` | [源码](https://github.com/ps5-payload-dev/shsrv/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/shsrv_v0.20.elf) |
| <img src="readme-icons-itsplk/klogsrv.png" width="36" alt=""> | **klogsrv** | `v0.9` | 把已越狱主机的 /dev/klog 转发到端口 3232。 | 未声明 | `2026-08-02` | [源码](https://github.com/ps5-payload-dev/klogsrv/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/klogsrv_v0.9.elf) |
|  | **Lapy-JB-Daemon** | `v1.2` | 模仿 etaHEN 按需越狱接口的独立守护进程。 | 未声明 | `2026-06-01` | [源码](https://github.com/itsPLK/PS5-Lapy-JB-Daemon/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/Lapy-JB-Daemon_v1.2.elf) |
| <img src="readme-icons-itsplk/BackPork.jpg" width="36" alt=""> | **BackPork** | `0.1` | 游戏启动时自动挂载系统库，用来旁加载。 | 未声明 | `2026-04-30` | [源码](https://github.com/BestPig/BackPork/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/BackPork_0.1.elf) |
| <img src="readme-icons-itsplk/etaHEN.jpg" width="36" alt=""> | **etaHEN** | `2.5B` | 一体化的 PS5 Homebrew Enabler。 | 未声明 | `2025-12-25` | [源码](https://github.com/etaHEN/etaHEN/releases) | [下载](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/etaHEN_2.5B.bin) |
<!-- ITSPLK_END -->
