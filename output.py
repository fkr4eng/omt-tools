import pyirk as p
import sympy as sp

from ipydex import IPS, activate_ips_on_exception  # noqa


omt = p.irkloader.load_mod_from_uri(r"irk:/omt/0.1/omt", prefix="omt")

ag = p.irkloader.load_mod_from_uri(r"irk:/ocse/0.2/agents", prefix="ag")


__URI__ = "irk:/omt/mem"

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
R61354 = p.create_relation(R1__has_label="has citation id")
R68407 = p.create_relation(R1__has_label="has internal reference")
I18540 = p.create_item(R1__has_label="publication: Recommended Methods to Study Resistive Switching Devices")
I60787 = p.create_item(R1__has_label="H. Y. Lee")
I67882 = p.create_item(R1__has_label="Y. S. Chen")
I34722 = p.create_item(R1__has_label="P. S. Chen")
I74868 = p.create_item(R1__has_label="P. Y. Gu")
I95468 = p.create_item(R1__has_label="Y. Y. Hsu")
I16106 = p.create_item(R1__has_label="S. M. Wang")
I79357 = p.create_item(R1__has_label="W. H. Liu")
I8074 = p.create_item(R1__has_label="C. H. Tsai")
I47536 = p.create_item(R1__has_label="S. S. Sheu")
I85771 = p.create_item(R1__has_label="P. C. Chiang")
I84727 = p.create_item(R1__has_label="W. P. Lin")
I93588 = p.create_item(R1__has_label="C. H. Lin")
I9860 = p.create_item(R1__has_label="W. S. Chen")
I85989 = p.create_item(R1__has_label="F. T. Chen")
I15339 = p.create_item(R1__has_label="C. H. Lien")
I87633 = p.create_item(R1__has_label="M. J. Tsai")
I6557 = p.create_item(R1__has_label="publication: IEEE Int. Electron Devices Meet.")
I57087 = p.create_item(R1__has_label="B. Govoreanu")
I77061 = p.create_item(R1__has_label="G. S. Kar")
I17932 = p.create_item(R1__has_label="Y-Y. Chen")
I18505 = p.create_item(R1__has_label="V. Paraschiv")
I72084 = p.create_item(R1__has_label="S. Kubicek")
I19460 = p.create_item(R1__has_label="A. Fantini")
I72376 = p.create_item(R1__has_label="I. P. Radu")
I92025 = p.create_item(R1__has_label="L. Goux")
I93207 = p.create_item(R1__has_label="S. Clima")
I38568 = p.create_item(R1__has_label="R. Degraeve")
I24422 = p.create_item(R1__has_label="N. Jossart")
I24045 = p.create_item(R1__has_label="O. Richard")
I26160 = p.create_item(R1__has_label="T. Vandeweyer")
I39551 = p.create_item(R1__has_label="K. Seo")
I94055 = p.create_item(R1__has_label="P. Hendrickx")
I36185 = p.create_item(R1__has_label="G. Pourtois")
I31023 = p.create_item(R1__has_label="H. Bender")
I63537 = p.create_item(R1__has_label="L. Altimime")
I52555 = p.create_item(R1__has_label="D. J. Wouters")
I27376 = p.create_item(R1__has_label="J. A. Kittl")
I20440 = p.create_item(R1__has_label="M. Jurczak")
I13184 = p.create_item(R1__has_label="publication: No title given 25631219101")
I1679 = p.create_item(R1__has_label="J. J. Yang")
I89283 = p.create_item(R1__has_label="M.-X. Zhang")
I72952 = p.create_item(R1__has_label="J. P. Strachan")
I6909 = p.create_item(R1__has_label="F. Miao")
I53460 = p.create_item(R1__has_label="M. D. Pickett")
I68385 = p.create_item(R1__has_label="R. D. Kelley")
I44786 = p.create_item(R1__has_label="G. Medeiros-Ribeiro")
I6037 = p.create_item(R1__has_label="R. S. Williams")
I31376 = p.create_item(R1__has_label="publication: Appl. Phys. Lett.")
I3139 = p.create_item(R1__has_label="M. J. Lee")
I31567 = p.create_item(R1__has_label="C. B. Lee")
I75821 = p.create_item(R1__has_label="D. S. Lee")
I96458 = p.create_item(R1__has_label="S. R. Lee")
I18688 = p.create_item(R1__has_label="M. Chang")
I26296 = p.create_item(R1__has_label="J. H. Hur")
I75465 = p.create_item(R1__has_label="Y. B. Kim")
I93192 = p.create_item(R1__has_label="C. J. Kim")
I7316 = p.create_item(R1__has_label="D. H. Seo")
I47350 = p.create_item(R1__has_label="S. Seo")
I84610 = p.create_item(R1__has_label="U. I. Chung")
I33761 = p.create_item(R1__has_label="I. K. Yoo")
I63613 = p.create_item(R1__has_label="K. Kim")
I94114 = p.create_item(R1__has_label="publication: Nat. Mater.")
I37565 = p.create_item(R1__has_label="I G. Baek")
I88176 = p.create_item(R1__has_label="M. S. Lee")
I28585 = p.create_item(R1__has_label="D. S. Suh")
I16241 = p.create_item(R1__has_label="J. C. Park")
I12074 = p.create_item(R1__has_label="S. O. Park")
I30366 = p.create_item(R1__has_label="H. S. Kim")
I76063 = p.create_item(R1__has_label="J. T. Moon")
I82668 = p.create_item(R1__has_label="publication: presented at *IEEE Int. Electron Device Meet.*")
I79359 = p.create_item(R1__has_label="C. H. Cheng")
I51636 = p.create_item(R1__has_label="A. Chin")
I38505 = p.create_item(R1__has_label="F. S. Yeh")
I91063 = p.create_item(R1__has_label="publication: Symp. VLSI Technol.")
I96093 = p.create_item(R1__has_label="Z. Wei")
I31934 = p.create_item(R1__has_label="Y. Kanzawa")
I90518 = p.create_item(R1__has_label="K. Arita")
I11228 = p.create_item(R1__has_label="Y. Katoh")
I46274 = p.create_item(R1__has_label="K. Kawai")
I28662 = p.create_item(R1__has_label="S. Muraoka")
I35553 = p.create_item(R1__has_label="S. Mitani")
I48163 = p.create_item(R1__has_label="S. Fujii")
I66013 = p.create_item(R1__has_label="K. Katayama")
I79007 = p.create_item(R1__has_label="M. Iijima")
I1871 = p.create_item(R1__has_label="T. Mikawa")
I8544 = p.create_item(R1__has_label="T. Ninomiya")
I66252 = p.create_item(R1__has_label="R. Miyanaga")
I16648 = p.create_item(R1__has_label="Y. Kawashima")
I91231 = p.create_item(R1__has_label="K. Tsuji")
I5202 = p.create_item(R1__has_label="A. Himeno")
I66876 = p.create_item(R1__has_label="T. Okada")
I17956 = p.create_item(R1__has_label="R. Azuma")
I10396 = p.create_item(R1__has_label="K. Shimakawa")
I79049 = p.create_item(R1__has_label="H. Sugaya")
I3375 = p.create_item(R1__has_label="T. Takagi")
I91390 = p.create_item(R1__has_label="R. Yasuhara")
I45686 = p.create_item(R1__has_label="K. Horiba")
I87710 = p.create_item(R1__has_label="H. Kumigashira")
I19647 = p.create_item(R1__has_label="M. Oshima")
I79796 = p.create_item(R1__has_label="publication: presented at *IEEE IEDM*")
I3560 = p.create_item(R1__has_label="L. G. Wang")
I78447 = p.create_item(R1__has_label="X. Qian")
I72007 = p.create_item(R1__has_label="Y. Q. Cao")
I36884 = p.create_item(R1__has_label="Z. Y. Cao")
I87369 = p.create_item(R1__has_label="G. Y. Fang")
I34943 = p.create_item(R1__has_label="A. D. Li")
I69977 = p.create_item(R1__has_label="D. Wu")
I56497 = p.create_item(R1__has_label="publication: No title given 41246013015")
I55117 = p.create_item(R1__has_label="H.-S. P. Wong")
I81948 = p.create_item(R1__has_label="S. Yu")
I8432 = p.create_item(R1__has_label="Y. Wu")
I49144 = p.create_item(R1__has_label="B. Lee")
I13384 = p.create_item(R1__has_label="publication: No title given 28138552030")
I75653 = p.create_item(R1__has_label="M. C. Wu")
I73280 = p.create_item(R1__has_label="Y. W. Lin")
I31254 = p.create_item(R1__has_label="W. Y. Jang")
I67533 = p.create_item(R1__has_label="T. Y. Tseng")
I39529 = p.create_item(R1__has_label="publication: IEEE Electron Device Lett.")
I74938 = p.create_item(R1__has_label="C. Ahn")
I85012 = p.create_item(R1__has_label="Z. Jiang")
I99712 = p.create_item(R1__has_label="C. S. Lee")
I94362 = p.create_item(R1__has_label="H. Y. Chen")
I85528 = p.create_item(R1__has_label="J. Liang")
I2855 = p.create_item(R1__has_label="L. S. Liyanage")
I46793 = p.create_item(R1__has_label="H. S. P. Wong")
I90963 = p.create_item(R1__has_label="publication: IEEE Trans. Electron Devices")
I54975 = p.create_item(R1__has_label="D. Lee")
I72751 = p.create_item(R1__has_label="G. S. Park")
I80078 = p.create_item(R1__has_label="U. Chung")
I5210 = p.create_item(R1__has_label="publication: 2011 Symp. on VLSI Technology - Digest of Technical Papers")
I32782 = p.create_item(R1__has_label="V. K. Nagareddy")
I91760 = p.create_item(R1__has_label="A. K. Ott")
I91215 = p.create_item(R1__has_label="C. Dou")
I81970 = p.create_item(R1__has_label="T. Tsvetkova")
I68229 = p.create_item(R1__has_label="M. Sandulov")
I64747 = p.create_item(R1__has_label="M. F. Craciun")
I39757 = p.create_item(R1__has_label="A. C. Ferrari")
I30227 = p.create_item(R1__has_label="C. D. Wright")
I24132 = p.create_item(R1__has_label="publication: No title given 26048021673")
I14404 = p.create_item(R1__has_label="X. Cao")
I65317 = p.create_item(R1__has_label="X. M. Li")
I25665 = p.create_item(R1__has_label="X. D. Gao")
I85099 = p.create_item(R1__has_label="W. D. Yu")
I97353 = p.create_item(R1__has_label="X. J. Liu")
I47693 = p.create_item(R1__has_label="Y. W. Zhang")
I17571 = p.create_item(R1__has_label="L. D. Chen")
I63422 = p.create_item(R1__has_label="X. H. Cheng")
I91057 = p.create_item(R1__has_label="publication: No title given 86846326096")
I86040 = p.create_item(R1__has_label="TiN/TiOx/HfOx/TiN")
I60665 = p.create_item(R1__has_label="Ti/ZrO2/Pt")
I36571 = p.create_item(R1__has_label="ZrO2")
I76227 = p.create_item(R1__has_label="TiN/Hf/HfOx/TiN")
I11040 = p.create_item(R1__has_label="Al/Ti/Al2O3/s-CNT")
I40507 = p.create_item(R1__has_label="s-CNT")
I45775 = p.create_item(R1__has_label="Pt/Ta2O5-x/TaO2-x/Pt")
I88802 = p.create_item(R1__has_label="Ta2O5-x")
I89671 = p.create_item(R1__has_label="TaO2-x")
I5377 = p.create_item(R1__has_label="Pt/TaOx/Pt")
I79564 = p.create_item(R1__has_label="Ta/TaOx/TiO2/Ti")
I67803 = p.create_item(R1__has_label="Pt/TaOx/Ta")
I37074 = p.create_item(R1__has_label="W/AlO/TaOx/ZrOx/Ru")
I34513 = p.create_item(R1__has_label="AlO")
I4484 = p.create_item(R1__has_label="ZrOx")
I93059 = p.create_item(R1__has_label="Pt/Al2O3/HfO2/Al2O3/TiN/Si")
I48946 = p.create_item(R1__has_label="TaN/TiN/Zr/HfO2/CAFM tip")
I44836 = p.create_item(R1__has_label="CAFM tip")
I99459 = p.create_item(R1__has_label="Ni/GeO/STO/TaN")
I48965 = p.create_item(R1__has_label="GeO")
I85347 = p.create_item(R1__has_label="STO")
I45993 = p.create_item(R1__has_label="Pt/Gd2O3/Pt")
I24141 = p.create_item(R1__has_label="Gd2O3")
I35428 = p.create_item(R1__has_label="publication: Memristive crossbar arrays for brain-inspired computing")
I10778 = p.create_item(R1__has_label="Wang, Z.")
I69974 = p.create_item(R1__has_label="publication: Memristors with difusive dynamics as synaptic emulators for neuromorphic computing")
I70494 = p.create_item(R1__has_label="Li, C.")
I87242 = p.create_item(R1__has_label="publication: Tree-dimensional crossbar arrays of self-rectifying Si/SiO2/Si memristors")
I93860 = p.create_item(R1__has_label="Midya, R.")
I78857 = p.create_item(R1__has_label="publication: Anatomy of Ag/Hafnia-based selectors with 1010 nonlinearity")
I94601 = p.create_item(R1__has_label="Huang, J.-J.")
I52917 = p.create_item(R1__has_label="Tseng, Y.-M.")
I86787 = p.create_item(R1__has_label="Hsu, C.-W.")
I21123 = p.create_item(R1__has_label="Hou, T.-H.")
I39708 = p.create_item(R1__has_label="publication: Bipolar nonlinear Ni/ TiO2/Ni selector for 1S1R crossbar array applications")
I93276 = p.create_item(R1__has_label="Shin, J.")
I53205 = p.create_item(R1__has_label="publication: TiO2-based metal–insulator–metal selection device for bipolar resistive random access memory cross-point application")
I87136 = p.create_item(R1__has_label="Govoreanu, B.")
I41902 = p.create_item(R1__has_label="publication: High-performance metal–insulator–metal tunnel diode selectors")
I85417 = p.create_item(R1__has_label="Woo, J.")
I97657 = p.create_item(R1__has_label="publication: Electrical and reliability characteristics of a scaled (∼30nm) tunnel barrier selector (W/Ta2O5/TaOx/TiO2/TiN) with excellent performance (JMAX>107A/cm2)")
I29872 = p.create_item(R1__has_label="Lee, W.")
I21621 = p.create_item(R1__has_label="publication: Varistor-type bidirectional switch (JMAX>107A/cm2 , selectivity ∼104 ) for 3D bipolar resistive memory arrays")
I87604 = p.create_item(R1__has_label="Choi, B. J.")
I58690 = p.create_item(R1__has_label="publication: Trilayer tunnel selectors for memristor memory cells")
I7533 = p.create_item(R1__has_label="Kawahara, A.")
I28840 = p.create_item(R1__has_label="publication: An 8 Mb multi-layered cross-point ReRAM macro with 443 MB/s write throughput")
I49189 = p.create_item(R1__has_label="publication: Termally stable integrated Se-based OTS selectors with >20MA/cm2 current drive, >3.103 half-bias nonlinearity, tunable threshold voltage and excellent endurance")
I8849 = p.create_item(R1__has_label="Kim, S. G.")
I74720 = p.create_item(R1__has_label="publication: Breakthrough of selector technology for cross-point 25-nm ReRAM")
I95219 = p.create_item(R1__has_label="Son, M.")
I45292 = p.create_item(R1__has_label="publication: Excellent selector characteristics of nanoscale VO2 for high-density bipolar ReRAM applications")
I90863 = p.create_item(R1__has_label="Kim, W. G.")
I66609 = p.create_item(R1__has_label="publication: NbO2-based low power and cost efective 1S1R switching for high density cross point ReRAM application")
I26240 = p.create_item(R1__has_label="Cha, E.")
I16712 = p.create_item(R1__has_label="publication: Nanoscale (∼10nm) 3D vertical ReRAM and NbO2 threshold selector with TiN electrode")
I26637 = p.create_item(R1__has_label="Lee, M.-J.")
I73173 = p.create_item(R1__has_label="publication: Highly-scalable threshold switching select device based on chalcogenide glasses for 3D nanoscaled memory arrays")
I77352 = p.create_item(R1__has_label="Sun, J.")
I12092 = p.create_item(R1__has_label="publication: Physically transient threshold switching device based on magnesium oxide for security application")
I95662 = p.create_item(R1__has_label="Wang, G.")
I50118 = p.create_item(R1__has_label="publication: High‐performance and low‐power rewritable SiO*x* 1 kbit one diode–one resistor crossbar memory array")
I52771 = p.create_item(R1__has_label="publication: Vacancy-modulated conductive oxide resistive RAM (VMCO-RRAM): an area-scalable switching current, self-compliant, highly nonlinear and wide on/of-window resistive switching cell")
I38213 = p.create_item(R1__has_label="Song, M.")
I9385 = p.create_item(R1__has_label="publication: Self-selective characteristics of nanoscale VOx devices for high-density ReRAM applications")
I34131 = p.create_item(R1__has_label="Lu, D.")
I47402 = p.create_item(R1__has_label="publication: Investigations of conduction mechanisms of the self-rectifying n<sup>+</sup>Si-HfO2-Ni RRAM devices")
I8777 = p.create_item(R1__has_label="Wang, M. J.")
I61519 = p.create_item(R1__has_label="Gao, S.")
I89808 = p.create_item(R1__has_label="Zeng, F.")
I73802 = p.create_item(R1__has_label="Song, C.")
I63079 = p.create_item(R1__has_label="Pan, F.")
I92934 = p.create_item(R1__has_label="publication: Unipolar resistive switching with forming-free and self-rectifying efects in Cu/HfO2/n-Si devices")
I97154 = p.create_item(R1__has_label="Kim, K.-H.")
I84376 = p.create_item(R1__has_label="Jo, S. H.")
I72298 = p.create_item(R1__has_label="Gaba, S.")
I34559 = p.create_item(R1__has_label="Lu, W.")
I83048 = p.create_item(R1__has_label="publication: Nanoscale resistive memory with intrinsic diode characteristics and long endurance")
I71732 = p.create_item(R1__has_label="Ni/TiO2/Ni")
I16765 = p.create_item(R1__has_label="Pt/TiO2/TiN")
I18578 = p.create_item(R1__has_label="TiN/Ta2O5/TiN")
I87992 = p.create_item(R1__has_label="W/Ta2O5/TaOx/TiO2/TiN")
I44440 = p.create_item(R1__has_label="Pt/TaOx/TiO2/TaOx/Pt")
I58468 = p.create_item(R1__has_label="Pt/TaN1+x/Ta2O5/TaN1+x/Pt")
I47470 = p.create_item(R1__has_label="TaN/SiNx/TaN")
I82062 = p.create_item(R1__has_label="TiN/GexSe1-x/TiN")
I58157 = p.create_item(R1__has_label="TiN/As:SiO2/TiN")
I27966 = p.create_item(R1__has_label="Pt/VO2/Pt")
I21352 = p.create_item(R1__has_label="TiN/NbO2/TiN")
I46285 = p.create_item(R1__has_label="TiN/NbO2/W")
I6912 = p.create_item(R1__has_label="TiN/AsTeGeSiN/TiN")
I26347 = p.create_item(R1__has_label="W/Ag/MgO/Ag/W")
I24977 = p.create_item(R1__has_label="Pt/Ag:SiOxNy/Pt")
I9309 = p.create_item(R1__has_label="Pd/Ag/HfO2/Ag/Pd")
I93983 = p.create_item(R1__has_label="TiN/Al2O3/TiO2/TiN")
I18158 = p.create_item(R1__has_label="W/VOx/Pt")
I63066 = p.create_item(R1__has_label="p-Si/SiO2/n-Si")
I55774 = p.create_item(R1__has_label="Ni/HfO2/n-Si")
I3236 = p.create_item(R1__has_label="Cu/HfO2/n-Si")
I95705 = p.create_item(R1__has_label="Ag/a-Si/p-poly-Si")
I78145 = p.create_item(R1__has_label="publication: Hardware implementation of memristorbased artificial neural networks")
I93419 = p.create_item(R1__has_label="Yao, P.")
I98801 = p.create_item(R1__has_label="publication: Fully hardware-implemented memristor convolutional neural network")
I11520 = p.create_item(R1__has_label="Cai, F.")
I47520 = p.create_item(R1__has_label="publication: A fully integrated reprogrammable memristor-CMOS system for efficient multiply-accumulate operations")
I59694 = p.create_item(R1__has_label="Wan, W.")
I79160 = p.create_item(R1__has_label="publication: A compute-in-memory chip based on resistive random-access memory")
I56829 = p.create_item(R1__has_label="Mochida, R.")
I10094 = p.create_item(R1__has_label="publication: A 4M synapses integrated analog ReRAM based 66.5 TOPS/W neural-network processor with cell current controlled writing and flexible network architecture")
I33159 = p.create_item(R1__has_label="Su, F.")
I42033 = p.create_item(R1__has_label="publication: A 462GOPs/J RRAM-based nonvolatile intelligent processor for energy harvesting IoE system featuring nonvolatile logics and processing-in-memory")
I92000 = p.create_item(R1__has_label="Kiani, F.")
I7940 = p.create_item(R1__has_label="Yin, J.")
I69530 = p.create_item(R1__has_label="Joshua Yang, J.")
I68259 = p.create_item(R1__has_label="Xia, Q.")
I29098 = p.create_item(R1__has_label="publication: A fully hardware-based memristive multilayer neural network")
I82346 = p.create_item(R1__has_label="publication: CMOS-integrated nanoscale memristive crossbars for CNN and optimization acceleration")
I90071 = p.create_item(R1__has_label="Pedretti, G.")
I88962 = p.create_item(R1__has_label="publication: Redundancy and analog slicing for precise inmemory machine learning - Part I: Programming techniques")
I12398 = p.create_item(R1__has_label="publication: Redundancy and analog slicing for precise inmemory machine learning - Part II: Applications and benchmark")
I33364 = p.create_item(R1__has_label="publication: Fully memristive neural networks for pattern classification with unsupervised learning")
I8173 = p.create_item(R1__has_label="Bocquet, M.")
I98878 = p.create_item(R1__has_label="publication: In-memory and error-immune differential RRAM implementation of binarized deep neural networks")
I76458 = p.create_item(R1__has_label="Chen, W. H.")
I23249 = p.create_item(R1__has_label="publication: CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors")
I38620 = p.create_item(R1__has_label="Hirtzlin, T.")
I76087 = p.create_item(R1__has_label="publication: Digital biologically plausible implementation of binarized neural networks with differential hafnium oxide resistive memory arrays")
I48237 = p.create_item(R1__has_label="Wu, T. F.")
I61398 = p.create_item(R1__has_label="publication: A 43pJ/Cycle Non-Volatile Microcontroller with 4.7μs Shutdown/Wake-up Integrating 2.3-bit/Cell Resistive RAM and Resilience Techniques")
I99103 = p.create_item(R1__has_label="Au/Pd/WOx/Au")
I28976 = p.create_item(R1__has_label="TiN/TaOx/HfOx/TiN")
I66639 = p.create_item(R1__has_label="Pt/Ta/Ta2O5/Pt/Ti")
I34380 = p.create_item(R1__has_label="Ta/TaOx/Pt")
I37464 = p.create_item(R1__has_label="W/TiN/TiON")
I11681 = p.create_item(R1__has_label="Pt/SiOxAg/Pt/Ti")
I41069 = p.create_item(R1__has_label="Ta/Pd/HfO2/Pt/Ti")
I5868 = p.create_item(R1__has_label="TiN/HfO2/Ti/TiN")
I61689 = p.create_item(R1__has_label="W/Ta2O5/TaOx/W")
I37167 = p.create_item(R1__has_label="AlCu/TiN/Ti/HfO2/TiN")
I47202 = p.create_item(R1__has_label="TiN/HfO2/TaOx/TiN")


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




has_citation_id = p.QualifierFactory(R61354["has citation id"])






# 2019_lanza 
I18540["publication: Recommended Methods to Study Resistive Switching Devices"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=["Mario Lanza", "H.-S. Philip Wong", " Eric Pop", " Daniele Ielmini", " Dimitri Strukov", " Brian C. Regan", "Luca Larcher", " Marco A. Villena", " J. Joshua Yang", " Ludovic Goux", " Attilio Belmonte", " Yuchao Yang", "Francesco M. Puglisi", " Jinfeng Kang", " Blanka Magyari-Köpe", " Eilam Yalon", " Anthony Kenyon", "Mark Buckwell", " Adnan Mehonic", " Alexander Shluger", " Haitong Li", " Tuo-Hung Hou", " Boris Hudec", "Deji Akinwande", " Ruijing Ge", " Stefano Ambrogio", " Juan B. Roldan", " Enrique Miranda", " Jordi Suñe", "Kin Leong Pey", " Xing Wu", " Nagarajan Raghavan", " Ernest Wu", " Wei D. Lu", " Gabriele Navarro", "Weidong Zhang", " Huaqiang Wu", " Runwei Li", " Alexander Holleitner", " Ursula Wurstbauer", "Max C. Lemme", " Ming Liu", " Shibing Long", " Qi Liu", " Hangbing Lv", " Andrea Padovani", "Paolo Pavan", " Ilia Valov", " Xu Jing", " Tingting Han", " Kaichen Zhu", " Shaochuan Chen", " Fei Hui", "Yuanyuan Shi"],
    ag__R8434__has_title="Recommended Methods to Study Resistive Switching Devices",
    ag__R8435__has_year=2019,
    R68407__has_internal_reference="2019_lanza_et_al",
    
)
I18540["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I6557["publication: IEEE Int. Electron Devices Meet."], qualifiers=[has_citation_id(24), ])
I18540["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I13184["publication: No title given 25631219101"], qualifiers=[has_citation_id(52), ])
I18540["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I31376["publication: Appl. Phys. Lett."], qualifiers=[has_citation_id(116), ])
I18540["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I94114["publication: Nat. Mater."], qualifiers=[has_citation_id(120), ])
I18540["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I82668["publication: presented at *IEEE Int. Electron Device Meet.*"], qualifiers=[has_citation_id(121), ])
I18540["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I91063["publication: Symp. VLSI Technol."], qualifiers=[has_citation_id(127), ])
I18540["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I79796["publication: presented at *IEEE IEDM*"], qualifiers=[has_citation_id(129), ])
I18540["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I56497["publication: No title given 41246013015"], qualifiers=[has_citation_id(133), ])
I18540["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I13384["publication: No title given 28138552030"], qualifiers=[has_citation_id(241), ])
I18540["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I39529["publication: IEEE Electron Device Lett."], qualifiers=[has_citation_id(242), ])
I18540["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I90963["publication: IEEE Trans. Electron Devices"], qualifiers=[has_citation_id(243), ])
I18540["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I5210["publication: 2011 Symp. on VLSI Technology - Digest of Technical Papers"], qualifiers=[has_citation_id(244), ])
I18540["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I24132["publication: No title given 26048021673"], qualifiers=[has_citation_id(245), ])
I18540["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I91057["publication: No title given 86846326096"], qualifiers=[has_citation_id(246), ])


# 2019_lanza 
I60787["H. Y. Lee"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="H. Y. Lee",
    
)


# 2019_lanza 
I67882["Y. S. Chen"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. S. Chen",
    
)


# 2019_lanza 
I34722["P. S. Chen"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="P. S. Chen",
    
)


# 2019_lanza 
I74868["P. Y. Gu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="P. Y. Gu",
    
)


# 2019_lanza 
I95468["Y. Y. Hsu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. Y. Hsu",
    
)


# 2019_lanza 
I16106["S. M. Wang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. M. Wang",
    
)


# 2019_lanza 
I79357["W. H. Liu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="W. H. Liu",
    
)


# 2019_lanza 
I8074["C. H. Tsai"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. H. Tsai",
    
)


# 2019_lanza 
I47536["S. S. Sheu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. S. Sheu",
    
)


# 2019_lanza 
I85771["P. C. Chiang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="P. C. Chiang",
    
)


# 2019_lanza 
I84727["W. P. Lin"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="W. P. Lin",
    
)


# 2019_lanza 
I93588["C. H. Lin"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. H. Lin",
    
)


# 2019_lanza 
I9860["W. S. Chen"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="W. S. Chen",
    
)


# 2019_lanza 
I85989["F. T. Chen"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="F. T. Chen",
    
)


# 2019_lanza 
I15339["C. H. Lien"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. H. Lien",
    
)


# 2019_lanza 
I87633["M. J. Tsai"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. J. Tsai",
    
)


# 2019_lanza 
I6557["publication: IEEE Int. Electron Devices Meet."].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I60787["H. Y. Lee"], I67882["Y. S. Chen"], I34722["P. S. Chen"], I74868["P. Y. Gu"], I95468["Y. Y. Hsu"], I16106["S. M. Wang"], I79357["W. H. Liu"], I8074["C. H. Tsai"], I47536["S. S. Sheu"], I85771["P. C. Chiang"], I84727["W. P. Lin"], I93588["C. H. Lin"], I9860["W. S. Chen"], I85989["F. T. Chen"], I15339["C. H. Lien"], I87633["M. J. Tsai"]],
    ag__R8434__has_title="IEEE Int. Electron Devices Meet.",
    ag__R8435__has_year=2010,
    R11809__has_memristor_stack=I86040["TiN/TiOx/HfOx/TiN"],
    
)


# 2019_lanza 
I57087["B. Govoreanu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="B. Govoreanu",
    
)


# 2019_lanza 
I77061["G. S. Kar"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="G. S. Kar",
    
)


# 2019_lanza 
I17932["Y-Y. Chen"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y-Y. Chen",
    
)


# 2019_lanza 
I18505["V. Paraschiv"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="V. Paraschiv",
    
)


# 2019_lanza 
I72084["S. Kubicek"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. Kubicek",
    
)


# 2019_lanza 
I19460["A. Fantini"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="A. Fantini",
    
)


# 2019_lanza 
I72376["I. P. Radu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="I. P. Radu",
    
)


# 2019_lanza 
I92025["L. Goux"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="L. Goux",
    
)


# 2019_lanza 
I93207["S. Clima"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. Clima",
    
)


# 2019_lanza 
I38568["R. Degraeve"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="R. Degraeve",
    
)


# 2019_lanza 
I24422["N. Jossart"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="N. Jossart",
    
)


# 2019_lanza 
I24045["O. Richard"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="O. Richard",
    
)


# 2019_lanza 
I26160["T. Vandeweyer"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="T. Vandeweyer",
    
)


# 2019_lanza 
I39551["K. Seo"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="K. Seo",
    
)


# 2019_lanza 
I94055["P. Hendrickx"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="P. Hendrickx",
    
)


# 2019_lanza 
I36185["G. Pourtois"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="G. Pourtois",
    
)


# 2019_lanza 
I31023["H. Bender"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="H. Bender",
    
)


# 2019_lanza 
I63537["L. Altimime"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="L. Altimime",
    
)


# 2019_lanza 
I52555["D. J. Wouters"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="D. J. Wouters",
    
)


# 2019_lanza 
I27376["J. A. Kittl"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="J. A. Kittl",
    
)


# 2019_lanza 
I20440["M. Jurczak"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. Jurczak",
    
)


# 2019_lanza 
I13184["publication: No title given 25631219101"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I57087["B. Govoreanu"], I77061["G. S. Kar"], I17932["Y-Y. Chen"], I18505["V. Paraschiv"], I72084["S. Kubicek"], I19460["A. Fantini"], I72376["I. P. Radu"], I92025["L. Goux"], I93207["S. Clima"], I38568["R. Degraeve"], I24422["N. Jossart"], I24045["O. Richard"], I26160["T. Vandeweyer"], I39551["K. Seo"], I94055["P. Hendrickx"], I36185["G. Pourtois"], I31023["H. Bender"], I63537["L. Altimime"], I52555["D. J. Wouters"], I27376["J. A. Kittl"], I20440["M. Jurczak"]],
    ag__R8434__has_title="No title given 25631219101",
    ag__R8435__has_year=2011,
    R11809__has_memristor_stack=I76227["TiN/Hf/HfOx/TiN"],
    
)


# 2019_lanza 
I1679["J. J. Yang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="J. J. Yang",
    
)


# 2019_lanza 
I89283["M.-X. Zhang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M.-X. Zhang",
    
)


# 2019_lanza 
I72952["J. P. Strachan"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="J. P. Strachan",
    
)


# 2019_lanza 
I6909["F. Miao"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="F. Miao",
    
)


# 2019_lanza 
I53460["M. D. Pickett"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. D. Pickett",
    
)


# 2019_lanza 
I68385["R. D. Kelley"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="R. D. Kelley",
    
)


# 2019_lanza 
I44786["G. Medeiros-Ribeiro"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="G. Medeiros-Ribeiro",
    
)


# 2019_lanza 
I6037["R. S. Williams"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="R. S. Williams",
    
)


# 2019_lanza 
I31376["publication: Appl. Phys. Lett."].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I1679["J. J. Yang"], I89283["M.-X. Zhang"], I72952["J. P. Strachan"], I6909["F. Miao"], I53460["M. D. Pickett"], I68385["R. D. Kelley"], I44786["G. Medeiros-Ribeiro"], I6037["R. S. Williams"]],
    ag__R8434__has_title="Appl. Phys. Lett.",
    ag__R8435__has_year=2010,
    R11809__has_memristor_stack=I67803["Pt/TaOx/Ta"],
    
)


# 2019_lanza 
I3139["M. J. Lee"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. J. Lee",
    
)


# 2019_lanza 
I31567["C. B. Lee"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. B. Lee",
    
)


# 2019_lanza 
I75821["D. S. Lee"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="D. S. Lee",
    
)


# 2019_lanza 
I96458["S. R. Lee"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. R. Lee",
    
)


# 2019_lanza 
I18688["M. Chang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. Chang",
    
)


# 2019_lanza 
I26296["J. H. Hur"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="J. H. Hur",
    
)


# 2019_lanza 
I75465["Y. B. Kim"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. B. Kim",
    
)


# 2019_lanza 
I93192["C. J. Kim"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. J. Kim",
    
)


# 2019_lanza 
I7316["D. H. Seo"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="D. H. Seo",
    
)


# 2019_lanza 
I47350["S. Seo"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. Seo",
    
)


# 2019_lanza 
I84610["U. I. Chung"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="U. I. Chung",
    
)


# 2019_lanza 
I33761["I. K. Yoo"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="I. K. Yoo",
    
)


# 2019_lanza 
I63613["K. Kim"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="K. Kim",
    
)


# 2019_lanza 
I94114["publication: Nat. Mater."].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I3139["M. J. Lee"], I31567["C. B. Lee"], I75821["D. S. Lee"], I96458["S. R. Lee"], I18688["M. Chang"], I26296["J. H. Hur"], I75465["Y. B. Kim"], I93192["C. J. Kim"], I7316["D. H. Seo"], I47350["S. Seo"], I84610["U. I. Chung"], I33761["I. K. Yoo"], I63613["K. Kim"]],
    ag__R8434__has_title="Nat. Mater.",
    ag__R8435__has_year=2011,
    R11809__has_memristor_stack=I45775["Pt/Ta2O5-x/TaO2-x/Pt"],
    
)


# 2019_lanza 
I37565["I G. Baek"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="I G. Baek",
    
)


# 2019_lanza 
I88176["M. S. Lee"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. S. Lee",
    
)


# 2019_lanza 
I28585["D. S. Suh"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="D. S. Suh",
    
)


# 2019_lanza 
I16241["J. C. Park"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="J. C. Park",
    
)


# 2019_lanza 
I12074["S. O. Park"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. O. Park",
    
)


# 2019_lanza 
I30366["H. S. Kim"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="H. S. Kim",
    
)


# 2019_lanza 
I76063["J. T. Moon"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="J. T. Moon",
    
)


# 2019_lanza 
I82668["publication: presented at *IEEE Int. Electron Device Meet.*"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I37565["I G. Baek"], I88176["M. S. Lee"], I47350["S. Seo"], I3139["M. J. Lee"], I7316["D. H. Seo"], I28585["D. S. Suh"], I16241["J. C. Park"], I12074["S. O. Park"], I30366["H. S. Kim"], I33761["I. K. Yoo"], I84610["U. I. Chung"], I76063["J. T. Moon"]],
    ag__R8434__has_title="presented at *IEEE Int. Electron Device Meet.*",
    ag__R8435__has_year=2004,
    R11809__has_memristor_stack=I79564["Ta/TaOx/TiO2/Ti"],
    
)


# 2019_lanza 
I79359["C. H. Cheng"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. H. Cheng",
    
)


# 2019_lanza 
I51636["A. Chin"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="A. Chin",
    
)


# 2019_lanza 
I38505["F. S. Yeh"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="F. S. Yeh",
    
)


# 2019_lanza 
I91063["publication: Symp. VLSI Technol."].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I79359["C. H. Cheng"], I51636["A. Chin"], I38505["F. S. Yeh"]],
    ag__R8434__has_title="Symp. VLSI Technol.",
    ag__R8435__has_year=2010,
    R11809__has_memristor_stack=I99459["Ni/GeO/STO/TaN"],
    
)


# 2019_lanza 
I96093["Z. Wei"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Z. Wei",
    
)


# 2019_lanza 
I31934["Y. Kanzawa"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. Kanzawa",
    
)


# 2019_lanza 
I90518["K. Arita"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="K. Arita",
    
)


# 2019_lanza 
I11228["Y. Katoh"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. Katoh",
    
)


# 2019_lanza 
I46274["K. Kawai"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="K. Kawai",
    
)


# 2019_lanza 
I28662["S. Muraoka"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. Muraoka",
    
)


# 2019_lanza 
I35553["S. Mitani"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. Mitani",
    
)


# 2019_lanza 
I48163["S. Fujii"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. Fujii",
    
)


# 2019_lanza 
I66013["K. Katayama"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="K. Katayama",
    
)


# 2019_lanza 
I79007["M. Iijima"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. Iijima",
    
)


# 2019_lanza 
I1871["T. Mikawa"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="T. Mikawa",
    
)


# 2019_lanza 
I8544["T. Ninomiya"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="T. Ninomiya",
    
)


# 2019_lanza 
I66252["R. Miyanaga"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="R. Miyanaga",
    
)


# 2019_lanza 
I16648["Y. Kawashima"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. Kawashima",
    
)


# 2019_lanza 
I91231["K. Tsuji"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="K. Tsuji",
    
)


# 2019_lanza 
I5202["A. Himeno"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="A. Himeno",
    
)


# 2019_lanza 
I66876["T. Okada"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="T. Okada",
    
)


# 2019_lanza 
I17956["R. Azuma"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="R. Azuma",
    
)


# 2019_lanza 
I10396["K. Shimakawa"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="K. Shimakawa",
    
)


# 2019_lanza 
I79049["H. Sugaya"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="H. Sugaya",
    
)


# 2019_lanza 
I3375["T. Takagi"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="T. Takagi",
    
)


# 2019_lanza 
I91390["R. Yasuhara"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="R. Yasuhara",
    
)


# 2019_lanza 
I45686["K. Horiba"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="K. Horiba",
    
)


# 2019_lanza 
I87710["H. Kumigashira"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="H. Kumigashira",
    
)


# 2019_lanza 
I19647["M. Oshima"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. Oshima",
    
)


# 2019_lanza 
I79796["publication: presented at *IEEE IEDM*"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I96093["Z. Wei"], I31934["Y. Kanzawa"], I90518["K. Arita"], I11228["Y. Katoh"], I46274["K. Kawai"], I28662["S. Muraoka"], I35553["S. Mitani"], I48163["S. Fujii"], I66013["K. Katayama"], I79007["M. Iijima"], I1871["T. Mikawa"], I8544["T. Ninomiya"], I66252["R. Miyanaga"], I16648["Y. Kawashima"], I91231["K. Tsuji"], I5202["A. Himeno"], I66876["T. Okada"], I17956["R. Azuma"], I10396["K. Shimakawa"], I79049["H. Sugaya"], I3375["T. Takagi"], I91390["R. Yasuhara"], I45686["K. Horiba"], I87710["H. Kumigashira"], I19647["M. Oshima"]],
    ag__R8434__has_title="presented at *IEEE IEDM*",
    ag__R8435__has_year=2008,
    R11809__has_memristor_stack=I5377["Pt/TaOx/Pt"],
    
)


# 2019_lanza 
I3560["L. G. Wang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="L. G. Wang",
    
)


# 2019_lanza 
I78447["X. Qian"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="X. Qian",
    
)


# 2019_lanza 
I72007["Y. Q. Cao"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. Q. Cao",
    
)


# 2019_lanza 
I36884["Z. Y. Cao"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Z. Y. Cao",
    
)


# 2019_lanza 
I87369["G. Y. Fang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="G. Y. Fang",
    
)


# 2019_lanza 
I34943["A. D. Li"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="A. D. Li",
    
)


# 2019_lanza 
I69977["D. Wu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="D. Wu",
    
)


# 2019_lanza 
I56497["publication: No title given 41246013015"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I3560["L. G. Wang"], I78447["X. Qian"], I72007["Y. Q. Cao"], I36884["Z. Y. Cao"], I87369["G. Y. Fang"], I34943["A. D. Li"], I69977["D. Wu"]],
    ag__R8434__has_title="No title given 41246013015",
    ag__R8435__has_year=2015,
    R11809__has_memristor_stack=I93059["Pt/Al2O3/HfO2/Al2O3/TiN/Si"],
    
)


# 2019_lanza 
I55117["H.-S. P. Wong"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="H.-S. P. Wong",
    
)


# 2019_lanza 
I81948["S. Yu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. Yu",
    
)


# 2019_lanza 
I8432["Y. Wu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. Wu",
    
)


# 2019_lanza 
I49144["B. Lee"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="B. Lee",
    
)


# 2019_lanza 
I13384["publication: No title given 28138552030"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I55117["H.-S. P. Wong"], I60787["H. Y. Lee"], I81948["S. Yu"], I67882["Y. S. Chen"], I8432["Y. Wu"], I34722["P. S. Chen"], I49144["B. Lee"], I85989["F. T. Chen"], I87633["M. J. Tsai"]],
    ag__R8434__has_title="No title given 28138552030",
    ag__R8435__has_year=2012,
    R11809__has_memristor_stack=I86040["TiN/TiOx/HfOx/TiN"],
    
)


# 2019_lanza 
I75653["M. C. Wu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. C. Wu",
    
)


# 2019_lanza 
I73280["Y. W. Lin"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. W. Lin",
    
)


# 2019_lanza 
I31254["W. Y. Jang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="W. Y. Jang",
    
)


# 2019_lanza 
I67533["T. Y. Tseng"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="T. Y. Tseng",
    
)


# 2019_lanza 
I39529["publication: IEEE Electron Device Lett."].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I75653["M. C. Wu"], I73280["Y. W. Lin"], I31254["W. Y. Jang"], I93588["C. H. Lin"], I67533["T. Y. Tseng"]],
    ag__R8434__has_title="IEEE Electron Device Lett.",
    ag__R8435__has_year=2011,
    R11809__has_memristor_stack=I60665["Ti/ZrO2/Pt"],
    
)


# 2019_lanza 
I74938["C. Ahn"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. Ahn",
    
)


# 2019_lanza 
I85012["Z. Jiang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Z. Jiang",
    
)


# 2019_lanza 
I99712["C. S. Lee"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. S. Lee",
    
)


# 2019_lanza 
I94362["H. Y. Chen"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="H. Y. Chen",
    
)


# 2019_lanza 
I85528["J. Liang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="J. Liang",
    
)


# 2019_lanza 
I2855["L. S. Liyanage"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="L. S. Liyanage",
    
)


# 2019_lanza 
I46793["H. S. P. Wong"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="H. S. P. Wong",
    
)


# 2019_lanza 
I90963["publication: IEEE Trans. Electron Devices"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I74938["C. Ahn"], I85012["Z. Jiang"], I99712["C. S. Lee"], I94362["H. Y. Chen"], I85528["J. Liang"], I2855["L. S. Liyanage"], I46793["H. S. P. Wong"]],
    ag__R8434__has_title="IEEE Trans. Electron Devices",
    ag__R8435__has_year=2015,
    R11809__has_memristor_stack=I11040["Al/Ti/Al2O3/s-CNT"],
    
)


# 2019_lanza 
I54975["D. Lee"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="D. Lee",
    
)


# 2019_lanza 
I72751["G. S. Park"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="G. S. Park",
    
)


# 2019_lanza 
I80078["U. Chung"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="U. Chung",
    
)


# 2019_lanza 
I5210["publication: 2011 Symp. on VLSI Technology - Digest of Technical Papers"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I75465["Y. B. Kim"], I96458["S. R. Lee"], I54975["D. Lee"], I31567["C. B. Lee"], I18688["M. Chang"], I26296["J. H. Hur"], I3139["M. J. Lee"], I72751["G. S. Park"], I93192["C. J. Kim"], I80078["U. Chung"], I33761["I. K. Yoo"], I63613["K. Kim"]],
    ag__R8434__has_title="2011 Symp. on VLSI Technology - Digest of Technical Papers",
    ag__R8435__has_year=2011,
    R11809__has_memristor_stack=I37074["W/AlO/TaOx/ZrOx/Ru"],
    
)


# 2019_lanza 
I32782["V. K. Nagareddy"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="V. K. Nagareddy",
    
)


# 2019_lanza 
I91760["A. K. Ott"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="A. K. Ott",
    
)


# 2019_lanza 
I91215["C. Dou"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. Dou",
    
)


# 2019_lanza 
I81970["T. Tsvetkova"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="T. Tsvetkova",
    
)


# 2019_lanza 
I68229["M. Sandulov"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. Sandulov",
    
)


# 2019_lanza 
I64747["M. F. Craciun"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. F. Craciun",
    
)


# 2019_lanza 
I39757["A. C. Ferrari"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="A. C. Ferrari",
    
)


# 2019_lanza 
I30227["C. D. Wright"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. D. Wright",
    
)


# 2019_lanza 
I24132["publication: No title given 26048021673"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I32782["V. K. Nagareddy"], I91760["A. K. Ott"], I91215["C. Dou"], I81970["T. Tsvetkova"], I68229["M. Sandulov"], I64747["M. F. Craciun"], I39757["A. C. Ferrari"], I30227["C. D. Wright"]],
    ag__R8434__has_title="No title given 26048021673",
    R11809__has_memristor_stack=I48946["TaN/TiN/Zr/HfO2/CAFM tip"],
    
)


# 2019_lanza 
I14404["X. Cao"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="X. Cao",
    
)


# 2019_lanza 
I65317["X. M. Li"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="X. M. Li",
    
)


# 2019_lanza 
I25665["X. D. Gao"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="X. D. Gao",
    
)


# 2019_lanza 
I85099["W. D. Yu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="W. D. Yu",
    
)


# 2019_lanza 
I97353["X. J. Liu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="X. J. Liu",
    
)


# 2019_lanza 
I47693["Y. W. Zhang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. W. Zhang",
    
)


# 2019_lanza 
I17571["L. D. Chen"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="L. D. Chen",
    
)


# 2019_lanza 
I63422["X. H. Cheng"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="X. H. Cheng",
    
)


# 2019_lanza 
I91057["publication: No title given 86846326096"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I14404["X. Cao"], I65317["X. M. Li"], I25665["X. D. Gao"], I85099["W. D. Yu"], I97353["X. J. Liu"], I47693["Y. W. Zhang"], I17571["L. D. Chen"], I63422["X. H. Cheng"]],
    ag__R8434__has_title="No title given 86846326096",
    ag__R8435__has_year=2009,
    R11809__has_memristor_stack=I45993["Pt/Gd2O3/Pt"],
    
)


# 2019_lanza 
I86040["TiN/TiOx/HfOx/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I86040["TiN/TiOx/HfOx/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I86040["TiN/TiOx/HfOx/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I86040["TiN/TiOx/HfOx/TiN"].set_relation(R48517["has stack component"], omt.I6120["TiOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I86040["TiN/TiOx/HfOx/TiN"].set_relation(R48517["has stack component"], omt.I6105["HfOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019_lanza 



# 2019_lanza 



# 2019_lanza 



# 2019_lanza 
I60665["Ti/ZrO2/Pt"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I60665["Ti/ZrO2/Pt"].set_relation(R48517["has stack component"], omt.I87594["titanium"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I60665["Ti/ZrO2/Pt"].set_relation(R48517["has stack component"], I36571["ZrO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I60665["Ti/ZrO2/Pt"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019_lanza 



# 2019_lanza 
I36571["ZrO2"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019_lanza 



# 2019_lanza 
I76227["TiN/Hf/HfOx/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I76227["TiN/Hf/HfOx/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I76227["TiN/Hf/HfOx/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I76227["TiN/Hf/HfOx/TiN"].set_relation(R48517["has stack component"], omt.I79894["hafnium"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I76227["TiN/Hf/HfOx/TiN"].set_relation(R48517["has stack component"], omt.I6105["HfOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019_lanza 



# 2019_lanza 
I11040["Al/Ti/Al2O3/s-CNT"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I11040["Al/Ti/Al2O3/s-CNT"].set_relation(R48517["has stack component"], omt.I85583["aluminum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I11040["Al/Ti/Al2O3/s-CNT"].set_relation(R48517["has stack component"], omt.I87594["titanium"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I11040["Al/Ti/Al2O3/s-CNT"].set_relation(R48517["has stack component"], omt.I6100["Al2O3"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I11040["Al/Ti/Al2O3/s-CNT"].set_relation(R48517["has stack component"], I40507["s-CNT"], qualifiers=[has_position(3), is_at_outer_position(True), ])


# 2019_lanza 



# 2019_lanza 



# 2019_lanza 
I40507["s-CNT"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019_lanza 
I45775["Pt/Ta2O5-x/TaO2-x/Pt"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I45775["Pt/Ta2O5-x/TaO2-x/Pt"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I45775["Pt/Ta2O5-x/TaO2-x/Pt"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I45775["Pt/Ta2O5-x/TaO2-x/Pt"].set_relation(R48517["has stack component"], I88802["Ta2O5-x"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I45775["Pt/Ta2O5-x/TaO2-x/Pt"].set_relation(R48517["has stack component"], I89671["TaO2-x"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019_lanza 
I88802["Ta2O5-x"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019_lanza 
I89671["TaO2-x"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019_lanza 
I5377["Pt/TaOx/Pt"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I5377["Pt/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I5377["Pt/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I5377["Pt/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_lanza 



# 2019_lanza 
I79564["Ta/TaOx/TiO2/Ti"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I79564["Ta/TaOx/TiO2/Ti"].set_relation(R48517["has stack component"], omt.I38968["tantalum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I79564["Ta/TaOx/TiO2/Ti"].set_relation(R48517["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I79564["Ta/TaOx/TiO2/Ti"].set_relation(R48517["has stack component"], omt.I6119["TiO2"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I79564["Ta/TaOx/TiO2/Ti"].set_relation(R48517["has stack component"], omt.I87594["titanium"], qualifiers=[has_position(3), is_at_outer_position(True), ])


# 2019_lanza 



# 2019_lanza 



# 2019_lanza 
I67803["Pt/TaOx/Ta"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I67803["Pt/TaOx/Ta"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I67803["Pt/TaOx/Ta"].set_relation(R48517["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I67803["Pt/TaOx/Ta"].set_relation(R48517["has stack component"], omt.I38968["tantalum"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019_lanza 
I37074["W/AlO/TaOx/ZrOx/Ru"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I37074["W/AlO/TaOx/ZrOx/Ru"].set_relation(R48517["has stack component"], omt.I41958["tungsten"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I37074["W/AlO/TaOx/ZrOx/Ru"].set_relation(R48517["has stack component"], I34513["AlO"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I37074["W/AlO/TaOx/ZrOx/Ru"].set_relation(R48517["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I37074["W/AlO/TaOx/ZrOx/Ru"].set_relation(R48517["has stack component"], I4484["ZrOx"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I37074["W/AlO/TaOx/ZrOx/Ru"].set_relation(R48517["has stack component"], omt.I97157["ruthenium"], qualifiers=[has_position(4), is_at_outer_position(True), ])


# 2019_lanza 



# 2019_lanza 
I34513["AlO"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019_lanza 
I4484["ZrOx"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019_lanza 



# 2019_lanza 
I93059["Pt/Al2O3/HfO2/Al2O3/TiN/Si"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I93059["Pt/Al2O3/HfO2/Al2O3/TiN/Si"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I93059["Pt/Al2O3/HfO2/Al2O3/TiN/Si"].set_relation(R48517["has stack component"], omt.I6100["Al2O3"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I93059["Pt/Al2O3/HfO2/Al2O3/TiN/Si"].set_relation(R48517["has stack component"], omt.I6100["Al2O3"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I93059["Pt/Al2O3/HfO2/Al2O3/TiN/Si"].set_relation(R48517["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I93059["Pt/Al2O3/HfO2/Al2O3/TiN/Si"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(4), is_at_outer_position(False), ])
I93059["Pt/Al2O3/HfO2/Al2O3/TiN/Si"].set_relation(R48517["has stack component"], omt.I70616["silicon"], qualifiers=[has_position(5), is_at_outer_position(True), ])


# 2019_lanza 



# 2019_lanza 



# 2019_lanza 
I48946["TaN/TiN/Zr/HfO2/CAFM tip"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I48946["TaN/TiN/Zr/HfO2/CAFM tip"].set_relation(R48517["has stack component"], omt.I6125["TaN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I48946["TaN/TiN/Zr/HfO2/CAFM tip"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I48946["TaN/TiN/Zr/HfO2/CAFM tip"].set_relation(R48517["has stack component"], omt.I61164["zirconium"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I48946["TaN/TiN/Zr/HfO2/CAFM tip"].set_relation(R48517["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I48946["TaN/TiN/Zr/HfO2/CAFM tip"].set_relation(R48517["has stack component"], I44836["CAFM tip"], qualifiers=[has_position(4), is_at_outer_position(True), ])


# 2019_lanza 



# 2019_lanza 



# 2019_lanza 
I44836["CAFM tip"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019_lanza 
I99459["Ni/GeO/STO/TaN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I99459["Ni/GeO/STO/TaN"].set_relation(R48517["has stack component"], omt.I87636["nickel"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I99459["Ni/GeO/STO/TaN"].set_relation(R48517["has stack component"], I48965["GeO"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I99459["Ni/GeO/STO/TaN"].set_relation(R48517["has stack component"], I85347["STO"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I99459["Ni/GeO/STO/TaN"].set_relation(R48517["has stack component"], omt.I6125["TaN"], qualifiers=[has_position(3), is_at_outer_position(True), ])


# 2019_lanza 



# 2019_lanza 
I48965["GeO"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019_lanza 
I85347["STO"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019_lanza 
I45993["Pt/Gd2O3/Pt"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I45993["Pt/Gd2O3/Pt"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I45993["Pt/Gd2O3/Pt"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I45993["Pt/Gd2O3/Pt"].set_relation(R48517["has stack component"], I24141["Gd2O3"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_lanza 
I24141["Gd2O3"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019_xia 
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=["Qiangfei Xia", "J. Joshua Yang"],
    ag__R8434__has_title="Memristive crossbar arrays for brain-inspired computing",
    ag__R8435__has_year=2019,
    R68407__has_internal_reference="2019_xia_et_al",
    
)
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I69974["publication: Memristors with difusive dynamics as synaptic emulators for neuromorphic computing"], qualifiers=[has_citation_id(33), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I87242["publication: Tree-dimensional crossbar arrays of self-rectifying Si/SiO2/Si memristors"], qualifiers=[has_citation_id(54), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I78857["publication: Anatomy of Ag/Hafnia-based selectors with 1010 nonlinearity"], qualifiers=[has_citation_id(92), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I39708["publication: Bipolar nonlinear Ni/ TiO2/Ni selector for 1S1R crossbar array applications"], qualifiers=[has_citation_id(94), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I53205["publication: TiO2-based metal–insulator–metal selection device for bipolar resistive random access memory cross-point application"], qualifiers=[has_citation_id(95), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I41902["publication: High-performance metal–insulator–metal tunnel diode selectors"], qualifiers=[has_citation_id(96), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I97657["publication: Electrical and reliability characteristics of a scaled (∼30nm) tunnel barrier selector (W/Ta2O5/TaOx/TiO2/TiN) with excellent performance (JMAX>107A/cm2)"], qualifiers=[has_citation_id(97), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I21621["publication: Varistor-type bidirectional switch (JMAX>107A/cm2 , selectivity ∼104 ) for 3D bipolar resistive memory arrays"], qualifiers=[has_citation_id(98), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I58690["publication: Trilayer tunnel selectors for memristor memory cells"], qualifiers=[has_citation_id(99), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I28840["publication: An 8 Mb multi-layered cross-point ReRAM macro with 443 MB/s write throughput"], qualifiers=[has_citation_id(100), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I49189["publication: Termally stable integrated Se-based OTS selectors with >20MA/cm2 current drive, >3.103 half-bias nonlinearity, tunable threshold voltage and excellent endurance"], qualifiers=[has_citation_id(102), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I74720["publication: Breakthrough of selector technology for cross-point 25-nm ReRAM"], qualifiers=[has_citation_id(106), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I45292["publication: Excellent selector characteristics of nanoscale VO2 for high-density bipolar ReRAM applications"], qualifiers=[has_citation_id(107), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I66609["publication: NbO2-based low power and cost efective 1S1R switching for high density cross point ReRAM application"], qualifiers=[has_citation_id(108), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I16712["publication: Nanoscale (∼10nm) 3D vertical ReRAM and NbO2 threshold selector with TiN electrode"], qualifiers=[has_citation_id(109), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I73173["publication: Highly-scalable threshold switching select device based on chalcogenide glasses for 3D nanoscaled memory arrays"], qualifiers=[has_citation_id(110), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I12092["publication: Physically transient threshold switching device based on magnesium oxide for security application"], qualifiers=[has_citation_id(111), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I50118["publication: High‐performance and low‐power rewritable SiO*x* 1 kbit one diode–one resistor crossbar memory array"], qualifiers=[has_citation_id(114), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I52771["publication: Vacancy-modulated conductive oxide resistive RAM (VMCO-RRAM): an area-scalable switching current, self-compliant, highly nonlinear and wide on/of-window resistive switching cell"], qualifiers=[has_citation_id(115), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I9385["publication: Self-selective characteristics of nanoscale VOx devices for high-density ReRAM applications"], qualifiers=[has_citation_id(116), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I47402["publication: Investigations of conduction mechanisms of the self-rectifying n<sup>+</sup>Si-HfO2-Ni RRAM devices"], qualifiers=[has_citation_id(117), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I92934["publication: Unipolar resistive switching with forming-free and self-rectifying efects in Cu/HfO2/n-Si devices"], qualifiers=[has_citation_id(118), ])
I35428["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I83048["publication: Nanoscale resistive memory with intrinsic diode characteristics and long endurance"], qualifiers=[has_citation_id(119), ])


# 2019_xia 
I10778["Wang, Z."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wang, Z.",
    
)


# 2019_xia 
I69974["publication: Memristors with difusive dynamics as synaptic emulators for neuromorphic computing"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I10778["Wang, Z."],
    ag__R8434__has_title="Memristors with difusive dynamics as synaptic emulators for neuromorphic computing",
    ag__R8435__has_year=2017,
    R11809__has_memristor_stack=I24977["Pt/Ag:SiOxNy/Pt"],
    
)


# 2019_xia 
I70494["Li, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Li, C.",
    
)


# 2019_xia 
I87242["publication: Tree-dimensional crossbar arrays of self-rectifying Si/SiO2/Si memristors"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I70494["Li, C."],
    ag__R8434__has_title="Tree-dimensional crossbar arrays of self-rectifying Si/SiO2/Si memristors",
    ag__R8435__has_year=2017,
    R11809__has_memristor_stack=I63066["p-Si/SiO2/n-Si"],
    
)


# 2019_xia 
I93860["Midya, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Midya, R.",
    
)


# 2019_xia 
I78857["publication: Anatomy of Ag/Hafnia-based selectors with 1010 nonlinearity"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I93860["Midya, R."],
    ag__R8434__has_title="Anatomy of Ag/Hafnia-based selectors with 1010 nonlinearity",
    ag__R8435__has_year=2017,
    R11809__has_memristor_stack=I9309["Pd/Ag/HfO2/Ag/Pd"],
    
)


# 2019_xia 
I94601["Huang, J.-J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Huang, J.-J.",
    
)


# 2019_xia 
I52917["Tseng, Y.-M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Tseng, Y.-M.",
    
)


# 2019_xia 
I86787["Hsu, C.-W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Hsu, C.-W.",
    
)


# 2019_xia 
I21123["Hou, T.-H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Hou, T.-H.",
    
)


# 2019_xia 
I39708["publication: Bipolar nonlinear Ni/ TiO2/Ni selector for 1S1R crossbar array applications"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I94601["Huang, J.-J."], I52917["Tseng, Y.-M."], I86787["Hsu, C.-W."], I21123["Hou, T.-H."]],
    ag__R8434__has_title="Bipolar nonlinear Ni/ TiO2/Ni selector for 1S1R crossbar array applications",
    ag__R8435__has_year=2011,
    R11809__has_memristor_stack=I71732["Ni/TiO2/Ni"],
    
)


# 2019_xia 
I93276["Shin, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Shin, J.",
    
)


# 2019_xia 
I53205["publication: TiO2-based metal–insulator–metal selection device for bipolar resistive random access memory cross-point application"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I93276["Shin, J."],
    ag__R8434__has_title="TiO2-based metal–insulator–metal selection device for bipolar resistive random access memory cross-point application",
    ag__R8435__has_year=2011,
    R11809__has_memristor_stack=I16765["Pt/TiO2/TiN"],
    
)


# 2019_xia 
I87136["Govoreanu, B."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Govoreanu, B.",
    
)


# 2019_xia 
I41902["publication: High-performance metal–insulator–metal tunnel diode selectors"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I87136["Govoreanu, B."],
    ag__R8434__has_title="High-performance metal–insulator–metal tunnel diode selectors",
    ag__R8435__has_year=2014,
    R11809__has_memristor_stack=I18578["TiN/Ta2O5/TiN"],
    
)


# 2019_xia 
I85417["Woo, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Woo, J.",
    
)


# 2019_xia 
I97657["publication: Electrical and reliability characteristics of a scaled (∼30nm) tunnel barrier selector (W/Ta2O5/TaOx/TiO2/TiN) with excellent performance (JMAX>107A/cm2)"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I85417["Woo, J."],
    ag__R8434__has_title="Electrical and reliability characteristics of a scaled (∼30nm) tunnel barrier selector (W/Ta2O5/TaOx/TiO2/TiN) with excellent performance (JMAX>107A/cm2)",
    ag__R8435__has_year=2014,
    R11809__has_memristor_stack=I87992["W/Ta2O5/TaOx/TiO2/TiN"],
    
)


# 2019_xia 
I29872["Lee, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Lee, W.",
    
)


# 2019_xia 
I21621["publication: Varistor-type bidirectional switch (JMAX>107A/cm2 , selectivity ∼104 ) for 3D bipolar resistive memory arrays"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I29872["Lee, W."],
    ag__R8434__has_title="Varistor-type bidirectional switch (JMAX>107A/cm2 , selectivity ∼104 ) for 3D bipolar resistive memory arrays",
    ag__R8435__has_year=2012,
    R11809__has_memristor_stack=I44440["Pt/TaOx/TiO2/TaOx/Pt"],
    
)


# 2019_xia 
I87604["Choi, B. J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Choi, B. J.",
    
)


# 2019_xia 
I58690["publication: Trilayer tunnel selectors for memristor memory cells"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I87604["Choi, B. J."],
    ag__R8434__has_title="Trilayer tunnel selectors for memristor memory cells",
    ag__R8435__has_year=2016,
    R11809__has_memristor_stack=I58468["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"],
    
)


# 2019_xia 
I7533["Kawahara, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kawahara, A.",
    
)


# 2019_xia 
I28840["publication: An 8 Mb multi-layered cross-point ReRAM macro with 443 MB/s write throughput"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I7533["Kawahara, A."],
    ag__R8434__has_title="An 8 Mb multi-layered cross-point ReRAM macro with 443 MB/s write throughput",
    ag__R8435__has_year=2013,
    R11809__has_memristor_stack=I47470["TaN/SiNx/TaN"],
    
)


# 2019_xia 
I49189["publication: Termally stable integrated Se-based OTS selectors with >20MA/cm2 current drive, >3.103 half-bias nonlinearity, tunable threshold voltage and excellent endurance"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I87136["Govoreanu, B."],
    ag__R8434__has_title="Termally stable integrated Se-based OTS selectors with >20MA/cm2 current drive, >3.103 half-bias nonlinearity, tunable threshold voltage and excellent endurance",
    ag__R8435__has_year=2017,
    R11809__has_memristor_stack=I82062["TiN/GexSe1-x/TiN"],
    
)


# 2019_xia 
I8849["Kim, S. G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kim, S. G.",
    
)


# 2019_xia 
I74720["publication: Breakthrough of selector technology for cross-point 25-nm ReRAM"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I8849["Kim, S. G."],
    ag__R8434__has_title="Breakthrough of selector technology for cross-point 25-nm ReRAM",
    ag__R8435__has_year=2017,
    R11809__has_memristor_stack=I58157["TiN/As:SiO2/TiN"],
    
)


# 2019_xia 
I95219["Son, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Son, M.",
    
)


# 2019_xia 
I45292["publication: Excellent selector characteristics of nanoscale VO2 for high-density bipolar ReRAM applications"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I95219["Son, M."],
    ag__R8434__has_title="Excellent selector characteristics of nanoscale VO2 for high-density bipolar ReRAM applications",
    ag__R8435__has_year=2011,
    R11809__has_memristor_stack=I27966["Pt/VO2/Pt"],
    
)


# 2019_xia 
I90863["Kim, W. G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kim, W. G.",
    
)


# 2019_xia 
I66609["publication: NbO2-based low power and cost efective 1S1R switching for high density cross point ReRAM application"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I90863["Kim, W. G."],
    ag__R8434__has_title="NbO2-based low power and cost efective 1S1R switching for high density cross point ReRAM application",
    ag__R8435__has_year=2014,
    R11809__has_memristor_stack=I21352["TiN/NbO2/TiN"],
    
)


# 2019_xia 
I26240["Cha, E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Cha, E.",
    
)


# 2019_xia 
I16712["publication: Nanoscale (∼10nm) 3D vertical ReRAM and NbO2 threshold selector with TiN electrode"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I26240["Cha, E."],
    ag__R8434__has_title="Nanoscale (∼10nm) 3D vertical ReRAM and NbO2 threshold selector with TiN electrode",
    ag__R8435__has_year=2013,
    R11809__has_memristor_stack=I46285["TiN/NbO2/W"],
    
)


# 2019_xia 
I26637["Lee, M.-J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Lee, M.-J.",
    
)


# 2019_xia 
I73173["publication: Highly-scalable threshold switching select device based on chalcogenide glasses for 3D nanoscaled memory arrays"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I26637["Lee, M.-J."],
    ag__R8434__has_title="Highly-scalable threshold switching select device based on chalcogenide glasses for 3D nanoscaled memory arrays",
    ag__R8435__has_year=2012,
    R11809__has_memristor_stack=I6912["TiN/AsTeGeSiN/TiN"],
    
)


# 2019_xia 
I77352["Sun, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Sun, J.",
    
)


# 2019_xia 
I12092["publication: Physically transient threshold switching device based on magnesium oxide for security application"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I77352["Sun, J."],
    ag__R8434__has_title="Physically transient threshold switching device based on magnesium oxide for security application",
    ag__R8435__has_year=2018,
    R11809__has_memristor_stack=I26347["W/Ag/MgO/Ag/W"],
    
)


# 2019_xia 
I95662["Wang, G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wang, G.",
    
)


# 2019_xia 
I50118["publication: High‐performance and low‐power rewritable SiO*x* 1 kbit one diode–one resistor crossbar memory array"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I95662["Wang, G."],
    ag__R8434__has_title="High‐performance and low‐power rewritable SiO*x* 1 kbit one diode–one resistor crossbar memory array",
    ag__R8435__has_year=2013,
    
)


# 2019_xia 
I52771["publication: Vacancy-modulated conductive oxide resistive RAM (VMCO-RRAM): an area-scalable switching current, self-compliant, highly nonlinear and wide on/of-window resistive switching cell"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I87136["Govoreanu, B."],
    ag__R8434__has_title="Vacancy-modulated conductive oxide resistive RAM (VMCO-RRAM): an area-scalable switching current, self-compliant, highly nonlinear and wide on/of-window resistive switching cell",
    ag__R8435__has_year=2013,
    R11809__has_memristor_stack=I93983["TiN/Al2O3/TiO2/TiN"],
    
)


# 2019_xia 
I38213["Song, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Song, M.",
    
)


# 2019_xia 
I9385["publication: Self-selective characteristics of nanoscale VOx devices for high-density ReRAM applications"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I38213["Song, M."],
    ag__R8434__has_title="Self-selective characteristics of nanoscale VOx devices for high-density ReRAM applications",
    ag__R8435__has_year=2012,
    R11809__has_memristor_stack=I18158["W/VOx/Pt"],
    
)


# 2019_xia 
I34131["Lu, D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Lu, D.",
    
)


# 2019_xia 
I47402["publication: Investigations of conduction mechanisms of the self-rectifying n<sup>+</sup>Si-HfO2-Ni RRAM devices"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I34131["Lu, D."],
    ag__R8434__has_title="Investigations of conduction mechanisms of the self-rectifying n<sup>+</sup>Si-HfO2-Ni RRAM devices",
    ag__R8435__has_year=2014,
    R11809__has_memristor_stack=I55774["Ni/HfO2/n-Si"],
    
)


# 2019_xia 
I8777["Wang, M. J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wang, M. J.",
    
)


# 2019_xia 
I61519["Gao, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Gao, S.",
    
)


# 2019_xia 
I89808["Zeng, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Zeng, F.",
    
)


# 2019_xia 
I73802["Song, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Song, C.",
    
)


# 2019_xia 
I63079["Pan, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Pan, F.",
    
)


# 2019_xia 
I92934["publication: Unipolar resistive switching with forming-free and self-rectifying efects in Cu/HfO2/n-Si devices"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I8777["Wang, M. J."], I61519["Gao, S."], I89808["Zeng, F."], I73802["Song, C."], I63079["Pan, F."]],
    ag__R8434__has_title="Unipolar resistive switching with forming-free and self-rectifying efects in Cu/HfO2/n-Si devices",
    ag__R8435__has_year=2016,
    R11809__has_memristor_stack=I3236["Cu/HfO2/n-Si"],
    
)


# 2019_xia 
I97154["Kim, K.-H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kim, K.-H.",
    
)


# 2019_xia 
I84376["Jo, S. H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Jo, S. H.",
    
)


# 2019_xia 
I72298["Gaba, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Gaba, S.",
    
)


# 2019_xia 
I34559["Lu, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Lu, W.",
    
)


# 2019_xia 
I83048["publication: Nanoscale resistive memory with intrinsic diode characteristics and long endurance"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I97154["Kim, K.-H."], I84376["Jo, S. H."], I72298["Gaba, S."], I34559["Lu, W."]],
    ag__R8434__has_title="Nanoscale resistive memory with intrinsic diode characteristics and long endurance",
    ag__R8435__has_year=2010,
    R11809__has_memristor_stack=I95705["Ag/a-Si/p-poly-Si"],
    
)


# 2019_xia 
I71732["Ni/TiO2/Ni"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I71732["Ni/TiO2/Ni"].set_relation(R48517["has stack component"], omt.I87636["nickel"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I71732["Ni/TiO2/Ni"].set_relation(R48517["has stack component"], omt.I87636["nickel"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I71732["Ni/TiO2/Ni"].set_relation(R48517["has stack component"], omt.I6119["TiO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_xia 
I16765["Pt/TiO2/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I16765["Pt/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I16765["Pt/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6119["TiO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I16765["Pt/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019_xia 
I18578["TiN/Ta2O5/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I18578["TiN/Ta2O5/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I18578["TiN/Ta2O5/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I18578["TiN/Ta2O5/TiN"].set_relation(R48517["has stack component"], omt.I6123["Ta2O5"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_xia 



# 2019_xia 
I87992["W/Ta2O5/TaOx/TiO2/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I87992["W/Ta2O5/TaOx/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I41958["tungsten"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I87992["W/Ta2O5/TaOx/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6123["Ta2O5"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I87992["W/Ta2O5/TaOx/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I87992["W/Ta2O5/TaOx/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6119["TiO2"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I87992["W/Ta2O5/TaOx/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(4), is_at_outer_position(True), ])


# 2019_xia 
I44440["Pt/TaOx/TiO2/TaOx/Pt"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I44440["Pt/TaOx/TiO2/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I44440["Pt/TaOx/TiO2/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(4), is_at_outer_position(True), ])
I44440["Pt/TaOx/TiO2/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I44440["Pt/TaOx/TiO2/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I44440["Pt/TaOx/TiO2/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I6119["TiO2"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019_xia 
I58468["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I58468["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I58468["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(4), is_at_outer_position(True), ])
I58468["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"].set_relation(R48517["has stack component"], omt.I6124["TaN1+x"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I58468["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"].set_relation(R48517["has stack component"], omt.I6124["TaN1+x"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I58468["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"].set_relation(R48517["has stack component"], omt.I6123["Ta2O5"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019_xia 



# 2019_xia 
I47470["TaN/SiNx/TaN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I47470["TaN/SiNx/TaN"].set_relation(R48517["has stack component"], omt.I6125["TaN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I47470["TaN/SiNx/TaN"].set_relation(R48517["has stack component"], omt.I6125["TaN"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I47470["TaN/SiNx/TaN"].set_relation(R48517["has stack component"], omt.I6126["SiNx"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_xia 



# 2019_xia 
I82062["TiN/GexSe1-x/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I82062["TiN/GexSe1-x/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I82062["TiN/GexSe1-x/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I82062["TiN/GexSe1-x/TiN"].set_relation(R48517["has stack component"], omt.I6130["GexSe1-x"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_xia 
omt.I6130["GexSe1-x"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019_xia 
I58157["TiN/As:SiO2/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I58157["TiN/As:SiO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I58157["TiN/As:SiO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I58157["TiN/As:SiO2/TiN"].set_relation(R48517["has stack component"], omt.I6131["As:SiO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_xia 
omt.I6131["As:SiO2"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019_xia 
I27966["Pt/VO2/Pt"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I27966["Pt/VO2/Pt"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I27966["Pt/VO2/Pt"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I27966["Pt/VO2/Pt"].set_relation(R48517["has stack component"], omt.I6132["VO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_xia 



# 2019_xia 
I21352["TiN/NbO2/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I21352["TiN/NbO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I21352["TiN/NbO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I21352["TiN/NbO2/TiN"].set_relation(R48517["has stack component"], omt.I6133["NbO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_xia 



# 2019_xia 
I46285["TiN/NbO2/W"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I46285["TiN/NbO2/W"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I46285["TiN/NbO2/W"].set_relation(R48517["has stack component"], omt.I6133["NbO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I46285["TiN/NbO2/W"].set_relation(R48517["has stack component"], omt.I41958["tungsten"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019_xia 
I6912["TiN/AsTeGeSiN/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I6912["TiN/AsTeGeSiN/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I6912["TiN/AsTeGeSiN/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I6912["TiN/AsTeGeSiN/TiN"].set_relation(R48517["has stack component"], omt.I6149["AsTeGeSiN"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_xia 



# 2019_xia 
I26347["W/Ag/MgO/Ag/W"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I26347["W/Ag/MgO/Ag/W"].set_relation(R48517["has stack component"], omt.I41958["tungsten"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I26347["W/Ag/MgO/Ag/W"].set_relation(R48517["has stack component"], omt.I41958["tungsten"], qualifiers=[has_position(4), is_at_outer_position(True), ])
I26347["W/Ag/MgO/Ag/W"].set_relation(R48517["has stack component"], omt.I93439["silver"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I26347["W/Ag/MgO/Ag/W"].set_relation(R48517["has stack component"], omt.I93439["silver"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I26347["W/Ag/MgO/Ag/W"].set_relation(R48517["has stack component"], omt.I6135["MgO"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019_xia 



# 2019_xia 



# 2019_xia 
I24977["Pt/Ag:SiOxNy/Pt"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I24977["Pt/Ag:SiOxNy/Pt"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I24977["Pt/Ag:SiOxNy/Pt"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I24977["Pt/Ag:SiOxNy/Pt"].set_relation(R48517["has stack component"], omt.I6150["Ag:SiOxNy"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_xia 
omt.I6150["Ag:SiOxNy"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019_xia 
I9309["Pd/Ag/HfO2/Ag/Pd"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I9309["Pd/Ag/HfO2/Ag/Pd"].set_relation(R48517["has stack component"], omt.I60065["palladium"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I9309["Pd/Ag/HfO2/Ag/Pd"].set_relation(R48517["has stack component"], omt.I60065["palladium"], qualifiers=[has_position(4), is_at_outer_position(True), ])
I9309["Pd/Ag/HfO2/Ag/Pd"].set_relation(R48517["has stack component"], omt.I93439["silver"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I9309["Pd/Ag/HfO2/Ag/Pd"].set_relation(R48517["has stack component"], omt.I93439["silver"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I9309["Pd/Ag/HfO2/Ag/Pd"].set_relation(R48517["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019_xia 



# 2019_xia 
I93983["TiN/Al2O3/TiO2/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I93983["TiN/Al2O3/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I93983["TiN/Al2O3/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I93983["TiN/Al2O3/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6100["Al2O3"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I93983["TiN/Al2O3/TiO2/TiN"].set_relation(R48517["has stack component"], omt.I6119["TiO2"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019_xia 
I18158["W/VOx/Pt"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I18158["W/VOx/Pt"].set_relation(R48517["has stack component"], omt.I41958["tungsten"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I18158["W/VOx/Pt"].set_relation(R48517["has stack component"], omt.I6140["VOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I18158["W/VOx/Pt"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019_xia 



# 2019_xia 
I63066["p-Si/SiO2/n-Si"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I63066["p-Si/SiO2/n-Si"].set_relation(R48517["has stack component"], omt.I6141["p-Si"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I63066["p-Si/SiO2/n-Si"].set_relation(R48517["has stack component"], omt.I6111["SiO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I63066["p-Si/SiO2/n-Si"].set_relation(R48517["has stack component"], omt.I6142["n-Si"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019_xia 
omt.I6141["p-Si"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019_xia 



# 2019_xia 
omt.I6142["n-Si"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019_xia 
I55774["Ni/HfO2/n-Si"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I55774["Ni/HfO2/n-Si"].set_relation(R48517["has stack component"], omt.I87636["nickel"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I55774["Ni/HfO2/n-Si"].set_relation(R48517["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I55774["Ni/HfO2/n-Si"].set_relation(R48517["has stack component"], omt.I6142["n-Si"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019_xia 
I3236["Cu/HfO2/n-Si"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I3236["Cu/HfO2/n-Si"].set_relation(R48517["has stack component"], omt.I23950["copper"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I3236["Cu/HfO2/n-Si"].set_relation(R48517["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I3236["Cu/HfO2/n-Si"].set_relation(R48517["has stack component"], omt.I6142["n-Si"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019_xia 



# 2019_xia 
I95705["Ag/a-Si/p-poly-Si"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I95705["Ag/a-Si/p-poly-Si"].set_relation(R48517["has stack component"], omt.I93439["silver"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I95705["Ag/a-Si/p-poly-Si"].set_relation(R48517["has stack component"], omt.I6143["a-Si"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I95705["Ag/a-Si/p-poly-Si"].set_relation(R48517["has stack component"], omt.I6144["p-poly-Si"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019_xia 
omt.I6143["a-Si"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2019_xia 
omt.I6144["p-poly-Si"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2024_aguirre 
I78145["publication: Hardware implementation of memristorbased artificial neural networks"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=["Fernando Aguirre", "Abu Sebastian"],
    ag__R8434__has_title="Hardware implementation of memristorbased artificial neural networks",
    ag__R8435__has_year=2024,
    R68407__has_internal_reference="2024_aguirre_et_al",
    
)
I78145["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I98801["publication: Fully hardware-implemented memristor convolutional neural network"], qualifiers=[has_citation_id(55), ])
I78145["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I47520["publication: A fully integrated reprogrammable memristor-CMOS system for efficient multiply-accumulate operations"], qualifiers=[has_citation_id(57), ])
I78145["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I79160["publication: A compute-in-memory chip based on resistive random-access memory"], qualifiers=[has_citation_id(60), ])
I78145["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I10094["publication: A 4M synapses integrated analog ReRAM based 66.5 TOPS/W neural-network processor with cell current controlled writing and flexible network architecture"], qualifiers=[has_citation_id(99), ])
I78145["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I42033["publication: A 462GOPs/J RRAM-based nonvolatile intelligent processor for energy harvesting IoE system featuring nonvolatile logics and processing-in-memory"], qualifiers=[has_citation_id(100), ])
I78145["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I29098["publication: A fully hardware-based memristive multilayer neural network"], qualifiers=[has_citation_id(102), ])
I78145["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I82346["publication: CMOS-integrated nanoscale memristive crossbars for CNN and optimization acceleration"], qualifiers=[has_citation_id(113), ])
I78145["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I88962["publication: Redundancy and analog slicing for precise inmemory machine learning - Part I: Programming techniques"], qualifiers=[has_citation_id(114), ])
I78145["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I12398["publication: Redundancy and analog slicing for precise inmemory machine learning - Part II: Applications and benchmark"], qualifiers=[has_citation_id(115), ])
I78145["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I33364["publication: Fully memristive neural networks for pattern classification with unsupervised learning"], qualifiers=[has_citation_id(116), ])
I78145["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I98878["publication: In-memory and error-immune differential RRAM implementation of binarized deep neural networks"], qualifiers=[has_citation_id(123), ])
I78145["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I23249["publication: CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors"], qualifiers=[has_citation_id(219), ])
I78145["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I76087["publication: Digital biologically plausible implementation of binarized neural networks with differential hafnium oxide resistive memory arrays"], qualifiers=[has_citation_id(272), ])
I78145["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I61398["publication: A 43pJ/Cycle Non-Volatile Microcontroller with 4.7μs Shutdown/Wake-up Integrating 2.3-bit/Cell Resistive RAM and Resilience Techniques"], qualifiers=[has_citation_id(274), ])


# 2024_aguirre 
I93419["Yao, P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Yao, P.",
    
)


# 2024_aguirre 
I98801["publication: Fully hardware-implemented memristor convolutional neural network"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I93419["Yao, P."],
    ag__R8434__has_title="Fully hardware-implemented memristor convolutional neural network",
    ag__R8435__has_year=2020,
    R11809__has_memristor_stack=I28976["TiN/TaOx/HfOx/TiN"],
    
)


# 2024_aguirre 
I11520["Cai, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Cai, F.",
    
)


# 2024_aguirre 
I47520["publication: A fully integrated reprogrammable memristor-CMOS system for efficient multiply-accumulate operations"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I11520["Cai, F."],
    ag__R8434__has_title="A fully integrated reprogrammable memristor-CMOS system for efficient multiply-accumulate operations",
    ag__R8435__has_year=2019,
    R11809__has_memristor_stack=I99103["Au/Pd/WOx/Au"],
    
)


# 2024_aguirre 
I59694["Wan, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wan, W.",
    
)


# 2024_aguirre 
I79160["publication: A compute-in-memory chip based on resistive random-access memory"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I59694["Wan, W."],
    ag__R8434__has_title="A compute-in-memory chip based on resistive random-access memory",
    ag__R8435__has_year=2022,
    R11809__has_memristor_stack=I47202["TiN/HfO2/TaOx/TiN"],
    
)


# 2024_aguirre 
I56829["Mochida, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Mochida, R.",
    
)


# 2024_aguirre 
I10094["publication: A 4M synapses integrated analog ReRAM based 66.5 TOPS/W neural-network processor with cell current controlled writing and flexible network architecture"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I56829["Mochida, R."],
    ag__R8434__has_title="A 4M synapses integrated analog ReRAM based 66.5 TOPS/W neural-network processor with cell current controlled writing and flexible network architecture",
    ag__R8435__has_year=2018,
    R11809__has_memristor_stack=I61689["W/Ta2O5/TaOx/W"],
    
)


# 2024_aguirre 
I33159["Su, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Su, F.",
    
)


# 2024_aguirre 
I42033["publication: A 462GOPs/J RRAM-based nonvolatile intelligent processor for energy harvesting IoE system featuring nonvolatile logics and processing-in-memory"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I33159["Su, F."],
    ag__R8434__has_title="A 462GOPs/J RRAM-based nonvolatile intelligent processor for energy harvesting IoE system featuring nonvolatile logics and processing-in-memory",
    ag__R8435__has_year=2017,
    R11809__has_memristor_stack=I37167["AlCu/TiN/Ti/HfO2/TiN"],
    
)


# 2024_aguirre 
I92000["Kiani, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kiani, F.",
    
)


# 2024_aguirre 
I7940["Yin, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Yin, J.",
    
)


# 2024_aguirre 
I69530["Joshua Yang, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Joshua Yang, J.",
    
)


# 2024_aguirre 
I68259["Xia, Q."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Xia, Q.",
    
)


# 2024_aguirre 
I29098["publication: A fully hardware-based memristive multilayer neural network"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I92000["Kiani, F."], I7940["Yin, J."], I10778["Wang, Z."], I69530["Joshua Yang, J."], I68259["Xia, Q."]],
    ag__R8434__has_title="A fully hardware-based memristive multilayer neural network",
    ag__R8435__has_year=2021,
    R11809__has_memristor_stack=I66639["Pt/Ta/Ta2O5/Pt/Ti"],
    
)


# 2024_aguirre 
I82346["publication: CMOS-integrated nanoscale memristive crossbars for CNN and optimization acceleration"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I70494["Li, C."],
    ag__R8434__has_title="CMOS-integrated nanoscale memristive crossbars for CNN and optimization acceleration",
    ag__R8435__has_year=2020,
    R11809__has_memristor_stack=I34380["Ta/TaOx/Pt"],
    
)


# 2024_aguirre 
I90071["Pedretti, G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Pedretti, G.",
    
)


# 2024_aguirre 
I88962["publication: Redundancy and analog slicing for precise inmemory machine learning - Part I: Programming techniques"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I90071["Pedretti, G."],
    ag__R8434__has_title="Redundancy and analog slicing for precise inmemory machine learning - Part I: Programming techniques",
    ag__R8435__has_year=2021,
    
)


# 2024_aguirre 
I12398["publication: Redundancy and analog slicing for precise inmemory machine learning - Part II: Applications and benchmark"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I90071["Pedretti, G."],
    ag__R8434__has_title="Redundancy and analog slicing for precise inmemory machine learning - Part II: Applications and benchmark",
    ag__R8435__has_year=2021,
    
)


# 2024_aguirre 
I33364["publication: Fully memristive neural networks for pattern classification with unsupervised learning"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I10778["Wang, Z."],
    ag__R8434__has_title="Fully memristive neural networks for pattern classification with unsupervised learning",
    ag__R8435__has_year=2018,
    R11809__has_memristor_stack=[I11681["Pt/SiOxAg/Pt/Ti"], I41069["Ta/Pd/HfO2/Pt/Ti"]],
    
)


# 2024_aguirre 
I8173["Bocquet, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Bocquet, M.",
    
)


# 2024_aguirre 
I98878["publication: In-memory and error-immune differential RRAM implementation of binarized deep neural networks"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I8173["Bocquet, M."],
    ag__R8434__has_title="In-memory and error-immune differential RRAM implementation of binarized deep neural networks",
    ag__R8435__has_year=2018,
    R11809__has_memristor_stack=I5868["TiN/HfO2/Ti/TiN"],
    
)


# 2024_aguirre 
I76458["Chen, W. H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Chen, W. H.",
    
)


# 2024_aguirre 
I23249["publication: CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I76458["Chen, W. H."],
    ag__R8434__has_title="CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors",
    ag__R8435__has_year=2019,
    R11809__has_memristor_stack=I37464["W/TiN/TiON"],
    
)


# 2024_aguirre 
I38620["Hirtzlin, T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Hirtzlin, T.",
    
)


# 2024_aguirre 
I76087["publication: Digital biologically plausible implementation of binarized neural networks with differential hafnium oxide resistive memory arrays"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I38620["Hirtzlin, T."],
    ag__R8434__has_title="Digital biologically plausible implementation of binarized neural networks with differential hafnium oxide resistive memory arrays",
    ag__R8435__has_year=2020,
    R11809__has_memristor_stack=I5868["TiN/HfO2/Ti/TiN"],
    
)


# 2024_aguirre 
I48237["Wu, T. F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wu, T. F.",
    
)


# 2024_aguirre 
I61398["publication: A 43pJ/Cycle Non-Volatile Microcontroller with 4.7μs Shutdown/Wake-up Integrating 2.3-bit/Cell Resistive RAM and Resilience Techniques"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I48237["Wu, T. F."],
    ag__R8434__has_title="A 43pJ/Cycle Non-Volatile Microcontroller with 4.7μs Shutdown/Wake-up Integrating 2.3-bit/Cell Resistive RAM and Resilience Techniques",
    ag__R8435__has_year=2019,
    R11809__has_memristor_stack=I5868["TiN/HfO2/Ti/TiN"],
    
)


# 2024_aguirre 
I99103["Au/Pd/WOx/Au"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I99103["Au/Pd/WOx/Au"].set_relation(R48517["has stack component"], omt.I54426["gold"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I99103["Au/Pd/WOx/Au"].set_relation(R48517["has stack component"], omt.I54426["gold"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I99103["Au/Pd/WOx/Au"].set_relation(R48517["has stack component"], omt.I60065["palladium"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I99103["Au/Pd/WOx/Au"].set_relation(R48517["has stack component"], omt.I6146["WOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2024_aguirre 



# 2024_aguirre 



# 2024_aguirre 
I28976["TiN/TaOx/HfOx/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I28976["TiN/TaOx/HfOx/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I28976["TiN/TaOx/HfOx/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I28976["TiN/TaOx/HfOx/TiN"].set_relation(R48517["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I28976["TiN/TaOx/HfOx/TiN"].set_relation(R48517["has stack component"], omt.I6105["HfOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2024_aguirre 
I66639["Pt/Ta/Ta2O5/Pt/Ti"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I66639["Pt/Ta/Ta2O5/Pt/Ti"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I66639["Pt/Ta/Ta2O5/Pt/Ti"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I66639["Pt/Ta/Ta2O5/Pt/Ti"].set_relation(R48517["has stack component"], omt.I38968["tantalum"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I66639["Pt/Ta/Ta2O5/Pt/Ti"].set_relation(R48517["has stack component"], omt.I6123["Ta2O5"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I66639["Pt/Ta/Ta2O5/Pt/Ti"].set_relation(R48517["has stack component"], omt.I87594["titanium"], qualifiers=[has_position(4), is_at_outer_position(True), ])


# 2024_aguirre 
I34380["Ta/TaOx/Pt"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I34380["Ta/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I38968["tantalum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I34380["Ta/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I34380["Ta/TaOx/Pt"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2024_aguirre 
I37464["W/TiN/TiON"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I37464["W/TiN/TiON"].set_relation(R48517["has stack component"], omt.I41958["tungsten"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I37464["W/TiN/TiON"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I37464["W/TiN/TiON"].set_relation(R48517["has stack component"], omt.I6147["TiON"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2024_aguirre 



# 2024_aguirre 
I11681["Pt/SiOxAg/Pt/Ti"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I11681["Pt/SiOxAg/Pt/Ti"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I11681["Pt/SiOxAg/Pt/Ti"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I11681["Pt/SiOxAg/Pt/Ti"].set_relation(R48517["has stack component"], omt.I6151["SiOxAg"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I11681["Pt/SiOxAg/Pt/Ti"].set_relation(R48517["has stack component"], omt.I87594["titanium"], qualifiers=[has_position(3), is_at_outer_position(True), ])


# 2024_aguirre 
omt.I6151["SiOxAg"].update_relations(
    R4__is_instance_of=I99429["stack component"],
    
)


# 2024_aguirre 
I41069["Ta/Pd/HfO2/Pt/Ti"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I41069["Ta/Pd/HfO2/Pt/Ti"].set_relation(R48517["has stack component"], omt.I38968["tantalum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I41069["Ta/Pd/HfO2/Pt/Ti"].set_relation(R48517["has stack component"], omt.I60065["palladium"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I41069["Ta/Pd/HfO2/Pt/Ti"].set_relation(R48517["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I41069["Ta/Pd/HfO2/Pt/Ti"].set_relation(R48517["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I41069["Ta/Pd/HfO2/Pt/Ti"].set_relation(R48517["has stack component"], omt.I87594["titanium"], qualifiers=[has_position(4), is_at_outer_position(True), ])


# 2024_aguirre 
I5868["TiN/HfO2/Ti/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I5868["TiN/HfO2/Ti/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I5868["TiN/HfO2/Ti/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I5868["TiN/HfO2/Ti/TiN"].set_relation(R48517["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I5868["TiN/HfO2/Ti/TiN"].set_relation(R48517["has stack component"], omt.I87594["titanium"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2024_aguirre 
I61689["W/Ta2O5/TaOx/W"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I61689["W/Ta2O5/TaOx/W"].set_relation(R48517["has stack component"], omt.I41958["tungsten"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I61689["W/Ta2O5/TaOx/W"].set_relation(R48517["has stack component"], omt.I41958["tungsten"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I61689["W/Ta2O5/TaOx/W"].set_relation(R48517["has stack component"], omt.I6123["Ta2O5"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I61689["W/Ta2O5/TaOx/W"].set_relation(R48517["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2024_aguirre 
I37167["AlCu/TiN/Ti/HfO2/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I37167["AlCu/TiN/Ti/HfO2/TiN"].set_relation(R48517["has stack component"], omt.I6148["AlCu"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I37167["AlCu/TiN/Ti/HfO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I37167["AlCu/TiN/Ti/HfO2/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(4), is_at_outer_position(True), ])
I37167["AlCu/TiN/Ti/HfO2/TiN"].set_relation(R48517["has stack component"], omt.I87594["titanium"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I37167["AlCu/TiN/Ti/HfO2/TiN"].set_relation(R48517["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(3), is_at_outer_position(False), ])


# 2024_aguirre 



# 2024_aguirre 
I47202["TiN/HfO2/TaOx/TiN"].update_relations(
    R4__is_instance_of=I40233["memristor stack"],
    
)
I47202["TiN/HfO2/TaOx/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I47202["TiN/HfO2/TaOx/TiN"].set_relation(R48517["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I47202["TiN/HfO2/TaOx/TiN"].set_relation(R48517["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I47202["TiN/HfO2/TaOx/TiN"].set_relation(R48517["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])




p.end_mod()