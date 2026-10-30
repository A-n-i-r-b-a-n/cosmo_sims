#importing important libraries
import numpy as np
import h5py as h
import pyvista as pv


##########################################################################################
# Loading Snap Files
##########################################################################################

def load_snap(snap, **kwargs):
    """
    Takes in snap number and other arguments to extract the parameters inside an .hdf5 file

    snap: integere type; refers to the snap number

    PartType: integer type; eg. in zoom in gravit only simulations 1 refers to the high res.
    dark matter particles whereas, 2 refers to the low res. dark matter particles

    path: string type; refers to the path where the snap files exist, takes the current dir-
    ectory if no argument is given

    param: string type; extracts the particular parameter if mentioned, outputs the enti-
    re dataframe if no argument is given
    """
    if 'path' in kwargs.keys():
        path = kwargs['path']
    else:
        path = '.'

    file = f'{path}/snap_{snap:03d}.hdf5'
    
    if len(kwargs) == 0:
        s = h.File(file, 'r')

    else:

        if 'PartType' in kwargs.keys():
            pt = kwargs['PartType']
        else:
            pt = 1

        if 'param' in kwargs.keys():
            param = kwargs['param']
            s = np.array(h.File(file, 'r')[f'PartType{pt}'][param][:])
        else: 
            s = h.File(file, 'r')[f'PartType{pt}']

    return s
#--------------------------------------------------------------------------------------------#

#################################################################################
# Plotting interactive dm and gas box
#################################################################################
def box_multiparticle(label, dm_data, **kwargs):
    """
    The function takes the dark matter coordinates and gas/baryonic matter coordi-
    nates and plots the 3D box with appropriate color code

    label: lsit type, contains the list of labels for x, y and z axes.

    dm_data: numpy ndarray type, refers to the coordinates of the dark matter part-
    icles

    gas_data: numpy ndarray type, refers to the coordinates of the gas/baryonic par-
    ticles 

    sf_data: numpy ndarray type, refers to the coordinates of the star particles.

    dm_color: string/touple/vector type, refers to the color of dm particles.

    gas_color: string/touple/vector type, refers to the color of gas particles.

    sf_color: string/touple/vector type, refers to the color of star particles

    scale: int type, refers to the scale of the box, eg. 1e3 


    """

    if 'dm_color' in kwargs.keys():
        dmc = kwargs['dm_color']
    else:
        dmc = 'red'

    if 'scale' in kwargs.keys():
        scl = kwargs['scale']
    else:
        scl = 1
    
    plotter = pv.Plotter()

    plotter.add_points(
    dm_data/scl, #dm
    color= dmc,
    point_size=1,
    render_points_as_spheres=False,
    opacity=0.35,
    label="High-resolution DM"
)

    if 'gas_data' in kwargs.keys():

        if 'gas_color' in kwargs.keys():
            gc = kwargs['gas_color']
        else:
            gc = 'white'
        
        gas_data = kwargs['gas_data']
        plotter.add_points(
        gas_data/scl, #gas
        color= gc,
        point_size=1,
        render_points_as_spheres=False,
        opacity=0.35,
        label="High-resolution gas particles"
        )

    if 'sf_data' in kwargs.keys():

        if 'sf_color' in kwargs.keys():
            sfc = kwargs['sf_color']
        else:
            sfc = 'yellow'
        
        sf_data = kwargs['sf_data']
        plotter.add_points(
        sf_data/scl, #sf
        color= sfc,
        point_size=1,
        render_points_as_spheres=False,
        opacity=0.35,
        label="High-resolution star particles"
        )

    if 'lrdm_data' in kwargs.keys():
        if 'lrdm_color' in kwargs.keys():
            lrdmc = kwargs['lrdm_color']
        else:
            lrdmc = 'gray'
   
        lrdm_data = kwargs['lrdm_data']
        plotter.add_points(
        lrdm_data/scl, #lrdm
        color= lrdmc,
        point_size=1,
        render_points_as_spheres=False,
        opacity=0.35,
        label="Low-resolution dark matter particles"
        )

    if 'bh_data' in kwargs.keys():
            if 'bh_color' in kwargs.keys():
                bhc = kwargs['bh_color']
            else:
                bhc = 'blue'
       
            bh_data = kwargs['lrdm_data']
            plotter.add_points(
            bh_data/scl, #bh
            color= bhc,
            point_size=1,
            render_points_as_spheres=False,
            opacity=0.35,
            label="Black hole particles"
            )

    plotter.set_background('black')

    plotter.show_bounds(
    location='outer',
    xtitle= label[0],
    ytitle= label[1],
    ztitle= label[2],

    color = 'white',
    font_size = 10,
    n_xlabels = 5,
    n_ylabels = 5,
    n_zlabels = 5 )
    plotter.add_axes()
    plotter.show()
    
    return None
#-------------------------------------------------------------------------------#


gas_coords = load_snap(14, PartType = 0, param = 'Coordinates')
dm_coords = load_snap(14, PartType = 1, param = 'Coordinates')
sf_coords = load_snap(14, PartType = 4, param = 'Coordinates')

lbl = ['x (Mpc)', 'y (Mpc)', 'z (Mpc)']

box_multiparticle(label = lbl,
                            dm_data = dm_coords, 
                            gas_data = gas_coords, 
                            sf_data = sf_coords, 
                            dm_color = 'red', 
                            gas_color = 'white', 
                            sf_color = 'yellow',
                            scale = 1e3
)
