# FastAPI Server for Huggingface Inference Endpoints

A custom fastapi server packaged as docker image for Huggingface inference endpoints deployment.
This repository serves as a minimal working example to deploy a custom language model on Huggingface Inference Endpoints using Docker and FastAPI.
The server exposes a **/health** endpoint for health checks and a **/predict** endpoint for next token predictions.

To easily and quickly try the server, you can e.g. use the following small language model:
[cerebras/Cerebras-GPT-111M](https://huggingface.co/cerebras/Cerebras-GPT-111M)

The loader assumes that model and tokenizer files are available in the **/repository** directory which is mounted by HF endpoints (https://huggingface.co/docs/inference-endpoints/en/guides/custom_container).
HF will make the files of the repository that you select under **Model Repository** during deployment available at **/repository**.

## Docker

You can build the docker image by running the following in the root of the repo:

```bash
docker build . -t server
```

There is also a docker image available on [dockerhub](https://hub.docker.com/repository/docker/schrammsm/fastapi_hf_inference/general) for your convenience.
You can pull a copy by running:

```bash
docker pull schrammsm/fastapi_hf_inference:1.0.0
```
