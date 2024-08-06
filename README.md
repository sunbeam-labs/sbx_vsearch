<img src="https://github.com/sunbeam-labs/sunbeam/blob/stable/docs/images/sunbeam_logo.gif" width=120, height=120 align="left" />

# sbx_vsearch

<!-- badges: start -->
[![Tests](https://github.com/sunbeam-labs/sbx_vsearch/actions/workflows/pr.yml/badge.svg)](https://github.com/sunbeam-labs/sbx_vsearch/actions/workflows/pr.yml)
[![Release](https://img.shields.io/github/release/sunbeam-labs/sbx_vsearch.svg?style=flat)](https://github.com/sunbeam-labs/sbx_vsearch/releases/latest)
[![DockerHub](https://img.shields.io/docker/pulls/sunbeamlabs/sbx_vsearch)](https://hub.docker.com/repository/docker/sunbeamlabs/sbx_vsearch/)
<!-- badges: end -->

A [Sunbeam](https://github.com/sunbeam-labs/sunbeam) extension for using [Vsearch](https://github.com/torognes/vsearch) with the `--usearch-global` option to do alignment of reads to any fasta file. 

## Installation

To install, activate your conda environment (using the name of your environment) and use `sunbeam extend`:

    conda activate <i>sunbeamX.X.X</i>
    sunbeam extend https://github.com/sunbeam-labs/sbx_vsearch.git

## Usage

To run `vsearch`:

    sunbeam init --data_fp /path/to/reads/ /path/to/project/
    sunbeam config modify -i -f /path/to/project/sunbeam_config.yml -s 'sbx_vsearch: {{db: {/path/to/db}}}'
    sunbeam run --profile /path/to/project/ all_vsearch

N.B. For sunbeam versions <4 the last command will be something like `sunbeam run --configfile /path/to/project/sunbeam_config.yml all_classify`.

## Configuration

  - db_fp: Is the filepath to a directory containing reference fasta files
  - threads: Is the number of threads to use while running vsearch
  - min_id: Is the minimum identity for query-target match
  - weak_id: Is the set lower than min-id and you will get some weaker matches too
  - userfields: Are the fields for results file, see vsearch - documentation for details
  - iddef: Is the way "identity" is calculated, see vsearch docs for details (it's equal to (matching columns) / (alignment length) excluding terminal gaps)
  - fasta_width: Is the width of alignment lines in fasta output, set to 0 to eliminate wrapping
  - maxaccepts: Is the maximum number of hits to accept before stopping the search Default is 1

## Legacy Installation

For sunbeam versions <3 or if `sunbeam extend` isn't working, you can use `git` directly to install an extension:

    git clone https://github.com/sunbeam-labs/sbx_vsearch.git extensions/sbx_vsearch

and then include it in the config for any given project with:

    cat extensions/sbx_vsearch/config.yml >> /path/to/project/sunbeam_config.yml
