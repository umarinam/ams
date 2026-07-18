#!/usr/bin/env python3
"""Starter AMS runner that initializes structured workflow artifacts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def build_markdown_report(assessment_id: str) -> str:
    return "\n".join(
        [
            f"# Modernization Readiness Report ({assessment_id})",
            "",
            "Modernization readiness: 0/100",
            "",
            "Primary blocker:",
            "No repository analysis has been executed yet.",
            "",
            "Recommended first step:",
            "Run repository discovery, then managed/native/build/test assessments.",
        ]
    ) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run starter AMS workflow")
    parser.add_argument("--repository-path", required=True)
    parser.add_argument("--assessment-id", required=True)
    parser.add_argument("--output-root", default="outputs")
    args = parser.parse_args()

    output_root = Path(args.output_root)
    assessment_id = args.assessment_id

    state = {
        "assessmentId": assessment_id,
        "repositoryPath": args.repository_path,
        "status": "in-progress",
        "detectedProjectTypes": [],
        "buildEntryPoints": [],
        "completedAgents": [],
        "pendingAgents": [
            "repository-discovery",
            "managed-assessment",
            "native-assessment",
            "build-assessment",
            "test-assessment",
            "modernization-planner",
            "validation",
        ],
        "findings": [],
        "conflicts": [],
        "humanApprovals": [],
    }

    inventory = {
        "projects": [],
        "dependencies": [],
        "buildOrder": [],
        "entryPoints": [],
        "testProjects": [],
    }

    dependency_graph = {"nodes": [], "edges": []}

    initial_modernization_plan = {
        "assessmentId": assessment_id,
        "readinessScore": 0,
        "blockers": ["No repository analysis has been executed yet."],
        "risks": [],
        "migrationOrder": [],
        "backlogItems": [],
        "recommendedPoC": "Run discovery and managed/native assessments to collect evidence.",
        "targetArchitecture": "To be determined from repository evidence.",
    }

    state_output_path = output_root / "orchestrator" / f"{assessment_id}-workflow-state.json"
    write_json(state_output_path, state)
    write_json(output_root / "inventory" / f"{assessment_id}-inventory.json", inventory)
    write_json(output_root / "inventory" / f"{assessment_id}-dependency-graph.json", dependency_graph)
    write_json(output_root / "reports" / f"{assessment_id}-modernization-plan.json", initial_modernization_plan)

    markdown_report = output_root / "reports" / f"{assessment_id}-modernization-report.md"
    markdown_report.parent.mkdir(parents=True, exist_ok=True)
    markdown_report.write_text(build_markdown_report(assessment_id), encoding="utf-8")

    print(f"Initialized AMS starter artifacts for '{assessment_id}'")
    print(f"Workflow state: {state_output_path}")
    print(f"Outputs: {output_root.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
