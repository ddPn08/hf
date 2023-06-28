from setuptools import setup

setup(
    name="hf",
    packages=["hf"],
    version="0.0.1",
    url="https://github.com/ddPn08/hf",
    description="CLI tool for Huggingface filesystem api.",
    author="ddPn08",
    author_email="contact@ddpn.world",
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "hf=hf.main:main",
        ]
    },
)
