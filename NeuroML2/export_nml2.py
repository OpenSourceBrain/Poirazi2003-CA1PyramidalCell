from pyneuroml.neuron import export_to_neuroml2
# from pyneuroml.neuron.nrn_export_utils import clear_neuron

export_to_neuroml2("../NEURON/test/test_Poirazi2003.hoc", 
                   "poirazi.cell.nml", 
                   includeBiophysicalProperties=True,
                   known_rev_potentials={'cal':-1, 'calH':140, 'can':140, 'car':140, 'cat':-1})

