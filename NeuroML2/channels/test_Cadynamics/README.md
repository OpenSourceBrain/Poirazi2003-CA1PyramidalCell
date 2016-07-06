### Ca++ dynamics

The internal Ca++ dynamics ([capool](https://github.com/OpenSourceBrain/Poirazi2003-CA1PyramidalCell/blob/master/NeuroML2/channels/capool.nml)), the Ca++ channels ([cal](https://github.com/OpenSourceBrain/Poirazi2003-CA1PyramidalCell/blob/master/NeuroML2/channels/cal.channel.nml), [calH](https://github.com/OpenSourceBrain/Poirazi2003-CA1PyramidalCell/blob/master/NeuroML2/channels/calH.channel.nml), [car](https://github.com/OpenSourceBrain/Poirazi2003-CA1PyramidalCell/blob/master/NeuroML2/channels/car.channel.nml)) and the Ca++ dependent channels ([cagk](https://github.com/OpenSourceBrain/Poirazi2003-CA1PyramidalCell/blob/master/NeuroML2/channels/cagk.channel.nml), [kca](https://github.com/OpenSourceBrain/Poirazi2003-CA1PyramidalCell/blob/master/NeuroML2/channels/kca.channel.nml)) are working fine.

But we have a problem with the T-type Ca++ channel ([.mod](https://github.com/OpenSourceBrain/Poirazi2003-CA1PyramidalCell/blob/master/NEURON/test/cat.mod), [cat.channel.nml](https://github.com/OpenSourceBrain/Poirazi2003-CA1PyramidalCell/blob/master/NeuroML2/channels/cat.channel.nml)) which is using a dummy Ca++ ion in the original mod file (because "The T-current does not activate calcium-dependent currents.")

    cd NEURON
    python test_Ca_nrn.py
    cd ../NeuroML2
    python test_Ca_jnml.py
