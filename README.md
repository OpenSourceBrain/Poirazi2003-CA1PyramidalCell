### multicompartmental CA1PyramidalCell model by Poirazi et al.

Arithmetic of subthreshold synaptic summation in a model CA1 pyramidal cell. Porazi P, Brannon T, Mel BW (2003a) [Neuron 37:977-987](http://www.ncbi.nlm.nih.gov/pubmed/12670426)

Pyramidal Neuron as Two-Layer Neural Network. Porazi P, Brannon T, Mel BW (2003b) [Neuron 37:989-999](http://www.ncbi.nlm.nih.gov/pubmed/12670427)

### NEURON version of model:

This model was originally developed in [NEURON](https://www.neuron.yale.edu/neuron/)

More details on the original NEURON version of this model [here](/ModelDB_NEURON)

In addition we created a simplified NEURON version, with a single cell and current clamp (in order to create a .mep file, which against LEMS/NeuroML2 implementation could be tested). More detailes on this NEURON version [here](/NEURON)

-------------------------------------------------------------------------------------------------------------------------------

### NeuroML2/LEMS version of model

This model will be converted to NeuroML2/LEMS ... see more [here](/NeuroML2)

Issues:
- T-type Ca++ channel (see more [here](https://github.com/OpenSourceBrain/Poirazi2003-CA1PyramidalCell/tree/master/NeuroML2/channels/test_Cadynamics))
- the setup of the NEURON model uses a custom distance measurement (perpendicular distance), which is not reproducable in NeuroML2  -> we suggest to keep the morphology and the channels, but reoptimise the model 

[![Build Status](https://travis-ci.org/OpenSourceBrain/Poirazi2003-CA1PyramidalCell.svg?branch=master)](https://travis-ci.org/OpenSourceBrain/Poirazi2003-CA1PyramidalCell)

