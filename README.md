# hf
CLI tool for HuggingFace filesystem api.

## Installation

```bash
pip install git+https://github.com/ddPn08/hf.git
```

## Usage

```bash
hf cd /models/runwayml/stable-diffusion-v1-5

# runwayml/stable-diffusion-v1-5
```

```bash
hf pwd

# runwayml/stable-diffusion-v1-5
```

```bash
hf ls -a -l -h

#       0.0B              feature_extractor/
#       0.0B              safety_checker/
#       0.0B              scheduler/
#       0.0B              text_encoder/
#       0.0B              tokenizer/
#       0.0B              unet/
#       0.0B              vae/
#     1.5KiB Oct 20 12:18 .gitattributes
#    14.1KiB Dec 19 15:29 README.md
#     541.0B May 05 10:38 model_index.json
#     4.0GiB Oct 20 01:10 v1-5-pruned-emaonly.ckpt
#     4.0GiB Jan 27 08:19 v1-5-pruned-emaonly.safetensors
#     7.2GiB Oct 20 12:18 v1-5-pruned.ckpt
#     7.2GiB Jan 27 08:19 v1-5-pruned.safetensors
#     1.8KiB Oct 20 09:30 v1-inference.yaml
```

```bash
hf cat README.md > README.md
```

```bash
hf dl v1-5-pruned.safetensors
```

Run `hf --help` for details.