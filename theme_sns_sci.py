from seaborn import set_theme
from matplotlib import rcParams
from matplotlib.pyplot import style, savefig
import os
from io import BytesIO
from PIL import Image
import win32clipboard
import win32con

#
# This visualization theme is based on and inspired by the work of **Koundinya Desiraju** for R's ggplot2, available at https://rpubs.com/Koundy/71792
#


# Function to configure the global theme for plots
def configure_theme(grid_set=False):
    """
    Sets up the global theme for visualizations, including color palette, font style,
    figure size, and axis configurations.
    """
    # Set the overall theme with a specific style, color palette, and font settings
    style.use("tableau-colorblind10")
    set_theme(style="ticks", font="Segoe UI", font_scale=1, palette=colour_palette())

    rcParams["figure.subplot.bottom"] = 0.2
    # Configure figure size and axis label styles
    rcParams["figure.figsize"] = (6, 4)  # Set the default figure size
    rcParams["axes.labelweight"] = "bold"  # Make axis labels bold
    rcParams["axes.titleweight"] = "bold"  # Make title bold
    rcParams["axes.titlesize"] = 18  # Title size
    rcParams["figure.titlesize"] = 12  # Subtitle size

    # Customize grid and axis spines (borders)
    rcParams["axes.grid"] = grid_set
    rcParams["grid.color"] = "#f0f0f0"

    rcParams["axes.spines.top"] = False  # Remove the top spine
    rcParams["axes.spines.right"] = False  # Remove the right spine
    rcParams["axes.spines.bottom"] = True  # Keep the bottom spine

    # Configure legend settings
    rcParams["legend.loc"] = "best"  # Position the legend in the best position
    rcParams["legend.frameon"] = False  # Disable the legend frame
    rcParams["legend.fontsize"] = 10  #  The legend font size


def colour_palette(num_colors=9):
    """
    Returns a customizable color palette. The function can be configured to
    return a specific number of colors from the predefined palette.

    :param num_colors: Number of colors to return (default is 9).
    :return: List of colors in hexadecimal format.
    """
    # Predefined color palette
    palette = [
        "#386cb0",  # Blue
        "#fdb462",  # Light orange
        "#7fc97f",  # Light green
        "#ef3b2c",  # Red
        "#662506",  # Dark brown
        "#a6cee3",  # Light blue
        "#fb9a99",  # Pink
        "#984ea3",  # Purple
        "#ffff33",  # Yellow
    ]

    # Ensure that no more colors are returned than what the palette contains
    return palette[:num_colors]


def save_plot(
    copy_to_clipboard=True, name="img", folder="image_out/", file_type="png", dpi=300
):
    """
    Saves a Seaborn plot to a specified folder and optionally copies it to the clipboard.

    Parameters:
        copy_to_clipboard (bool): Whether to copy the plot to the clipboard (default: True).
        name (str): The name of the image file (default: 'img').
        folder (str): The folder where the image will be saved (default: 'image_out/').
        file_type (str): The file format for the saved image (default: 'png').
        dpi (int): The resolution of the saved image (default: 300).
    """
    # Save plot to file
    if folder:
        try:
            folder_path = folder
            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            image_path = os.path.join(folder, f"{name}.{file_type}")
            savefig(image_path, format=file_type, dpi=dpi, bbox_inches="tight")
            print(f"Image saved to '{image_path}'.")
        except Exception as e:
            print(f"Error while creating folder '{folder_path}': {e}")

    # Copy plot to clipboard (only for png type)
    if copy_to_clipboard and (file_type == "png"):
        try:
            # Create a buffer to store the image
            buf = BytesIO()

            # Save the figure to the buffer
            savefig(buf, format="png", dpi=dpi, bbox_inches="tight")

            # Prepare the buffer for reading
            buf.seek(0)

            # Open the image using PIL
            image = Image.open(buf)

            # Copy the image to the clipboard
            output = BytesIO()
            image.convert("RGB").save(output, "BMP")
            data = output.getvalue()[14:]  # Remove BMP header
            output.close()

            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32con.CF_DIB, data)
            win32clipboard.CloseClipboard()

            print("Image copied to clipboard!")

        except Exception as e:
            print(f"Error while copying to clipboard: {e}")


if __name__ != "__main__":
    configure_theme()
