FROM condaforge/mambaforge:latest

# Setup
WORKDIR /home/sbx_vsearch_env

COPY envs/sbx_vsearch_env.yml ./

# Install environment
RUN mamba env create --file sbx_vsearch_env.yml --name sbx_vsearch_env

ENV PATH="/opt/conda/envs/sbx_vsearch_env/bin/:${PATH}"

# "Activate" the environment
SHELL ["conda", "run", "-n", "sbx_vsearch_env", "/bin/bash", "-c"]

# Run
CMD "bash"