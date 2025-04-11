import pyirk as p
import sympy as sp

from ipydex import IPS, activate_ips_on_exception  # noqa




ag = p.irkloader.load_mod_from_path(r"C:\Users\Julius Fiedler\Documents\Code\irk\irk-data\ocse\agents1.py", prefix="ag")



omt = p.irkloader.load_mod_from_path(r"C:\Users\Julius Fiedler\Documents\Code\irk\irk-data\omt\omt.py", prefix="omt")


__URI__ = "irk:/ocse/0.2/auto_import_formalized_statements"

keymanager = p.KeyManager()
p.register_mod(__URI__, keymanager)
p.start_mod(__URI__)

# these entities are declared here all at once in order to avoid referencing issues when setting relations.
# the relations of these entities are set below with the update method. This update method is called exactly once.
I40233 = p.create_item(R1__has_label="memristor stack")
I99429 = p.create_item(R1__has_label="stack component")
R48517 = p.create_relation(R1__has_label="has stack component")
R11809 = p.create_relation(R1__has_label="has memristor stack")
R17275 = p.create_relation(R1__has_label="has position")
R64265 = p.create_relation(R1__has_label="is at outer position")
I18540 = p.create_item(R1__has_label="publication: Memristive crossbar arrays for brain-inspired computing")
I60787 = p.create_item(R1__has_label="Wang, Z.")
I67882 = p.create_item(R1__has_label="publication: Memristors with difusive dynamics as synaptic emulators for neuromorphic computing")
I34722 = p.create_item(R1__has_label="Li, C.")
I74868 = p.create_item(R1__has_label="publication: Tree-dimensional crossbar arrays of self-rectifying Si/SiO2/Si memristors")
I95468 = p.create_item(R1__has_label="Midya, R.")
I16106 = p.create_item(R1__has_label="publication: Anatomy of Ag/Hafnia-based selectors with 1010 nonlinearity")
I79357 = p.create_item(R1__has_label="Huang, J.-J.")
I8074 = p.create_item(R1__has_label="Tseng, Y.-M.")
I47536 = p.create_item(R1__has_label="Hsu, C.-W.")
I85771 = p.create_item(R1__has_label="Hou, T.-H.")
I84727 = p.create_item(R1__has_label="publication: Bipolar nonlinear Ni/ TiO2/Ni selector for 1S1R crossbar array applications")
I93588 = p.create_item(R1__has_label="Shin, J.")
I9860 = p.create_item(R1__has_label="publication: TiO2-based metal–insulator–metal selection device for bipolar resistive random access memory cross-point application")
I85989 = p.create_item(R1__has_label="Govoreanu, B.")
I15339 = p.create_item(R1__has_label="publication: High-performance metal–insulator–metal tunnel diode selectors")
I87633 = p.create_item(R1__has_label="Woo, J.")
I6557 = p.create_item(R1__has_label="publication: Electrical and reliability characteristics of a scaled (∼30nm) tunnel barrier selector (W/Ta2O5/TaOx/TiO2/TiN) with excellent performance (JMAX>107A/cm2)")
I57087 = p.create_item(R1__has_label="Lee, W.")
I77061 = p.create_item(R1__has_label="publication: Varistor-type bidirectional switch (JMAX>107A/cm2 , selectivity ∼104 ) for 3D bipolar resistive memory arrays")
I17932 = p.create_item(R1__has_label="Choi, B. J.")
I18505 = p.create_item(R1__has_label="publication: Trilayer tunnel selectors for memristor memory cells")
I72084 = p.create_item(R1__has_label="Kawahara, A.")
I19460 = p.create_item(R1__has_label="publication: An 8 Mb multi-layered cross-point ReRAM macro with 443 MB/s write throughput")
I72376 = p.create_item(R1__has_label="publication: Termally stable integrated Se-based OTS selectors with >20MA/cm2 current drive, >3.103 half-bias nonlinearity, tunable threshold voltage and excellent endurance")
I92025 = p.create_item(R1__has_label="Kim, S. G.")
I93207 = p.create_item(R1__has_label="publication: Breakthrough of selector technology for cross-point 25-nm ReRAM")
I38568 = p.create_item(R1__has_label="Son, M.")
I24422 = p.create_item(R1__has_label="publication: Excellent selector characteristics of nanoscale VO2 for high-density bipolar ReRAM applications")
I24045 = p.create_item(R1__has_label="Kim, W. G.")
I26160 = p.create_item(R1__has_label="publication: NbO2-based low power and cost efective 1S1R switching for high density cross point ReRAM application")
I39551 = p.create_item(R1__has_label="Cha, E.")
I94055 = p.create_item(R1__has_label="publication: Nanoscale (∼10nm) 3D vertical ReRAM and NbO2 threshold selector with TiN electrode")
I36185 = p.create_item(R1__has_label="Lee, M.-J.")
I31023 = p.create_item(R1__has_label="publication: Highly-scalable threshold switching select device based on chalcogenide glasses for 3D nanoscaled memory arrays")
I63537 = p.create_item(R1__has_label="Sun, J.")
I52555 = p.create_item(R1__has_label="publication: Physically transient threshold switching device based on magnesium oxide for security application")
I27376 = p.create_item(R1__has_label="Wang, G.")
I20440 = p.create_item(R1__has_label="publication: High‐performance and low‐power rewritable SiO*x* 1 kbit one diode–one resistor crossbar memory array")
I13184 = p.create_item(R1__has_label="publication: Vacancy-modulated conductive oxide resistive RAM (VMCO-RRAM): an area-scalable switching current, self-compliant, highly nonlinear and wide on/of-window resistive switching cell")
I1679 = p.create_item(R1__has_label="Song, M.")
I89283 = p.create_item(R1__has_label="publication: Self-selective characteristics of nanoscale VOx devices for high-density ReRAM applications")
I72952 = p.create_item(R1__has_label="Lu, D.")
I6909 = p.create_item(R1__has_label="publication: Investigations of conduction mechanisms of the self-rectifying n<sup>+</sup>Si-HfO2-Ni RRAM devices")
I53460 = p.create_item(R1__has_label="Wang, M. J.")
I68385 = p.create_item(R1__has_label="Gao, S.")
I44786 = p.create_item(R1__has_label="Zeng, F.")
I6037 = p.create_item(R1__has_label="Song, C.")
I31376 = p.create_item(R1__has_label="Pan, F.")
I3139 = p.create_item(R1__has_label="publication: Unipolar resistive switching with forming-free and self-rectifying efects in Cu/HfO2/n-Si devices")
I31567 = p.create_item(R1__has_label="Kim, K.-H.")
I75821 = p.create_item(R1__has_label="Jo, S. H.")
I96458 = p.create_item(R1__has_label="Gaba, S.")
I18688 = p.create_item(R1__has_label="Lu, W.")
I26296 = p.create_item(R1__has_label="publication: Nanoscale resistive memory with intrinsic diode characteristics and long endurance")
I75465 = p.create_item(R1__has_label="Ni/TiO2/Ni")
I93192 = p.create_item(R1__has_label="Pt/TiO2/TiN")
I7316 = p.create_item(R1__has_label="TiN/Ta2O5/TiN")
I47350 = p.create_item(R1__has_label="W/Ta2O5/TaOx/TiO2/TiN")
I84610 = p.create_item(R1__has_label="Pt/TaOx/TiO2/TaOx/Pt")
I33761 = p.create_item(R1__has_label="Pt/TaN1+x/Ta2O5/TaN1+x/Pt")
I63613 = p.create_item(R1__has_label="TaN/SiNx/TaN")
I94114 = p.create_item(R1__has_label="TiN/GexSe1-x/TiN")
I37565 = p.create_item(R1__has_label="TiN/As:SiO2/TiN")
I88176 = p.create_item(R1__has_label="Pt/VO2/Pt")
I28585 = p.create_item(R1__has_label="TiN/NbO2/TiN")
I16241 = p.create_item(R1__has_label="TiN/NbO2/W")
I12074 = p.create_item(R1__has_label="TiN/AsTeGeSiN/TiN")
I30366 = p.create_item(R1__has_label="W/Ag/MgO/Ag/W")
I76063 = p.create_item(R1__has_label="Pt/Ag:SiOxNy/Pt")
I82668 = p.create_item(R1__has_label="Pd/Ag/HfO2/Ag/Pd")
I79359 = p.create_item(R1__has_label="TiN/Al2O3/TiO2/TiN")
I51636 = p.create_item(R1__has_label="W/VOx/Pt")
I38505 = p.create_item(R1__has_label="p-Si/SiO2/n-Si")
I91063 = p.create_item(R1__has_label="Ni/HfO2/n-Si")
I96093 = p.create_item(R1__has_label="Cu/HfO2/n-Si")
I31934 = p.create_item(R1__has_label="Ag/a-Si/p-poly-Si")
I90518 = p.create_item(R1__has_label="publication: Hardware implementation of memristorbased artificial neural networks")
I11228 = p.create_item(R1__has_label="Yao, P.")
I46274 = p.create_item(R1__has_label="publication: Fully hardware-implemented memristor convolutional neural network")
I28662 = p.create_item(R1__has_label="Cai, F.")
I35553 = p.create_item(R1__has_label="publication: A fully integrated reprogrammable memristor-CMOS system for efficient multiply-accumulate operations")
I48163 = p.create_item(R1__has_label="Wan, W.")
I66013 = p.create_item(R1__has_label="publication: A compute-in-memory chip based on resistive random-access memory")
I79007 = p.create_item(R1__has_label="Mochida, R.")
I1871 = p.create_item(R1__has_label="publication: A 4M synapses integrated analog ReRAM based 66.5 TOPS/W neural-network processor with cell current controlled writing and flexible network architecture")
I8544 = p.create_item(R1__has_label="Su, F.")
I66252 = p.create_item(R1__has_label="publication: A 462GOPs/J RRAM-based nonvolatile intelligent processor for energy harvesting IoE system featuring nonvolatile logics and processing-in-memory")
I16648 = p.create_item(R1__has_label="Kiani, F.")
I91231 = p.create_item(R1__has_label="Yin, J.")
I5202 = p.create_item(R1__has_label="Joshua Yang, J.")
I66876 = p.create_item(R1__has_label="Xia, Q.")
I17956 = p.create_item(R1__has_label="publication: A fully hardware-based memristive multilayer neural network")
I10396 = p.create_item(R1__has_label="publication: CMOS-integrated nanoscale memristive crossbars for CNN and optimization acceleration")
I79049 = p.create_item(R1__has_label="Pedretti, G.")
I3375 = p.create_item(R1__has_label="publication: Redundancy and analog slicing for precise inmemory machine learning - Part I: Programming techniques")
I91390 = p.create_item(R1__has_label="publication: Redundancy and analog slicing for precise inmemory machine learning - Part II: Applications and benchmark")
I45686 = p.create_item(R1__has_label="publication: Fully memristive neural networks for pattern classification with unsupervised learning")
I87710 = p.create_item(R1__has_label="Bocquet, M.")
I19647 = p.create_item(R1__has_label="publication: In-memory and error-immune differential RRAM implementation of binarized deep neural networks")
I79796 = p.create_item(R1__has_label="Chen, W. H.")
I3560 = p.create_item(R1__has_label="publication: CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors")
I78447 = p.create_item(R1__has_label="Hirtzlin, T.")
I72007 = p.create_item(R1__has_label="publication: Digital biologically plausible implementation of binarized neural networks with differential hafnium oxide resistive memory arrays")
I36884 = p.create_item(R1__has_label="Wu, T. F.")
I87369 = p.create_item(R1__has_label="publication: A 43pJ/Cycle Non-Volatile Microcontroller with 4.7μs Shutdown/Wake-up Integrating 2.3-bit/Cell Resistive RAM and Resilience Techniques")
I34943 = p.create_item(R1__has_label="Au/Pd/WOx/Au")
I69977 = p.create_item(R1__has_label="TiN/TaOx/HfOx/TiN")
I56497 = p.create_item(R1__has_label="Pt/Ta/Ta2O5/Pt/Ti")
I55117 = p.create_item(R1__has_label="Ta/TaOx/Pt")
I81948 = p.create_item(R1__has_label="W/TiN/TiON")
I8432 = p.create_item(R1__has_label="Pt/SiOxAg/Pt/Ti")
I49144 = p.create_item(R1__has_label="Ta/Pd/HfO2/Pt/Ti")
I13384 = p.create_item(R1__has_label="TiN/HfO2/Ti/TiN")
I75653 = p.create_item(R1__has_label="W/Ta2O5/TaOx/W")
I73280 = p.create_item(R1__has_label="AlCu/TiN/Ti/HfO2/TiN")
I39529 = p.create_item(R1__has_label="TiN/HfO2/TaOx/TiN")


########################################################################################################################
# content:
########################################################################################################################






I40233["memristor stack"].update_relations(
    R4__is_instance_of=p.I2["Metaclass"],
    
)



I99429["stack component"].update_relations(
    R4__is_instance_of=p.I2["Metaclass"],
    
)











R48517["has stack component"].update_relations(
    R8__has_domain_of_argument_1=I40233["memristor stack"],
    R11__has_range_of_result=I99429["stack component"],
    
)



R11809["has memristor stack"].update_relations(
    R8__has_domain_of_argument_1=ag.I6591["source document"],
    R11__has_range_of_result=I40233["memristor stack"],
    
)



R17275["has position"].update_relations(
    R11__has_range_of_result=p.I37["integer number"],
    
)
has_position = p.QualifierFactory(R17275["has position"])



R64265["is at outer position"].update_relations(
    R11__has_range_of_result=p.I53["bool"],
    
)
is_at_outer_position = p.QualifierFactory(R64265["is at outer position"])


# 2019 
I18540["publication: Memristive crossbar arrays for brain-inspired computing"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=["Qiangfei Xia", "J. Joshua Yang"],
    ag__R8434__has_title="Memristive crossbar arrays for brain-inspired computing",
    ag__R8435__has_year=2019,
    ag__R8440__cites=[I67882["publication: Memristors with difusive dynamics as synaptic emulators for neuromorphic computing"], I74868["publication: Tree-dimensional crossbar arrays of self-rectifying Si/SiO2/Si memristors"], I16106["publication: Anatomy of Ag/Hafnia-based selectors with 1010 nonlinearity"], I84727["publication: Bipolar nonlinear Ni/ TiO2/Ni selector for 1S1R crossbar array applications"], I9860["publication: TiO2-based metal–insulator–metal selection device for bipolar resistive random access memory cross-point application"], I15339["publication: High-performance metal–insulator–metal tunnel diode selectors"], I6557["publication: Electrical and reliability characteristics of a scaled (∼30nm) tunnel barrier selector (W/Ta2O5/TaOx/TiO2/TiN) with excellent performance (JMAX>107A/cm2)"], I77061["publication: Varistor-type bidirectional switch (JMAX>107A/cm2 , selectivity ∼104 ) for 3D bipolar resistive memory arrays"], I18505["publication: Trilayer tunnel selectors for memristor memory cells"], I19460["publication: An 8 Mb multi-layered cross-point ReRAM macro with 443 MB/s write throughput"], I72376["publication: Termally stable integrated Se-based OTS selectors with >20MA/cm2 current drive, >3.103 half-bias nonlinearity, tunable threshold voltage and excellent endurance"], I93207["publication: Breakthrough of selector technology for cross-point 25-nm ReRAM"], I24422["publication: Excellent selector characteristics of nanoscale VO2 for high-density bipolar ReRAM applications"], I26160["publication: NbO2-based low power and cost efective 1S1R switching for high density cross point ReRAM application"], I94055["publication: Nanoscale (∼10nm) 3D vertical ReRAM and NbO2 threshold selector with TiN electrode"], I31023["publication: Highly-scalable threshold switching select device based on chalcogenide glasses for 3D nanoscaled memory arrays"], I52555["publication: Physically transient threshold switching device based on magnesium oxide for security application"], I20440["publication: High‐performance and low‐power rewritable SiO*x* 1 kbit one diode–one resistor crossbar memory array"], I13184["publication: Vacancy-modulated conductive oxide resistive RAM (VMCO-RRAM): an area-scalable switching current, self-compliant, highly nonlinear and wide on/of-window resistive switching cell"], I89283["publication: Self-selective characteristics of nanoscale VOx devices for high-density ReRAM applications"], I6909["publication: Investigations of conduction mechanisms of the self-rectifying n<sup>+</sup>Si-HfO2-Ni RRAM devices"], I3139["publication: Unipolar resistive switching with forming-free and self-rectifying efects in Cu/HfO2/n-Si devices"], I26296["publication: Nanoscale resistive memory with intrinsic diode characteristics and long endurance"]],
    
)


# 2019 
I60787["Wang, Z."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wang, Z.",
    
)


# 2019 
I67882["publication: Memristors with difusive dynamics as synaptic emulators for neuromorphic computing"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I60787["Wang, Z."],
    ag__R8434__has_title="Memristors with difusive dynamics as synaptic emulators for neuromorphic computing",
    ag__R8435__has_year=2017,
    R11809__has_memristor_stack=I76063["Pt/Ag:SiOxNy/Pt"],
    
)


# 2019 
I34722["Li, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Li, C.",
    
)


# 2019 
I74868["publication: Tree-dimensional crossbar arrays of self-rectifying Si/SiO2/Si memristors"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I34722["Li, C."],
    ag__R8434__has_title="Tree-dimensional crossbar arrays of self-rectifying Si/SiO2/Si memristors",
    ag__R8435__has_year=2017,
    R11809__has_memristor_stack=I38505["p-Si/SiO2/n-Si"],
    
)


# 2019 
I95468["Midya, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Midya, R.",
    
)


# 2019 
I16106["publication: Anatomy of Ag/Hafnia-based selectors with 1010 nonlinearity"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I95468["Midya, R."],
    ag__R8434__has_title="Anatomy of Ag/Hafnia-based selectors with 1010 nonlinearity",
    ag__R8435__has_year=2017,
    R11809__has_memristor_stack=I82668["Pd/Ag/HfO2/Ag/Pd"],
    
)


# 2019 
I79357["Huang, J.-J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Huang, J.-J.",
    
)


# 2019 
I8074["Tseng, Y.-M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Tseng, Y.-M.",
    
)


# 2019 
I47536["Hsu, C.-W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Hsu, C.-W.",
    
)


# 2019 
I85771["Hou, T.-H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Hou, T.-H.",
    
)


# 2019 
I84727["publication: Bipolar nonlinear Ni/ TiO2/Ni selector for 1S1R crossbar array applications"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I79357["Huang, J.-J."], I8074["Tseng, Y.-M."], I47536["Hsu, C.-W."], I85771["Hou, T.-H."]],
    ag__R8434__has_title="Bipolar nonlinear Ni/ TiO2/Ni selector for 1S1R crossbar array applications",
    ag__R8435__has_year=2011,
    R11809__has_memristor_stack=I75465["Ni/TiO2/Ni"],
    
)


# 2019 
I93588["Shin, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Shin, J.",
    
)


# 2019 
I9860["publication: TiO2-based metal–insulator–metal selection device for bipolar resistive random access memory cross-point application"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I93588["Shin, J."],
    ag__R8434__has_title="TiO2-based metal–insulator–metal selection device for bipolar resistive random access memory cross-point application",
    ag__R8435__has_year=2011,
    R11809__has_memristor_stack=I93192["Pt/TiO2/TiN"],
    
)


# 2019 
I85989["Govoreanu, B."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Govoreanu, B.",
    
)


# 2019 
I15339["publication: High-performance metal–insulator–metal tunnel diode selectors"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I85989["Govoreanu, B."],
    ag__R8434__has_title="High-performance metal–insulator–metal tunnel diode selectors",
    ag__R8435__has_year=2014,
    R11809__has_memristor_stack=I7316["TiN/Ta2O5/TiN"],
    
)


# 2019 
I87633["Woo, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Woo, J.",
    
)


# 2019 
I6557["publication: Electrical and reliability characteristics of a scaled (∼30nm) tunnel barrier selector (W/Ta2O5/TaOx/TiO2/TiN) with excellent performance (JMAX>107A/cm2)"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I87633["Woo, J."],
    ag__R8434__has_title="Electrical and reliability characteristics of a scaled (∼30nm) tunnel barrier selector (W/Ta2O5/TaOx/TiO2/TiN) with excellent performance (JMAX>107A/cm2)",
    ag__R8435__has_year=2014,
    R11809__has_memristor_stack=I47350["W/Ta2O5/TaOx/TiO2/TiN"],
    
)


# 2019 
I57087["Lee, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Lee, W.",
    
)


# 2019 
I77061["publication: Varistor-type bidirectional switch (JMAX>107A/cm2 , selectivity ∼104 ) for 3D bipolar resistive memory arrays"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I57087["Lee, W."],
    ag__R8434__has_title="Varistor-type bidirectional switch (JMAX>107A/cm2 , selectivity ∼104 ) for 3D bipolar resistive memory arrays",
    ag__R8435__has_year=2012,
    R11809__has_memristor_stack=I84610["Pt/TaOx/TiO2/TaOx/Pt"],
    
)


# 2019 
I17932["Choi, B. J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Choi, B. J.",
    
)


# 2019 
I18505["publication: Trilayer tunnel selectors for memristor memory cells"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I17932["Choi, B. J."],
    ag__R8434__has_title="Trilayer tunnel selectors for memristor memory cells",
    ag__R8435__has_year=2016,
    R11809__has_memristor_stack=I33761["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"],
    
)


# 2019 
I72084["Kawahara, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kawahara, A.",
    
)


# 2019 
I19460["publication: An 8 Mb multi-layered cross-point ReRAM macro with 443 MB/s write throughput"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I72084["Kawahara, A."],
    ag__R8434__has_title="An 8 Mb multi-layered cross-point ReRAM macro with 443 MB/s write throughput",
    ag__R8435__has_year=2013,
    R11809__has_memristor_stack=I63613["TaN/SiNx/TaN"],
    
)


# 2019 
I72376["publication: Termally stable integrated Se-based OTS selectors with >20MA/cm2 current drive, >3.103 half-bias nonlinearity, tunable threshold voltage and excellent endurance"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I85989["Govoreanu, B."],
    ag__R8434__has_title="Termally stable integrated Se-based OTS selectors with >20MA/cm2 current drive, >3.103 half-bias nonlinearity, tunable threshold voltage and excellent endurance",
    ag__R8435__has_year=2017,
    R11809__has_memristor_stack=I94114["TiN/GexSe1-x/TiN"],
    
)


# 2019 
I92025["Kim, S. G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kim, S. G.",
    
)


# 2019 
I93207["publication: Breakthrough of selector technology for cross-point 25-nm ReRAM"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I92025["Kim, S. G."],
    ag__R8434__has_title="Breakthrough of selector technology for cross-point 25-nm ReRAM",
    ag__R8435__has_year=2017,
    R11809__has_memristor_stack=I37565["TiN/As:SiO2/TiN"],
    
)


# 2019 
I38568["Son, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Son, M.",
    
)


# 2019 
I24422["publication: Excellent selector characteristics of nanoscale VO2 for high-density bipolar ReRAM applications"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I38568["Son, M."],
    ag__R8434__has_title="Excellent selector characteristics of nanoscale VO2 for high-density bipolar ReRAM applications",
    ag__R8435__has_year=2011,
    R11809__has_memristor_stack=I88176["Pt/VO2/Pt"],
    
)


# 2019 
I24045["Kim, W. G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kim, W. G.",
    
)


# 2019 
I26160["publication: NbO2-based low power and cost efective 1S1R switching for high density cross point ReRAM application"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I24045["Kim, W. G."],
    ag__R8434__has_title="NbO2-based low power and cost efective 1S1R switching for high density cross point ReRAM application",
    ag__R8435__has_year=2014,
    R11809__has_memristor_stack=I28585["TiN/NbO2/TiN"],
    
)


# 2019 
I39551["Cha, E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Cha, E.",
    
)


# 2019 
I94055["publication: Nanoscale (∼10nm) 3D vertical ReRAM and NbO2 threshold selector with TiN electrode"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I39551["Cha, E."],
    ag__R8434__has_title="Nanoscale (∼10nm) 3D vertical ReRAM and NbO2 threshold selector with TiN electrode",
    ag__R8435__has_year=2013,
    R11809__has_memristor_stack=I16241["TiN/NbO2/W"],
    
)


# 2019 
I36185["Lee, M.-J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Lee, M.-J.",
    
)


# 2019 
I31023["publication: Highly-scalable threshold switching select device based on chalcogenide glasses for 3D nanoscaled memory arrays"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I36185["Lee, M.-J."],
    ag__R8434__has_title="Highly-scalable threshold switching select device based on chalcogenide glasses for 3D nanoscaled memory arrays",
    ag__R8435__has_year=2012,
    R11809__has_memristor_stack=I12074["TiN/AsTeGeSiN/TiN"],
    
)


# 2019 
I63537["Sun, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Sun, J.",
    
)


# 2019 
I52555["publication: Physically transient threshold switching device based on magnesium oxide for security application"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I63537["Sun, J."],
    ag__R8434__has_title="Physically transient threshold switching device based on magnesium oxide for security application",
    ag__R8435__has_year=2018,
    R11809__has_memristor_stack=I30366["W/Ag/MgO/Ag/W"],
    
)


# 2019 
I27376["Wang, G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wang, G.",
    
)


# 2019 
I20440["publication: High‐performance and low‐power rewritable SiO*x* 1 kbit one diode–one resistor crossbar memory array"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I27376["Wang, G."],
    ag__R8434__has_title="High‐performance and low‐power rewritable SiO*x* 1 kbit one diode–one resistor crossbar memory array",
    ag__R8435__has_year=2013,
    
)


# 2019 
I13184["publication: Vacancy-modulated conductive oxide resistive RAM (VMCO-RRAM): an area-scalable switching current, self-compliant, highly nonlinear and wide on/of-window resistive switching cell"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I85989["Govoreanu, B."],
    ag__R8434__has_title="Vacancy-modulated conductive oxide resistive RAM (VMCO-RRAM): an area-scalable switching current, self-compliant, highly nonlinear and wide on/of-window resistive switching cell",
    ag__R8435__has_year=2013,
    R11809__has_memristor_stack=I79359["TiN/Al2O3/TiO2/TiN"],
    
)


# 2019 
I1679["Song, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Song, M.",
    
)


# 2019 
I89283["publication: Self-selective characteristics of nanoscale VOx devices for high-density ReRAM applications"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I1679["Song, M."],
    ag__R8434__has_title="Self-selective characteristics of nanoscale VOx devices for high-density ReRAM applications",
    ag__R8435__has_year=2012,
    R11809__has_memristor_stack=I51636["W/VOx/Pt"],
    
)


# 2019 
I72952["Lu, D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Lu, D.",
    
)


# 2019 
I6909["publication: Investigations of conduction mechanisms of the self-rectifying n<sup>+</sup>Si-HfO2-Ni RRAM devices"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I72952["Lu, D."],
    ag__R8434__has_title="Investigations of conduction mechanisms of the self-rectifying n<sup>+</sup>Si-HfO2-Ni RRAM devices",
    ag__R8435__has_year=2014,
    R11809__has_memristor_stack=I91063["Ni/HfO2/n-Si"],
    
)


# 2019 
I53460["Wang, M. J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wang, M. J.",
    
)


# 2019 
I68385["Gao, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Gao, S.",
    
)


# 2019 
I44786["Zeng, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Zeng, F.",
    
)


# 2019 
I6037["Song, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Song, C.",
    
)


# 2019 
I31376["Pan, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Pan, F.",
    
)


# 2019 
I3139["publication: Unipolar resistive switching with forming-free and self-rectifying efects in Cu/HfO2/n-Si devices"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I53460["Wang, M. J."], I68385["Gao, S."], I44786["Zeng, F."], I6037["Song, C."], I31376["Pan, F."]],
    ag__R8434__has_title="Unipolar resistive switching with forming-free and self-rectifying efects in Cu/HfO2/n-Si devices",
    ag__R8435__has_year=2016,
    R11809__has_memristor_stack=I96093["Cu/HfO2/n-Si"],
    
)


# 2019 
I31567["Kim, K.-H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kim, K.-H.",
    
)


# 2019 
I75821["Jo, S. H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Jo, S. H.",
    
)


# 2019 
I96458["Gaba, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Gaba, S.",
    
)


# 2019 
I18688["Lu, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Lu, W.",
    
)


# 2019 
I26296["publication: Nanoscale resistive memory with intrinsic diode characteristics and long endurance"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I31567["Kim, K.-H."], I75821["Jo, S. H."], I96458["Gaba, S."], I18688["Lu, W."]],
    ag__R8434__has_title="Nanoscale resistive memory with intrinsic diode characteristics and long endurance",
    ag__R8435__has_year=2010,
    R11809__has_memristor_stack=I31934["Ag/a-Si/p-poly-Si"],
    
)


# 2019 
I75465["Ni/TiO2/Ni"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I75465["Ni/TiO2/Ni"].set_relation(R48517["has stack component"], omt.I6122["Ni"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I75465["Ni/TiO2/Ni"].set_relation(R48517["has stack component"], omt.I6122["Ni"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I75465["Ni/TiO2/Ni"].set_relation(R48517["has stack component"], omt.I6119["TiO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019 



# 2019 



# 2019 
I93192["Pt/TiO2/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I93192["Pt/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6109["Pt"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I93192["Pt/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6119["TiO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I93192["Pt/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019 



# 2019 



# 2019 
I7316["TiN/Ta2O5/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I7316["TiN/Ta2O5/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I7316["TiN/Ta2O5/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I7316["TiN/Ta2O5/TiN"].set_relation(R48517["has stack component"], omt.I6123["Ta2O5"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019 



# 2019 
I47350["W/Ta2O5/TaOx/TiO2/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I47350["W/Ta2O5/TaOx/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6121["W"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I47350["W/Ta2O5/TaOx/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6123["Ta2O5"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I47350["W/Ta2O5/TaOx/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I47350["W/Ta2O5/TaOx/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6119["TiO2"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I47350["W/Ta2O5/TaOx/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(4), is_at_outer_position(True), ])


# 2019 



# 2019 



# 2019 
I84610["Pt/TaOx/TiO2/TaOx/Pt"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I84610["Pt/TaOx/TiO2/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I6109["Pt"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I84610["Pt/TaOx/TiO2/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I6109["Pt"], qualifiers=[has_position(4), is_at_outer_position(True), ])
I84610["Pt/TaOx/TiO2/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I84610["Pt/TaOx/TiO2/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I84610["Pt/TaOx/TiO2/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I6119["TiO2"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019 
I33761["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I33761["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"].set_relation(R48517["has stack component"], omt.I6109["Pt"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I33761["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"].set_relation(R48517["has stack component"], omt.I6109["Pt"], qualifiers=[has_position(4), is_at_outer_position(True), ])
I33761["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"].set_relation(R48517["has stack component"], omt.I6124["TaN1+x"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I33761["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"].set_relation(R48517["has stack component"], omt.I6124["TaN1+x"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I33761["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"].set_relation(R48517["has stack component"], omt.I6123["Ta2O5"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019 



# 2019 
I63613["TaN/SiNx/TaN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I63613["TaN/SiNx/TaN"].set_relation(R48517["has stack component"], omt.I6125["TaN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I63613["TaN/SiNx/TaN"].set_relation(R48517["has stack component"], omt.I6125["TaN"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I63613["TaN/SiNx/TaN"].set_relation(R48517["has stack component"], omt.I6126["SiNx"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019 



# 2019 



# 2019 
I94114["TiN/GexSe1-x/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I94114["TiN/GexSe1-x/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I94114["TiN/GexSe1-x/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I94114["TiN/GexSe1-x/TiN"].set_relation(R48517["has stack component"], omt.I6130["GexSe1-x"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019 
omt.I6130["GexSe1-x"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019 
I37565["TiN/As:SiO2/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I37565["TiN/As:SiO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I37565["TiN/As:SiO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I37565["TiN/As:SiO2/TiN"].set_relation(R48517["has stack component"], omt.I6131["As:SiO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019 
omt.I6131["As:SiO2"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019 
I88176["Pt/VO2/Pt"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I88176["Pt/VO2/Pt"].set_relation(R48517["has stack component"], omt.I6109["Pt"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I88176["Pt/VO2/Pt"].set_relation(R48517["has stack component"], omt.I6109["Pt"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I88176["Pt/VO2/Pt"].set_relation(R48517["has stack component"], omt.I6132["VO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019 



# 2019 
I28585["TiN/NbO2/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I28585["TiN/NbO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I28585["TiN/NbO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I28585["TiN/NbO2/TiN"].set_relation(R48517["has stack component"], omt.I6133["NbO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019 



# 2019 
I16241["TiN/NbO2/W"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I16241["TiN/NbO2/W"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I16241["TiN/NbO2/W"].set_relation(R48517["has stack component"], omt.I6133["NbO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I16241["TiN/NbO2/W"].set_relation(R48517["has stack component"], omt.I6121["W"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019 
I12074["TiN/AsTeGeSiN/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I12074["TiN/AsTeGeSiN/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I12074["TiN/AsTeGeSiN/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I12074["TiN/AsTeGeSiN/TiN"].set_relation(R48517["has stack component"], omt.I6149["AsTeGeSiN"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019 



# 2019 
I30366["W/Ag/MgO/Ag/W"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I30366["W/Ag/MgO/Ag/W"].set_relation(R48517["has stack component"], omt.I6121["W"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I30366["W/Ag/MgO/Ag/W"].set_relation(R48517["has stack component"], omt.I6121["W"], qualifiers=[has_position(4), is_at_outer_position(True), ])
I30366["W/Ag/MgO/Ag/W"].set_relation(R48517["has stack component"], omt.I6134["Ag"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I30366["W/Ag/MgO/Ag/W"].set_relation(R48517["has stack component"], omt.I6134["Ag"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I30366["W/Ag/MgO/Ag/W"].set_relation(R48517["has stack component"], omt.I6135["MgO"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019 



# 2019 



# 2019 
I76063["Pt/Ag:SiOxNy/Pt"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I76063["Pt/Ag:SiOxNy/Pt"].set_relation(R48517["has stack component"], omt.I6109["Pt"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I76063["Pt/Ag:SiOxNy/Pt"].set_relation(R48517["has stack component"], omt.I6109["Pt"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I76063["Pt/Ag:SiOxNy/Pt"].set_relation(R48517["has stack component"], omt.I6150["Ag:SiOxNy"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019 
omt.I6150["Ag:SiOxNy"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019 
I82668["Pd/Ag/HfO2/Ag/Pd"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I82668["Pd/Ag/HfO2/Ag/Pd"].set_relation(R48517["has stack component"], omt.I6136["Pd"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I82668["Pd/Ag/HfO2/Ag/Pd"].set_relation(R48517["has stack component"], omt.I6136["Pd"], qualifiers=[has_position(4), is_at_outer_position(True), ])
I82668["Pd/Ag/HfO2/Ag/Pd"].set_relation(R48517["has stack component"], omt.I6134["Ag"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I82668["Pd/Ag/HfO2/Ag/Pd"].set_relation(R48517["has stack component"], omt.I6134["Ag"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I82668["Pd/Ag/HfO2/Ag/Pd"].set_relation(R48517["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019 



# 2019 



# 2019 
I79359["TiN/Al2O3/TiO2/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I79359["TiN/Al2O3/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I79359["TiN/Al2O3/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I79359["TiN/Al2O3/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6100["Al2O3"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I79359["TiN/Al2O3/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6119["TiO2"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019 



# 2019 
I51636["W/VOx/Pt"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I51636["W/VOx/Pt"].set_relation(R48517["has stack component"], omt.I6121["W"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I51636["W/VOx/Pt"].set_relation(R48517["has stack component"], omt.I6140["VOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I51636["W/VOx/Pt"].set_relation(R48517["has stack component"], omt.I6109["Pt"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019 



# 2019 
I38505["p-Si/SiO2/n-Si"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I38505["p-Si/SiO2/n-Si"].set_relation(R48517["has stack component"], omt.I6141["p-Si"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I38505["p-Si/SiO2/n-Si"].set_relation(R48517["has stack component"], omt.I6111["SiO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I38505["p-Si/SiO2/n-Si"].set_relation(R48517["has stack component"], omt.I6142["n-Si"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019 
omt.I6141["p-Si"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019 



# 2019 
omt.I6142["n-Si"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019 
I91063["Ni/HfO2/n-Si"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I91063["Ni/HfO2/n-Si"].set_relation(R48517["has stack component"], omt.I6122["Ni"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I91063["Ni/HfO2/n-Si"].set_relation(R48517["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I91063["Ni/HfO2/n-Si"].set_relation(R48517["has stack component"], omt.I6142["n-Si"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019 
I96093["Cu/HfO2/n-Si"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I96093["Cu/HfO2/n-Si"].set_relation(R48517["has stack component"], omt.I6101["Cu"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I96093["Cu/HfO2/n-Si"].set_relation(R48517["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I96093["Cu/HfO2/n-Si"].set_relation(R48517["has stack component"], omt.I6142["n-Si"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019 



# 2019 
I31934["Ag/a-Si/p-poly-Si"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I31934["Ag/a-Si/p-poly-Si"].set_relation(R48517["has stack component"], omt.I6134["Ag"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I31934["Ag/a-Si/p-poly-Si"].set_relation(R48517["has stack component"], omt.I6143["a-Si"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I31934["Ag/a-Si/p-poly-Si"].set_relation(R48517["has stack component"], omt.I6144["p-poly-Si"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019 
omt.I6143["a-Si"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019 
omt.I6144["p-poly-Si"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2024 
I90518["publication: Hardware implementation of memristorbased artificial neural networks"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=["Fernando Aguirre", "Abu Sebastian"],
    ag__R8434__has_title="Hardware implementation of memristorbased artificial neural networks",
    ag__R8435__has_year=2024,
    ag__R8440__cites=[I46274["publication: Fully hardware-implemented memristor convolutional neural network"], I35553["publication: A fully integrated reprogrammable memristor-CMOS system for efficient multiply-accumulate operations"], I66013["publication: A compute-in-memory chip based on resistive random-access memory"], I1871["publication: A 4M synapses integrated analog ReRAM based 66.5 TOPS/W neural-network processor with cell current controlled writing and flexible network architecture"], I66252["publication: A 462GOPs/J RRAM-based nonvolatile intelligent processor for energy harvesting IoE system featuring nonvolatile logics and processing-in-memory"], I17956["publication: A fully hardware-based memristive multilayer neural network"], I10396["publication: CMOS-integrated nanoscale memristive crossbars for CNN and optimization acceleration"], I3375["publication: Redundancy and analog slicing for precise inmemory machine learning - Part I: Programming techniques"], I91390["publication: Redundancy and analog slicing for precise inmemory machine learning - Part II: Applications and benchmark"], I45686["publication: Fully memristive neural networks for pattern classification with unsupervised learning"], I19647["publication: In-memory and error-immune differential RRAM implementation of binarized deep neural networks"], I3560["publication: CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors"], I72007["publication: Digital biologically plausible implementation of binarized neural networks with differential hafnium oxide resistive memory arrays"], I87369["publication: A 43pJ/Cycle Non-Volatile Microcontroller with 4.7μs Shutdown/Wake-up Integrating 2.3-bit/Cell Resistive RAM and Resilience Techniques"]],
    
)


# 2024 
I11228["Yao, P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Yao, P.",
    
)


# 2024 
I46274["publication: Fully hardware-implemented memristor convolutional neural network"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I11228["Yao, P."],
    ag__R8434__has_title="Fully hardware-implemented memristor convolutional neural network",
    ag__R8435__has_year=2020,
    R11809__has_memristor_stack=I69977["TiN/TaOx/HfOx/TiN"],
    
)


# 2024 
I28662["Cai, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Cai, F.",
    
)


# 2024 
I35553["publication: A fully integrated reprogrammable memristor-CMOS system for efficient multiply-accumulate operations"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I28662["Cai, F."],
    ag__R8434__has_title="A fully integrated reprogrammable memristor-CMOS system for efficient multiply-accumulate operations",
    ag__R8435__has_year=2019,
    R11809__has_memristor_stack=I34943["Au/Pd/WOx/Au"],
    
)


# 2024 
I48163["Wan, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wan, W.",
    
)


# 2024 
I66013["publication: A compute-in-memory chip based on resistive random-access memory"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I48163["Wan, W."],
    ag__R8434__has_title="A compute-in-memory chip based on resistive random-access memory",
    ag__R8435__has_year=2022,
    R11809__has_memristor_stack=I39529["TiN/HfO2/TaOx/TiN"],
    
)


# 2024 
I79007["Mochida, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Mochida, R.",
    
)


# 2024 
I1871["publication: A 4M synapses integrated analog ReRAM based 66.5 TOPS/W neural-network processor with cell current controlled writing and flexible network architecture"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I79007["Mochida, R."],
    ag__R8434__has_title="A 4M synapses integrated analog ReRAM based 66.5 TOPS/W neural-network processor with cell current controlled writing and flexible network architecture",
    ag__R8435__has_year=2018,
    R11809__has_memristor_stack=I75653["W/Ta2O5/TaOx/W"],
    
)


# 2024 
I8544["Su, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Su, F.",
    
)


# 2024 
I66252["publication: A 462GOPs/J RRAM-based nonvolatile intelligent processor for energy harvesting IoE system featuring nonvolatile logics and processing-in-memory"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I8544["Su, F."],
    ag__R8434__has_title="A 462GOPs/J RRAM-based nonvolatile intelligent processor for energy harvesting IoE system featuring nonvolatile logics and processing-in-memory",
    ag__R8435__has_year=2017,
    R11809__has_memristor_stack=I73280["AlCu/TiN/Ti/HfO2/TiN"],
    
)


# 2024 
I16648["Kiani, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kiani, F.",
    
)


# 2024 
I91231["Yin, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Yin, J.",
    
)


# 2024 
I5202["Joshua Yang, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Joshua Yang, J.",
    
)


# 2024 
I66876["Xia, Q."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Xia, Q.",
    
)


# 2024 
I17956["publication: A fully hardware-based memristive multilayer neural network"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I16648["Kiani, F."], I91231["Yin, J."], I60787["Wang, Z."], I5202["Joshua Yang, J."], I66876["Xia, Q."]],
    ag__R8434__has_title="A fully hardware-based memristive multilayer neural network",
    ag__R8435__has_year=2021,
    R11809__has_memristor_stack=I56497["Pt/Ta/Ta2O5/Pt/Ti"],
    
)


# 2024 
I10396["publication: CMOS-integrated nanoscale memristive crossbars for CNN and optimization acceleration"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I34722["Li, C."],
    ag__R8434__has_title="CMOS-integrated nanoscale memristive crossbars for CNN and optimization acceleration",
    ag__R8435__has_year=2020,
    R11809__has_memristor_stack=I55117["Ta/TaOx/Pt"],
    
)


# 2024 
I79049["Pedretti, G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Pedretti, G.",
    
)


# 2024 
I3375["publication: Redundancy and analog slicing for precise inmemory machine learning - Part I: Programming techniques"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I79049["Pedretti, G."],
    ag__R8434__has_title="Redundancy and analog slicing for precise inmemory machine learning - Part I: Programming techniques",
    ag__R8435__has_year=2021,
    
)


# 2024 
I91390["publication: Redundancy and analog slicing for precise inmemory machine learning - Part II: Applications and benchmark"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I79049["Pedretti, G."],
    ag__R8434__has_title="Redundancy and analog slicing for precise inmemory machine learning - Part II: Applications and benchmark",
    ag__R8435__has_year=2021,
    
)


# 2024 
I45686["publication: Fully memristive neural networks for pattern classification with unsupervised learning"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I60787["Wang, Z."],
    ag__R8434__has_title="Fully memristive neural networks for pattern classification with unsupervised learning",
    ag__R8435__has_year=2018,
    R11809__has_memristor_stack=[I8432["Pt/SiOxAg/Pt/Ti"], I49144["Ta/Pd/HfO2/Pt/Ti"]],
    
)


# 2024 
I87710["Bocquet, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Bocquet, M.",
    
)


# 2024 
I19647["publication: In-memory and error-immune differential RRAM implementation of binarized deep neural networks"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I87710["Bocquet, M."],
    ag__R8434__has_title="In-memory and error-immune differential RRAM implementation of binarized deep neural networks",
    ag__R8435__has_year=2018,
    R11809__has_memristor_stack=I13384["TiN/HfO2/Ti/TiN"],
    
)


# 2024 
I79796["Chen, W. H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Chen, W. H.",
    
)


# 2024 
I3560["publication: CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I79796["Chen, W. H."],
    ag__R8434__has_title="CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors",
    ag__R8435__has_year=2019,
    R11809__has_memristor_stack=I81948["W/TiN/TiON"],
    
)


# 2024 
I78447["Hirtzlin, T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Hirtzlin, T.",
    
)


# 2024 
I72007["publication: Digital biologically plausible implementation of binarized neural networks with differential hafnium oxide resistive memory arrays"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I78447["Hirtzlin, T."],
    ag__R8434__has_title="Digital biologically plausible implementation of binarized neural networks with differential hafnium oxide resistive memory arrays",
    ag__R8435__has_year=2020,
    R11809__has_memristor_stack=I13384["TiN/HfO2/Ti/TiN"],
    
)


# 2024 
I36884["Wu, T. F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wu, T. F.",
    
)


# 2024 
I87369["publication: A 43pJ/Cycle Non-Volatile Microcontroller with 4.7μs Shutdown/Wake-up Integrating 2.3-bit/Cell Resistive RAM and Resilience Techniques"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I36884["Wu, T. F."],
    ag__R8434__has_title="A 43pJ/Cycle Non-Volatile Microcontroller with 4.7μs Shutdown/Wake-up Integrating 2.3-bit/Cell Resistive RAM and Resilience Techniques",
    ag__R8435__has_year=2019,
    R11809__has_memristor_stack=I13384["TiN/HfO2/Ti/TiN"],
    
)


# 2024 
I34943["Au/Pd/WOx/Au"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I34943["Au/Pd/WOx/Au"].set_relation(R48517["has stack component"], omt.I6145["Au"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I34943["Au/Pd/WOx/Au"].set_relation(R48517["has stack component"], omt.I6145["Au"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I34943["Au/Pd/WOx/Au"].set_relation(R48517["has stack component"], omt.I6136["Pd"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I34943["Au/Pd/WOx/Au"].set_relation(R48517["has stack component"], omt.I6146["WOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2024 



# 2024 



# 2024 
I69977["TiN/TaOx/HfOx/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I69977["TiN/TaOx/HfOx/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I69977["TiN/TaOx/HfOx/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I69977["TiN/TaOx/HfOx/TiN"].set_relation(R48517["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I69977["TiN/TaOx/HfOx/TiN"].set_relation(R48517["has stack component"], omt.I6105["HfOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2024 



# 2024 
I56497["Pt/Ta/Ta2O5/Pt/Ti"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I56497["Pt/Ta/Ta2O5/Pt/Ti"].set_relation(R48517["has stack component"], omt.I6109["Pt"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I56497["Pt/Ta/Ta2O5/Pt/Ti"].set_relation(R48517["has stack component"], omt.I6109["Pt"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I56497["Pt/Ta/Ta2O5/Pt/Ti"].set_relation(R48517["has stack component"], omt.I6114["Ta"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I56497["Pt/Ta/Ta2O5/Pt/Ti"].set_relation(R48517["has stack component"], omt.I6123["Ta2O5"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I56497["Pt/Ta/Ta2O5/Pt/Ti"].set_relation(R48517["has stack component"], omt.I6116["Ti"], qualifiers=[has_position(4), is_at_outer_position(True), ])


# 2024 



# 2024 



# 2024 
I55117["Ta/TaOx/Pt"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I55117["Ta/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I6114["Ta"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I55117["Ta/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I55117["Ta/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I6109["Pt"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2024 
I81948["W/TiN/TiON"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I81948["W/TiN/TiON"].set_relation(R48517["has stack component"], omt.I6121["W"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I81948["W/TiN/TiON"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I81948["W/TiN/TiON"].set_relation(R48517["has stack component"], omt.I6147["TiON"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2024 



# 2024 
I8432["Pt/SiOxAg/Pt/Ti"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I8432["Pt/SiOxAg/Pt/Ti"].set_relation(R48517["has stack component"], omt.I6109["Pt"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I8432["Pt/SiOxAg/Pt/Ti"].set_relation(R48517["has stack component"], omt.I6109["Pt"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I8432["Pt/SiOxAg/Pt/Ti"].set_relation(R48517["has stack component"], omt.I6151["SiOxAg"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I8432["Pt/SiOxAg/Pt/Ti"].set_relation(R48517["has stack component"], omt.I6116["Ti"], qualifiers=[has_position(3), is_at_outer_position(True), ])


# 2024 
omt.I6151["SiOxAg"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2024 
I49144["Ta/Pd/HfO2/Pt/Ti"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I49144["Ta/Pd/HfO2/Pt/Ti"].set_relation(R48517["has stack component"], omt.I6114["Ta"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I49144["Ta/Pd/HfO2/Pt/Ti"].set_relation(R48517["has stack component"], omt.I6136["Pd"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I49144["Ta/Pd/HfO2/Pt/Ti"].set_relation(R48517["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I49144["Ta/Pd/HfO2/Pt/Ti"].set_relation(R48517["has stack component"], omt.I6109["Pt"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I49144["Ta/Pd/HfO2/Pt/Ti"].set_relation(R48517["has stack component"], omt.I6116["Ti"], qualifiers=[has_position(4), is_at_outer_position(True), ])


# 2024 
I13384["TiN/HfO2/Ti/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I13384["TiN/HfO2/Ti/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I13384["TiN/HfO2/Ti/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I13384["TiN/HfO2/Ti/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I13384["TiN/HfO2/Ti/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I13384["TiN/HfO2/Ti/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I13384["TiN/HfO2/Ti/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I13384["TiN/HfO2/Ti/TiN"].set_relation(R48517["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I13384["TiN/HfO2/Ti/TiN"].set_relation(R48517["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I13384["TiN/HfO2/Ti/TiN"].set_relation(R48517["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I13384["TiN/HfO2/Ti/TiN"].set_relation(R48517["has stack component"], omt.I6116["Ti"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I13384["TiN/HfO2/Ti/TiN"].set_relation(R48517["has stack component"], omt.I6116["Ti"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I13384["TiN/HfO2/Ti/TiN"].set_relation(R48517["has stack component"], omt.I6116["Ti"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2024 
I75653["W/Ta2O5/TaOx/W"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I75653["W/Ta2O5/TaOx/W"].set_relation(R48517["has stack component"], omt.I6121["W"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I75653["W/Ta2O5/TaOx/W"].set_relation(R48517["has stack component"], omt.I6121["W"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I75653["W/Ta2O5/TaOx/W"].set_relation(R48517["has stack component"], omt.I6123["Ta2O5"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I75653["W/Ta2O5/TaOx/W"].set_relation(R48517["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2024 
I73280["AlCu/TiN/Ti/HfO2/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I73280["AlCu/TiN/Ti/HfO2/TiN"].set_relation(R48517["has stack component"], omt.I6148["AlCu"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I73280["AlCu/TiN/Ti/HfO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I73280["AlCu/TiN/Ti/HfO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(4), is_at_outer_position(True), ])
I73280["AlCu/TiN/Ti/HfO2/TiN"].set_relation(R48517["has stack component"], omt.I6116["Ti"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I73280["AlCu/TiN/Ti/HfO2/TiN"].set_relation(R48517["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(3), is_at_outer_position(False), ])


# 2024 



# 2024 
I39529["TiN/HfO2/TaOx/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I39529["TiN/HfO2/TaOx/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I39529["TiN/HfO2/TaOx/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I39529["TiN/HfO2/TaOx/TiN"].set_relation(R48517["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I39529["TiN/HfO2/TaOx/TiN"].set_relation(R48517["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])




p.end_mod()