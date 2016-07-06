### Original NEURON scripts for model

These files are the original model scripts for use with the [NEURON simulator](https://www.neuron.yale.edu/neuron/) as [submitted to ModelDB](https://senselab.med.yale.edu/modeldb/showModel.cshtml?model=20212).

Authors/original README:

#### Following is a brief overview of the contents of this directory:

- lib: This directory contains all the library functions called in the setup of the CA1 model cell as well as functions used in the experiments. Each of the functions is described in detail within the respective *.hoc file. 
- morphology: This directory contains the morphology of the cell as well as various lists of dendritic compartments used in the model setup and the experiments (files are in subdirectory n123).
- template: This directory contains a few files that define templates used in the model setup and experiments. Templates are described in the .hoc files. 
- experiment: This directory contains a selected set of experiments as described in the aforementioned publications. Within each subdirectory, the *.hoc files contain the NEURON code for the experiment while the run_* files are the executables used by the user to run the experiment. Each experiment is described in detail in the respective .hoc files.

#### Experminets briefly:

> Within each experiment directory, the *.hoc files contain the code to be executed and the respective run* files are the executables.

    cd <experiment>
    chmod +x run_<experiment_name>
    run_<experiment_name> # on a unix/linux promt

- tune-synapses: Code for tuning the AMPA/NMDA conductances of a synapse placed on any possible location of the cell such that a local single pulse stimulation will result in 5mV local depolarization. For tuning, the NMDA conductance for each position is calculated using the NMDA/AMPA ratio parameter provided by the user in /morphology/n123/nmda-ampa-ratio.hoc
- spike-train-attennuation: Code for (1) Backpropagating Action Potential generation (bpap.hoc) with somatic or dendritic stimulation and (2) somatic/dendritic single trace generation under control, A-current blockade and Ca++ current blockade (Hofman_traces.hoc). The aim of this experiment is (1) to ensure that BPAPs behave similarly to biophysical data that differentiate between somatic and dendritic stimulation as seen in Spruston et al, 1995 and Golding eta al 1999. (2) to ensure that cell response to short stimuli under control, A-current and A,Ca++-current blockade resemble biophysical data provided by Hofman et al 1997. The experiment is used to generate figure 2 in Poirazi,P. Brannon, T. and Mel, B.W. 'Online Supplement: About the Model.'
- hyperpolarization-current: This experiment is used to study the effect of h-current on (1) input resistances and (2) propagation of hyperpolarizing voltage traces at the somatic and dendritic regions and to ensure that model responses comply with physiological findings provided by Magee 1998.The experiment is used to generate figure 1 in Poirazi,P. Brannon, T. and Mel, B.W. 'Online Supplement: About the Model.'
- single-shock:	This directory contains code for the Cash and Yuste 1999 validation experiments shown in Poirazi,P. Brannon, T. and Mel, B.W. 'Arithmetic of Subthreshold Synaptic Summation in a Model CA1 Pyramidal Cell., figures 1 and 2.It includes code for single pulse stimulation of two synaptic stimuli (a) individually and (b) in combination. The stimuli are placed on either one or two trunk sections (Trunk_A.hoc, Trunk_AplusB.hoc) or within a single oblique dendrite (Apical_Tips.hoc). The aim of this experiment is to show that the model cell performs the same kind of synaptic integration for single pulse stimuli as the Cash and Yuste 1999 paper shows.
- single-branch-potency: This directory contains code for the generation of figures 3 and 4 in Poirazi,P. Brannon, T. and Mel, B.W. 'Arithmetic of Subthreshold Synaptic Summation in a Model CA1 Pyramidal Cell. as well as figure 3 in Poirazi,P. Brannon, T. and Mel, B.W. 'Pyramidal Neuron as 2-Layer Neural Network.' This includes code for 50Hz or single shock stimulation of two groups of synapses in apical obliques where synapses are stimulated (a) individually and (b) in combination. Stimulated synapses can be within the same oblique (A_feq.hoc, A+Bfreq.hoc, A_shock.hoc A+Bfreq.hoc) or in two different obliques (A+Cfreq.hoc, A+Cshock.hoc). The aim of this experiment is to show that synaptic integration is different for single pulse vs high frequency stimulation and for within versus between side branch stimulation.
- cluster-dispersion: This directory contains code for the generation of figures 2, 5 and 6 in Poirazi,P. Brannon, T. and Mel, B.W. 'Arithmetic of Subthreshold Synaptic Summation in a Model CA1 Pyramidal Cell.' This includes code for 50 Hz stimulation of a fixed number of excitatory synapses (32, 35, 36, 40, 45, 48, 49 or 63) which are distributed on apical obliques in increasingly clustered form. In some cases, inhibition is added to prevent uncontrolled spiking. Spike rate for different degrees of synaptic clustering, synchronicity and background activation. (Disperse_equal_sized.hoc, Disperse_equal_sized_tuft.hoc, Disperse_6_2.hoc) is used to validate a mathematical model that predicts cell firing rate for various synaptic stimuli (figures 5 & 6).

#### Reports:

> Clarification change: The conductance value for the h current has been scaled by a factor of 1000 in cell-setup.hoc in order to eliminate this scaling factor from the h.mod file and correct the reported value which appeared to be very high in the Online Supplement. This does not alter the current in the model at all. The correction is in the reported conductance value which becomes 0.1872 mS/cm^2 and not 18.72 mS/cm^2 as was reported in the Online Supplement.

> Bug Report: There was a typo in the nap.mod file pointed out by Michele Migliore which has now been corrected. It did not appear to have any significant  effect on the model behavior and results.

If you have any problems using the model, please feel free to contact me at poirazi@imbb.forth.gr.

