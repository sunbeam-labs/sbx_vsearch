# sbx-centrifuge

[Sunbeam] extension for running [centrifuge]

## Installation

    git clone https://github.com/sunbeam-labs/sbx_centrifuge
    cat sunbeam/extensions/sbx_centrifuge/config.yml >> sunbeam_config.yml

## Running

This extension uses an [isolated Conda environment] for the centrifuge
installation, so you need to include the `--use-conda` argument when running
Sunbeam:

    sunbeam run --configfile=sunbeam_config.yml --use-conda 

The default MetaPhlAn2 database will be downloaded and stored inside the
original Sunbeam Conda environment in `$CONDA_PREFIX/opt/centrifuge_databases`.

[Sunbeam]: https://github.com/sunbeam-labs/sunbeam
[Centrifuge]: https://github.com/infphilo/centrifuge
[isolated Conda environment]: http://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html#integrated-package-management
