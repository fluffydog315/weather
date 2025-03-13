# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

pip install jupyterlab-spellchecker

# ! ls
# ! pwd

# ## Use command + click multiple places to edit 
# ##### try it

123567 
123567 
123567 

pip install tqdm

pip install ipywidgets

# + editable=true slideshow={"slide_type": ""} tags=["active_ipynb   "]
# has active_ipynb
from tqdm.notebook import tqdm

# + editable=true slideshow={"slide_type": ""} tags=["active_py"]
# has active_py tag
from tqdm import tqdm

# + editable=true slideshow={"slide_type": ""}
import time 
for i in tqdm(range(10)):
    time.sleep(.5)

# + editable=true slideshow={"slide_type": ""}
## show all execution time
# %%time
for i in tqdm(range(10)):
    time.sleep(.5)


# + editable=true slideshow={"slide_type": ""}
# %%timeit
sum(x ** 2 for x in range(1, 100000, 10))

# + editable=true slideshow={"slide_type": ""}
#print all output
#default is to print the last line
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# + editable=true slideshow={"slide_type": ""}
sum(range(10))
print(sum(range(10)))
sum(range(10))

# + editable=true slideshow={"slide_type": ""}

