#installs:  pip install pymupdf numpy matplotlib geopandas shapely ipywidgets ipympl ipykernel
#python3 -m venv .venv
#.venv\Scripts\activate
#pip install pymupdf numpy matplotlib geopandas shapely ipywidgets ipympl ipykernel

#this is an attempt using a single code file rather than the notebooks, Currently working, however It seems to create 3 images each time


# Imports
import fitz
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import ipywidgets as widgets
from shapely.geometry import Point, LineString, Polygon
from shapely import affinity

# %% Load the PDF as a background image
doc = fitz.open('')
pix = doc[0].get_pixmap(dpi=150)
bg = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
H, W = bg.shape[:2]

# %% Helper that draws the PDF with a grid
def show_base(ax, xlim=None, ylim=None, grid_step=100):
    ax.imshow(bg, extent=[0, W, H, 0], zorder=0)      # y runs downward, like the image
    ax.set_xlim(xlim or (0, W)); ax.set_ylim(ylim or (H, 0))
    ax.set_xticks(np.arange(0, W, grid_step)); ax.set_yticks(np.arange(0, H, grid_step))
    ax.grid(True, color='cyan', alpha=0.4, linewidth=0.5)
    ax.tick_params(labelsize=7)

# %% Quick look at the PDF with its grid
from IPython import get_ipython
ip = get_ipython()
if ip:
    ip.run_line_magic('matplotlib', 'inline')
fig, ax = plt.subplots(figsize=(14, 10))
show_base(ax)

# %% (Optional) Click to capture coordinates -- run this on its own
from IPython import get_ipython
ip = get_ipython()
if ip:
    ip.run_line_magic('matplotlib', 'widget')
clicked = []

fig, ax = plt.subplots(figsize=(12, 9))
show_base(ax)

def on_click(event):
    if event.inaxes:
        clicked.append((round(event.xdata), round(event.ydata)))
        ax.plot(event.xdata, event.ydata, 'ro', markersize=4)
        fig.canvas.draw()
        print(clicked)

fig.canvas.mpl_connect('button_press_event', on_click)

# %% Hard-coded drawings (paste your clicked coordinates in here)
drawings = gpd.GeoDataFrame({
    'name': ['Gazebo_1', 'Gazebo_2', 'find_1'],
    'geometry': [
        Polygon([(400, 500), (480, 500), (480, 620), (400, 620)]),
        LineString([(300, 300), (700, 320)]),
        Point(550, 450),
    ]
})

def plot_layer(dx=0, dy=0, scale=1.0, rotation=0, alpha=0.5,
               x0=0, x1=W, y0=H, y1=0):
    g = drawings.copy()
    g['geometry'] = g.geometry.apply(lambda s: affinity.scale(s, scale, scale, origin=(0, 0)))
    g['geometry'] = g.geometry.apply(lambda s: affinity.rotate(s, rotation, origin=(0, 0)))
    g['geometry'] = g.geometry.apply(lambda s: affinity.translate(s, dx, dy))

    fig, ax = plt.subplots(figsize=(14, 10))
    show_base(ax, xlim=(x0, x1), ylim=(y0, y1))
    g.plot(ax=ax, facecolor='red', edgecolor='red', alpha=alpha, linewidth=2, zorder=1)
    plt.show()
    print(f"dx={dx}, dy={dy}, scale={scale}, rotation={rotation}")

widgets.interact(
    plot_layer,
    dx=widgets.FloatSlider(min=-W, max=W, step=1, value=0, continuous_update=False),
    dy=widgets.FloatSlider(min=-H, max=H, step=1, value=0, continuous_update=False),
    scale=widgets.FloatSlider(min=0.1, max=3, step=0.01, value=1, continuous_update=False),
    rotation=widgets.FloatSlider(min=-180, max=180, step=0.5, value=0, continuous_update=False),
    alpha=widgets.FloatSlider(min=0.1, max=1, step=0.1, value=0.5),
    x0=widgets.IntSlider(min=0, max=W, value=0, description='zoom x0'),
    x1=widgets.IntSlider(min=0, max=W, value=W, description='zoom x1'),
    y0=widgets.IntSlider(min=0, max=H, value=H, description='zoom y bottom'),
    y1=widgets.IntSlider(min=0, max=H, value=0, description='zoom y top'),
)

# %% Save once you're happy
drawings.to_file('my_drawings.geojson', driver='GeoJSON')
