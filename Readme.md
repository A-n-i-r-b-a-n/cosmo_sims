# About ***cosmo_sims***

cosmo_sims is a cosmological simulation visualisation project which was created
to visualise  various cosmological simulations I ran using a moving mesh code, 
cosmological hydrodynamics simulation code called ***Arepo***

The project directory is strutured as follows:

/cosmo_sims/
|
|
|-------/dm_only/
|        |
|        |___data_vis.py
|        |
|        |---snap_016.hdf5
|
|
|-------/dm_hydro1/
|         |       
|         |---data_vis.py
|         |
|         |---snap_016.hdf5
|
|
|-------/dm_hydro2/
|         |
|         |---data_vis.py
|         |
|         |---snap_016.hdf5
|
|
|_______/star_formation1/
|        |
|        |---data_vis.py
|        |
|        |---snap_014.hdf5
|
|
|______/star_formation2/
        |
        |---data_vis.py
        |
        |---snap_013.hdf5

The **snap_xxx.hdf5** files are the data files that contain the simulation data
whereas the **data_vis.py** files are there for the visualisation purpose. It has
been written such that the user only needs to run the python file to open the inter-
active cosmological box. The user can ply around with various color combinations used 
to label different particle types, eg. star paricles, darek matter particles and gas
particles. 


## Installation

The user can install the project on their system by following the below steps.

### Clone the repository

Copy the project url from github and run the following commands:

```bash
git clone project_url
cd cosmo_sims
```
### Install required python packages

From the paret project directory create a python environment
on your pc and install the required python packages;

**For Linux and MacOs (On terminal):**
```bash
python3 -m venv new_env
source new_env/bin/activate

python3 -m pip install -r requirements.txt     
```
**For Windows(On windows powershell)**
```bash
python -m venv new_env
.\new_env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Running the data_vis.py files
If the newly created python environment is active, then you can navigate
to any of the project subfolders and and run the ***data_vis.py*** files 
for example; 

```bash
cd dm_hydro1
python3 data_vis.py
```

An interactive cosmological simulation box should open, drag the box to rotate it along
all three direction, scroll in and scroll out to zoom in and zoom our respectively. 



