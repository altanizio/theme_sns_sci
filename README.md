# theme_sns_sci

Repository containing a **custom theme for Seaborn** focused on scientific and professional visualizations, with style configuration, color palette, and options to automatically save plots, including copying the image to the clipboard on Windows.

---

## Description

`theme_sns_sci` provides a consistent and elegant visual setup for plots created with Seaborn and Matplotlib. It includes:

- A custom theme with a clean and readable style using the **Segoe UI** font;
- A color palette optimized for scientific visualization and colorblind-friendly;
- Configuration of font size, weight, and style for titles and labels;
- Control over grids, spines, and legends for clearer and minimalist plots;
- A function to save plots to disk and copy the image directly to the clipboard (Windows only).

This visualization theme is based on and inspired by the work of **Koundinya Desiraju** for R's ggplot2, available at [https://rpubs.com/Koundy/71792](https://rpubs.com/Koundy/71792).
---

## Installation

Copy the `theme_sns_sci.py` file into your project or install it as you prefer.

---

## Usage

### Configure the theme

```python
import seaborn as sns
import matplotlib.pyplot as plt
from theme_sns_sci import configure_theme, save_plot

configure_theme()

# After creating the plot
save_plot(name="example_plot", folder="images", file_type="png", dpi=300)


