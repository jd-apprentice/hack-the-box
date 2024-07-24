# Depix

Depix is a tool for recovering passwords from pixelized screenshots. This implementation works on pixelized images that were created with a linear box filter.

## Usage

1. First, we need to extract the individual characters from the screenshots. We can do this by running the following command:

```bash
pdfimages <pdf-file> <output-file>
```

2. Next, we can use the Depix tool to recover the password. We need to specify the pixelized image, as well as the reference image that contains the characters we are looking for. We can do this by running the following command:

```bash
python3 depix.py -p <pixelized-image>.ppm -s <reference-image>
python3 depix.py -p sample-000.ppm -s searchimages/debruinseq_notepad_Windows10_closeAndSpaced.png
```