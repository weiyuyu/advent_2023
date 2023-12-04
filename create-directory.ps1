$directoryName = $args[0]
if (Test-Path $directoryName) {
    Write-Output("$directoryName already exists")
} else {
    New-Item -ItemType Directory -Path $directoryName
    New-Item -ItemType Directory -Path "$directoryName/part1"
    New-Item -Path "$directoryName/part1/solution.py"
    New-Item -ItemType Directory -Path "$directoryName/part1/files"
    New-Item -Path "$directoryName/part1/files/input.txt"
    New-Item -ItemType Directory -Path "$directoryName/part2"
    New-Item -Path "$directoryName/part2/solution.py"
    New-Item -ItemType Directory -Path "$directoryName/part2/files"
    New-Item -Path "$directoryName/part2/files/input.txt"
    Write-Output("Created directory for $directoryName")
}