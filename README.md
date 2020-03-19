# sbx_vsearch

[Sunbeam](https://github.com/sunbeam-labs/sunbeam) extension for [Vsearch](https://github.com/torognes/vsearch)

This extension allows you to use the --usearch-global option of vsearch to do alignment of reads to any fasta file.

## Installation

1. git clone https://github.com/sunbeam-labs/sbx_vsearch
2. cp sbx_vsearch $SUNBEAM_DIR/extensions/
3. cat sunbeam/extensions/sbx_vsearch/config.yml >> sunbeam_config.yml (the config.yml that your are using for your given project)

## Running

1. sunbeam --use_conda all_vsearch {rest of parameters}

## References

[Sunbeam](https://github.com/sunbeam-labs/sunbeam)

[Vsearch](https://github.com/torognes/vsearch)

[isolated Conda environment](http://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html#integrated-package-management)
