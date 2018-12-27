from compas_ghc.DataStructures.CGHDiagrams import CGHFormDiagram as FormDiagram
from compas_ghc.DataStructures.CGHDiagrams import CGHForceDiagram as ForceDiagram
from compas_tna.equilibrium import horizontal_nodal
from compas_tna.equilibrium import vertical_from_zmax

# from compas_kmmt.utilities.CodeTimer.CodeTimer import CodeTimer
# from compas_tna.equilibrium import vertical_from_zmax_rhino

__all__ = [
    'HorizontalEquilibrium_fromData',
    'VerticalEquilibrium_fromZMax_fromData'
]

def VerticalEquilibrium_fromZMax_fromData (formdata, zmax, kmax=100): # *args, **kwargs
    form = FormDiagram.from_data(formdata)
    scale = vertical_from_zmax(form, zmax, kmax)
    return form.to_data(), scale


def HorizontalEquilibrium_fromData (formdata, forcedata, alpha = 100, kmax = 100): # *args, **kwargs

    # codeTm = CodeTimer()
    # codeTm.Mark('rpc function called')
    form = FormDiagram.from_data(formdata)
    force = ForceDiagram.from_data(forcedata)
    # codeTm.Mark('diagram from data')
    horizontal_nodal (form, force, alpha, kmax)
    # codeTm.Mark('parallelisation')
    # f = XFunc('compas_tna.equilibrium.horizontal_nodal_xfunc', tmpdir=compas_tna.TEMP, callback=callback)
    formdata, forcedata = form.to_data(), force.to_data()
    # codeTm.Mark('diagram to data')
    return formdata, forcedata