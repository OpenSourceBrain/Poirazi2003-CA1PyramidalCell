### NEURON scripts for model

The [test](/test/) folder contains files from the original model scripts [ModelDB:20212](https://senselab.med.yale.edu/modeldb/showModel.cshtml?model=20212) and additional simplified tester scripts (in order to create a .mep file, which against LEMS/NeuroML2 implementation could be tested).

The entire setup of the model has been concatenated in the [test/CA1Pyr.hoc](https://github.com/OpenSourceBrain/Poirazi2003-CA1PyramidalCell/tree/master/NEURON/test).
> Thanks for the help of George Kastelakis

To run the scripts, [install NEURON](https://www.neuron.yale.edu/neuron/download) and run:

    git clone https://github.com/OpenSourceBrain/Poirazi2003-CA1PyramidalCell.git  # clone git repository
    cd Poirazi2003-CA1PyramidalCell/NEURON/test
    nrnivmodl  # compile .mod files
    nrngui test_Poirazi2003.hoc  # runs a simulation (single cell, current clamp) and saves data
