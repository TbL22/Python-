# 代码历史使用方式

在 VS Code 中打开项目根目录 `C:\Users\李田博\Desktop\python校园程序`，不要只打开 `.vscode`。后续 App 开发统一在此目录进行。

通过“终端 → 运行任务”启动 `History: save locally`。任务运行期间每 5 秒检查一次已经由 Git 跟踪的文件，并为修改或删除创建提交。两次检查之间的连续保存可能合并，因此不保证每一次保存都有独立提交。关闭任务或 VS Code 后停止记录；下次开发时需要重新启动任务。

新文件需要先明确加入版本管理并提交：

```powershell
git add -- src/你的文件名
git commit -m "feat: 添加功能说明"
```

自动任务不纳入未跟踪文件。手动提交、切换版本、合并等操作前先停止自动任务。检测到暂存区有内容或合并、变基进行中时，任务会暂停提交。不要同时运行两个历史任务。

配置 GitHub 远程地址并完成 Git 身份认证后，可运行 `History: save and sync GitHub`。它同时保存本地历史，每分钟尝试推送当前分支及带说明的标签。推送失败会显示警告；本地提交仍保留。它不会自动合并远程变更或强制推送。

```powershell
git remote add origin <你的GitHub仓库地址>
git push -u origin main
```

完成一个阶段、检查功能后，停止自动任务，创建阶段提交和带说明的标签，例如：

```powershell
git add -- src README.md
git commit -m "feat: 完成第一阶段核心功能"
git tag -a v0.1.0 -m "第一阶段：可运行的项目骨架"
git push --follow-tags origin main
```

标签示例需要按实际阶段修改；已经存在的标签不要重复使用。若没有待提交改动，可直接为当前提交打标签。

查看历史：`git log --oneline --decorate`。查看旧文件：`git show 提交编号:文件路径`。恢复单个文件前停止自动任务并检查未提交内容，再执行 `git restore --source 提交编号 -- 文件路径`；恢复会覆盖该文件当前内容，之后可以提交为新的修复记录。

GitHub 仓库：https://github.com/TbL22/Python- 。本地 main 已连接 origin/main。

后台任务启动后每 5 秒保存已跟踪文件的变化，每分钟尝试同步 GitHub。日志在 `.git/history-output.log` 和 `.git/history-error.log`，进程编号记录在 `.git/history-process.id`。后台进程退出或电脑重启后，需要通过上述 VS Code 任务重新启动。不要在后台任务运行时重复启动 VS Code 历史任务。

停止本次后台任务：读取 `.git/history-process.id`，在任务管理器核对对应 PowerShell 进程后结束它。手动提交或恢复文件前先停止任务。

初始化标签 `setup-v0.1.0` 仅标记任务与历史工作流配置，不代表 App 第一阶段已经完成。
