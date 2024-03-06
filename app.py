import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from shiny.express import ui, input, render

# Add page options for the overall app.
ui.page_opts(title="My First Histogram Plot",fillable=True)

# Create a sidebar with a slider input
with ui.sidebar():
    # Add a slider for specifying the number of bins in the histogram.
    # The ui.input_slider function is called with 5 arguments:
    # 1. A string id ("selected_number_of_bins") that ultimately identifies this input.
    # 2. A string label ("Number of Bins") to be displayed alongside the slider.
    # 3. An integer representing the minimum number of bins (1)
    # 4. An integer representing the maximum number of bins (200)
    # 5. An integer representing the initial value of the slider (100)
    ui.input_slider("selected_number_of_bins", "Number of Bins", 1, 200, 100)

@render.plot(alt="A histogram showing random data distribution")
def draw_histogram():
    count_of_point: int = 500
    np.random.seed(25)
    random_data_array = 200 + 50 * np.random.randn(count_of_point)
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True, color="green")
        
@render.plot(alt="My First Random Scatterplot")
def scatterplot():
    count_of_point: int = 500
    np.random.seed(42)
    x = np.random.randn(count_of_point)
    y = np.random.randn(count_of_point)
    sns.scatterplot(x=x, y=y, color='blue')
