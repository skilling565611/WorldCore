param(
    [string]$PythonPath = ""
)

$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$helperPath = Join-Path $scriptDir "keepass_helper.py"

function Test-TkinterPython {
    param([string]$Candidate)

    if ([string]::IsNullOrWhiteSpace($Candidate)) {
        return $false
    }

    try {
        & $Candidate -c "import tkinter" *> $null
        return ($LASTEXITCODE -eq 0)
    }
    catch {
        return $false
    }
}

function Start-KeepPassHelper {
    param([string]$Candidate)

    Write-Host "Launching WorldCore KeepPass Helper with:"
    Write-Host $Candidate
    & $Candidate $helperPath
}

if (-not (Test-Path -LiteralPath $helperPath)) {
    Write-Error "Could not find helper app: $helperPath"
    exit 1
}

$candidates = New-Object System.Collections.Generic.List[string]

if ($PythonPath) {
    $candidates.Add($PythonPath)
}

$pythonCommands = @("python", "python3", "py")
foreach ($command in $pythonCommands) {
    $resolved = Get-Command $command -ErrorAction SilentlyContinue
    if ($resolved) {
        $candidates.Add($resolved.Source)
    }
}

$commonPythonRoots = @(
    "$env:LOCALAPPDATA\Programs\Python",
    "$env:ProgramFiles\Python312",
    "$env:ProgramFiles\Python311",
    "$env:ProgramFiles\Python310"
)

foreach ($root in $commonPythonRoots) {
    try {
        if (Test-Path -LiteralPath $root -ErrorAction Stop) {
            Get-ChildItem -LiteralPath $root -Recurse -Filter python.exe -ErrorAction SilentlyContinue |
                ForEach-Object { $candidates.Add($_.FullName) }
        }
    }
    catch {
        Write-Verbose "Skipping inaccessible Python search root: $root"
    }
}

$uniqueCandidates = $candidates | Where-Object { $_ } | Select-Object -Unique

foreach ($candidate in $uniqueCandidates) {
    if (Test-TkinterPython $candidate) {
        Start-KeepPassHelper $candidate
        exit $LASTEXITCODE
    }
}

Write-Host ""
Write-Host "No Python with Tkinter/Tcl-Tk support was found."
Write-Host ""
Write-Host "Fix:"
Write-Host "1. Install or repair standard Python from python.org."
Write-Host "2. Enable the Tcl/Tk and IDLE feature during setup."
Write-Host "3. Re-run this launcher:"
Write-Host "   powershell -ExecutionPolicy Bypass -File KeepPass\App\Run_KeepPass_Helper.ps1"
Write-Host ""
Write-Host "Optional if Python is installed somewhere specific:"
Write-Host "   powershell -ExecutionPolicy Bypass -File KeepPass\App\Run_KeepPass_Helper.ps1 -PythonPath C:\Path\To\Python\python.exe"
Write-Host ""
Write-Host "Do not use 'python -m install tkinter'; Tkinter is not installed that way."
exit 1
