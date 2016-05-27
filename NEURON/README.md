### NEURON scripts for model

This folder contains files from the original model scripts [ModelDB:20212](https://senselab.med.yale.edu/modeldb/showModel.cshtml?model=20212) and additional simplified tester scripts (in order to create a .mep file, which against LEMS/NeuroML2 implementation could be tested).

To run the scripts, [install NEURON](https://www.neuron.yale.edu/neuron/download) and run:

    git clone https://github.com/andrisecker/Poirazi2003-CA1Pyr.git  # clone git repository
    cd Poirazi2003-CA1Pyr/NEURON/test
    nrnivmodl  # compile .mod files
    nrngui test_Poirazi2003.hoc  # runs a simulation (single cell, current clamp) and saves data
