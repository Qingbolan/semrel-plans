# 服务器迁移手册

准备日期：2026-10-15。部署保留论文阅读、查询 JSON、数据文件下载、DAG 读取与 EAL 编译。分组和论文编辑仍按浏览器保存，可通过 `/migration.html` 导出并迁移；本次没有改为多人共享数据库。

## 迁移包

在项目根目录执行：

```sh
python3 backend/scripts/localize_inputs.py
npm ci
npm run build
python3 backend/scripts/prepare_release.py --output releases/2026-10-15
```

构建需要本机可用的 EasyNet CLI。`localize_inputs.py` 将 8-17 与 semantic-workload-bench 等来源中仍绑定到外部项目的输入复制到 `data/source-inputs/`，并更新输入绑定；不改动原始查询文本和提供的任务 JSON。重导入数据后应重新执行此步骤。准备脚本输出 `site.tar`、`SHA256SUMS`、逐文件 SHA-256 清单，以及独立的 Docker 构建上下文。数据集和来源快照全部包含，目录不依赖原电脑绝对路径，公开文件权限统一为 0644，避免本机生成的 0600 文件在容器中不可读；`.git`、node_modules、私有部署配置不包含在公开站点中。不要将整个工作仓库直接作为 Web 根目录。每次发布使用新的目录，不覆盖旧版本。

## 旧浏览器数据

1. 在现有网站打开 `http://localhost:8765/migration.html`，点击“导出浏览器数据”。必须使用原有浏览器和原有 origin（域名、协议、端口完全相同）。
2. 保管导出的 JSON；不同浏览器的编辑分别导出。
3. 新网站上线后打开 `https://实际域名/migration.html` 导入。导入会先下载新浏览器现有数据的备份，只覆盖备份中的同名记录。
4. 返回图册刷新，检查分组和论文编辑。服务器文件备份不会自动包含浏览器编辑。

## Linux 部署前置条件

- Linux 服务器、Docker Engine 和 Compose 插件、Nginx，以及已配置的域名和 HTTPS 证书。
- 不需要 EasyNet 编译器：图册中的计划图在构建时已编译为快照（`assets/plans.js`），服务器只提供静态文件与数据目录。没有编译器时，仅页面里“导入 EAL”不可用；健康检查返回 `eal_import: false`。
- 磁盘至少容纳压缩前文件总量、上传包和上一版备份。具体字节数见 `release-manifest.json` 的 `total_bytes`；保留两版建议预留其 3 倍以上空间。

## 传输、启动与验收

将整个迁移包目录复制到服务器，例如 `/srv/semrel/package-2026-10-15`。以下命令在该目录执行：

```sh
sha256sum -c SHA256SUMS
mkdir -p /srv/semrel/releases/2026-10-15
tar -xf site.tar -C /srv/semrel/releases/2026-10-15
python3 backend/scripts/verify_release.py --root /srv/semrel/releases/2026-10-15
cp deploy/.env.example deploy/.env
```

修改 `deploy/.env`：`ATLAS_PUBLIC_ORIGINS` 填写完整 origin，例如 `https://atlas.your-domain.com`（不能有路径或末尾斜杠）；`ATLAS_SITE_DIR` 指向刚解包的目录。多个明确域名用逗号分隔，不支持通配符。子路径部署不在当前配置范围内，使用独立域名根路径。

确保迁移文件可由容器 UID 10001 读取，目录可进入。然后：

```sh
docker compose --env-file deploy/.env -f deploy/compose.yaml build
docker compose --env-file deploy/.env -f deploy/compose.yaml up -d
docker compose --env-file deploy/.env -f deploy/compose.yaml ps
curl --fail http://127.0.0.1:8765/api/health
```

按 `deploy/nginx.conf.example` 配置真实域名、证书路径和本地端口，执行 `nginx -t` 后重载。反向代理保留原始 Host 和 Origin，不应伪造为 localhost。容器端口只绑定服务器 loopback；文件只读挂载，编译临时文件位于有大小限制的 `/tmp`，不执行 EAL mission。

```sh
python3 backend/scripts/verify_release.py --root /srv/semrel/releases/2026-10-15 --url https://实际域名
```

再在浏览器检查：论文页、任一 DAG、Abacus 三个工作流、MMQA 单题 JSON、图片／数据下载、EAL 导入编译、浏览器数据恢复。API 健康检查失败时查看 `docker compose --env-file deploy/.env -f deploy/compose.yaml logs atlas`。

## 回滚与备份

保留上一版站点目录、迁移包和对应运行代码／编译器。升级前导出浏览器编辑；若验收失败，将 `.env` 的 `ATLAS_SITE_DIR` 改回上一版，切回对应迁移包并运行 `docker compose ... up -d --build --force-recreate`。网站内容由只读发布目录提供，不在容器中修改。域名不变时浏览器编辑仍保留；域名改变需重新导入。

## 当前验证边界

本地验证覆盖域名／Origin 检查、文件访问边界、实际 EAL 编译 API、浏览器备份恢复和迁移包内容校验。本机 Docker daemon 未运行，因此未声称完成容器构建、Linux 二进制验收、Nginx TLS 或远程上线；这些由上面的目标机器验收命令完成。
