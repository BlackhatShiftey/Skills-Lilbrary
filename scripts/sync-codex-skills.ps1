param(
    [string[]]$SkillName
)

$libraryRoot = Split-Path -Parent $PSScriptRoot
$sourceRoot = Join-Path $libraryRoot "codex"
$destRoot = if ($env:CODEX_HOME) {
    Join-Path $env:CODEX_HOME "skills"
} else {
    Join-Path $HOME ".codex\\skills"
}

if (-not (Test-Path -LiteralPath $sourceRoot)) {
    throw "Source skill library not found: $sourceRoot"
}

if (-not (Test-Path -LiteralPath $destRoot)) {
    New-Item -ItemType Directory -Path $destRoot -Force | Out-Null
}

$skills = if ($SkillName -and $SkillName.Count -gt 0) {
    foreach ($name in $SkillName) {
        Join-Path $sourceRoot $name
    }
} else {
    Get-ChildItem -LiteralPath $sourceRoot -Directory | ForEach-Object { $_.FullName }
}

foreach ($skillPath in $skills) {
    if (-not (Test-Path -LiteralPath $skillPath)) {
        Write-Warning "Skipping missing skill: $skillPath"
        continue
    }

    $name = Split-Path -Leaf $skillPath
    $dest = Join-Path $destRoot $name

    if (Test-Path -LiteralPath $dest) {
        Remove-Item -LiteralPath $dest -Recurse -Force
    }

    Copy-Item -LiteralPath $skillPath -Destination $dest -Recurse -Force
    Write-Output "Synced $name -> $dest"
}
