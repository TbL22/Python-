param(
    [string]$Repo = (Split-Path $PSScriptRoot -Parent),
    [switch]$Once,
    [switch]$Push,
    [ValidateRange(1, 3600)][int]$IntervalSeconds = 5
)
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $Repo
git rev-parse --show-toplevel | Out-Null
if ($LASTEXITCODE -ne 0) { throw 'Not a Git repository.' }
$env:GIT_TERMINAL_PROMPT = '0'
$lastPush = [datetime]::MinValue
do {
    $branch = git symbolic-ref --quiet --short HEAD
    $busy = $false
    foreach ($marker in @('MERGE_HEAD', 'CHERRY_PICK_HEAD', 'REVERT_HEAD', 'rebase-merge', 'rebase-apply', 'index.lock')) {
        $path = git rev-parse --git-path $marker
        if (Test-Path -LiteralPath $path) { $busy = $true }
    }
    git diff --cached --quiet
    $staged = $LASTEXITCODE
    if (-not $branch -or $busy -or $staged -ne 0) {
        Write-Warning 'Paused: detached HEAD, Git operation, or manually staged changes. Finish that operation first.'
    } else {
        git diff --quiet
        $changed = $LASTEXITCODE
        if ($changed -eq 1) {
            git add --update
            if ($LASTEXITCODE -ne 0) { throw 'Could not stage tracked changes.' }
            git commit -m "autosave: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
            if ($LASTEXITCODE -ne 0) { throw 'Snapshot failed. Changes remain on disk; inspect git status.' }
        } elseif ($changed -ne 0) { throw 'Could not inspect changes.' }
        if ($Push -and ((Get-Date) - $lastPush).TotalSeconds -ge 60) {
            $lastPush = Get-Date
            git push --follow-tags origin $branch
            if ($LASTEXITCODE -ne 0) {
                Write-Warning 'Push failed. Local history is retained; retry in 60 seconds. Check remote, authentication and remote changes.'
            }
        }
    }
    if (-not $Once) { Start-Sleep -Seconds $IntervalSeconds }
} while (-not $Once)
