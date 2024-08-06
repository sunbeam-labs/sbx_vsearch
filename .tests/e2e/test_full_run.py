import os
import pytest
import shutil
import subprocess as sp
import sys
from pathlib import Path


@pytest.fixture
def setup(tmpdir):
    reads_fp = Path(".tests/data/reads/").resolve()
    db_fp = Path(".tests/data/ref/").resolve()

    project_dir = tmpdir / "project"

    sp.check_output(["sunbeam", "init", "--data_fp", reads_fp, project_dir])

    config_fp = project_dir / "sunbeam_config.yml"

    config_str = f"sbx_vsearch: {{db_fp: {db_fp}}}"
    sp.check_output(
        [
            "sunbeam",
            "config",
            "modify",
            "-i",
            "-s",
            f"{config_str}",
            f"{config_fp}",
        ]
    )

    yield tmpdir, project_dir


@pytest.fixture
def run_sunbeam(setup):
    tmpdir, project_dir = setup

    output_fp = project_dir / "sunbeam_output"

    try:
        # Run the test job
        sp.check_output(
            [
                "sunbeam",
                "run",
                "--conda-frontend",
                "conda",
                "--profile",
                project_dir,
                "all_vsearch",
                "--directory",
                tmpdir,
            ]
        )
    except sp.CalledProcessError as e:
        shutil.copytree(output_fp / "logs", "logs/")
        shutil.copytree(project_dir / "stats", "stats/")
        sys.exit(e)

    shutil.copytree(output_fp / "logs", "logs/")
    shutil.copytree(project_dir / "stats", "stats/")

    benchmarks_fp = project_dir / "stats"

    yield output_fp, benchmarks_fp


def test_full_run(run_sunbeam):
    output_fp, benchmarks_fp = run_sunbeam

    long_report_fp = output_fp / "mapping" / "vsearch" / "LONG_report.tsv"
    long_fasta_fp = output_fp / "mapping" / "vsearch" / "LONG.fasta"

    # Check output
    assert long_report_fp.exists()
    assert long_fasta_fp.exists()
