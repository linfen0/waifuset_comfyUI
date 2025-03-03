from setuptools import setup, find_packages

setup(
    name="waifuset",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "tqdm",
        "numpy",
        "pillow",
        "imagehash",
        "gradio==4.44.1",
        "opencv-python-headless",
        "torch",
        "torchvision",
        "pytorch-lightning",
    ],
    python_requires=">=3.7",
) 