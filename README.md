# Lab 2 - Prediction, Transforms and Entropy Coding

[Open the notebook](DT096A_Lab2.ipynb) · [Browse exported results](results/)

This lab compares how much image content can be predicted, concentrated in a transform, or coded into fewer bits. Three grayscale inputs are used: **clock**, **gradients**, and **ManWoman**. The full experiment is implemented in one longer Colab code cell, and its saved output is preserved.

## Section 3 - Information variation

- Global histograms and entropy for all three images
- Local entropy maps using **32 × 32** tiles
- Comparisons of selected **96 × 96** crops

The interesting part here is that the entropy of an entire image does not tell the whole story. A smoother crop and a textured crop can have quite different distributions, even when both come from the same source.

![Image histograms and local entropy maps](results/01_global_histograms_entropy_maps.png)

## Section 4 - Prediction and residuals

Prediction experiments use neighboring pixels to form an estimate of the next pixel. The notebook records the prediction-error image and its signed residual statistics, then compares entropy values. Conditional-entropy calculations use aligned neighboring-pixel pairs for consistency.

![Prediction residual comparisons](results/04_residuals_clock.png)

**Important detail:** a shifted/clipped residual histogram is useful for display, but entropy coding and statistical comparisons use the original signed residual values. Treating a display image as the true residual distribution would change the interpretation.

## Section 5 - DCT and KLT

Block transforms are tested on scaled inputs with **8 × 8 and 16 × 16** block sizes. The notebook compares DCT and a data-dependent **KLT** basis using different fractions of retained coefficients: **5%, 10%, 25%, 50%, 75% and 100%**. Figures and CSVs record reconstruction errors and energy retention.

![Transform reconstruction comparison](results/06_reconstructions_clock_8.png)

The KLT is learned from patches of the same evaluated image. This is useful for a controlled transform comparison, but it is **not** a separately trained general-purpose codec. The storage cost of the KLT basis is not included in the transform comparison.

## Section 6 - Huffman and arithmetic coding

The coding section uses image crops and prediction residuals, then compares **static Huffman coding** with **arithmetic coding**. Both use the same empirical symbol model, and decoded data are checked against their inputs. Results include code-length measurements and generated binary streams.

![Entropy coding comparison](results/08_coding_clock.png)

**Important detail:** the measured coded-bit lengths do not include all the overhead needed for a standalone image file, such as transmission of the symbol model and headers. The figures therefore describe coding performance under the experiment's assumptions, **not** a full-image compression ratio.

## Results folder

`results/` contains PNG plots, CSV tables, coding models, binary streams and short extracted code snippets. The original exported files are kept rather than recreating plots from guesses. Helpful starting points are `global_entropy.csv`, `predictor_entropy.csv`, `transform_results.csv` and `coding_comparison.csv`.

## Running the notebook

Use Google Colab (CPU) or an equivalent Python environment. The cell expects three files named exactly `clock.png`, `gradients.png` and `ManWoman.png`, either through the Colab upload prompt or in a local `lab2_inputs/` folder. **Those original three files were not included in the upload**, so the saved output can be viewed now but a clean rerun needs the inputs.

Packages include NumPy, Pillow, Matplotlib and SciPy. The notebook writes a `DT096A_Lab2_results` directory when executed.
