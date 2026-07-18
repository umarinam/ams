param(
    [Parameter(Mandatory = $true)]
    [string]$RepositoryPath,

    [Parameter(Mandatory = $true)]
    [string]$AssessmentId,

    [string]$OutputRoot = "outputs"
)

python "$PSScriptRoot/run-ams.py" --repository-path "$RepositoryPath" --assessment-id "$AssessmentId" --output-root "$OutputRoot"
