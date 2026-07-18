# AMS Orchestrator

The orchestrator controls execution order, shared workflow state, retries, and validation loops.

## Responsibilities

- Initialize workflow state
- Route work based on repository evidence
- Trigger specialized agents conditionally
- Detect duplicate build failures and avoid repeated attempts
- Request additional evidence for conflicting findings
- Require traceable evidence for recommendations
- Re-run planning when validation fails
- Flag high-impact decisions for human approval

## Required Inputs

- `repositoryPath`
- `assessmentId`

## Required Outputs

- `outputs/reports/<assessmentId>-modernization-report.json`
- `outputs/reports/<assessmentId>-modernization-report.md`
- Updated workflow state

## Routing Expression Language

`routing-rules.yaml` uses a minimal function-based expression syntax:

- `contains(array, value)`
- `length(array)`
