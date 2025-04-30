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
I1623 = p.create_item(R1__has_label="memristor stack")
I86037 = p.create_item(R1__has_label="stack component")
R66928 = p.create_relation(R1__has_label="has stack component")
R61856 = p.create_relation(R1__has_label="has memristor stack")
R34871 = p.create_relation(R1__has_label="has position")
R17110 = p.create_relation(R1__has_label="is at outer position")
R49997 = p.create_relation(R1__has_label="has citation id")
R14118 = p.create_relation(R1__has_label="has internal reference")
I98213 = p.create_item(R1__has_label="Mario Lanza")
I9301 = p.create_item(R1__has_label="H.-S. Philip Wong")
I68330 = p.create_item(R1__has_label="Eric Pop")
I12749 = p.create_item(R1__has_label="Daniele Ielmini")
I38831 = p.create_item(R1__has_label="Dimitri Strukov")
I45494 = p.create_item(R1__has_label="Brian C. Regan")
I47996 = p.create_item(R1__has_label="Luca Larcher")
I52583 = p.create_item(R1__has_label="Marco A. Villena")
I35079 = p.create_item(R1__has_label="J. Joshua Yang")
I10148 = p.create_item(R1__has_label="Ludovic Goux")
I35068 = p.create_item(R1__has_label="Attilio Belmonte")
I60959 = p.create_item(R1__has_label="Yuchao Yang")
I42597 = p.create_item(R1__has_label="Francesco M. Puglisi")
I81302 = p.create_item(R1__has_label="Jinfeng Kang")
I11032 = p.create_item(R1__has_label="Blanka Magyari-Köpe")
I61436 = p.create_item(R1__has_label="Eilam Yalon")
I18300 = p.create_item(R1__has_label="Anthony Kenyon")
I35023 = p.create_item(R1__has_label="Mark Buckwell")
I95103 = p.create_item(R1__has_label="Adnan Mehonic")
I67772 = p.create_item(R1__has_label="Alexander Shluger")
I66816 = p.create_item(R1__has_label="Haitong Li")
I89938 = p.create_item(R1__has_label="Tuo-Hung Hou")
I71699 = p.create_item(R1__has_label="Boris Hudec")
I4407 = p.create_item(R1__has_label="Deji Akinwande")
I94278 = p.create_item(R1__has_label="Ruijing Ge")
I81075 = p.create_item(R1__has_label="Stefano Ambrogio")
I17336 = p.create_item(R1__has_label="Juan B. Roldan")
I3089 = p.create_item(R1__has_label="Enrique Miranda")
I95679 = p.create_item(R1__has_label="Jordi Suñe")
I22719 = p.create_item(R1__has_label="Kin Leong Pey")
I36951 = p.create_item(R1__has_label="Xing Wu")
I31551 = p.create_item(R1__has_label="Nagarajan Raghavan")
I70878 = p.create_item(R1__has_label="Ernest Wu")
I9426 = p.create_item(R1__has_label="Wei D. Lu")
I94216 = p.create_item(R1__has_label="Gabriele Navarro")
I43418 = p.create_item(R1__has_label="Weidong Zhang")
I78330 = p.create_item(R1__has_label="Huaqiang Wu")
I84818 = p.create_item(R1__has_label="Runwei Li")
I31142 = p.create_item(R1__has_label="Alexander Holleitner")
I74019 = p.create_item(R1__has_label="Ursula Wurstbauer")
I83705 = p.create_item(R1__has_label="Max C. Lemme")
I19231 = p.create_item(R1__has_label="Ming Liu")
I72904 = p.create_item(R1__has_label="Shibing Long")
I26214 = p.create_item(R1__has_label="Qi Liu")
I56137 = p.create_item(R1__has_label="Hangbing Lv")
I15966 = p.create_item(R1__has_label="Andrea Padovani")
I42377 = p.create_item(R1__has_label="Paolo Pavan")
I88305 = p.create_item(R1__has_label="Ilia Valov")
I41974 = p.create_item(R1__has_label="Xu Jing")
I75108 = p.create_item(R1__has_label="Tingting Han")
I18859 = p.create_item(R1__has_label="Kaichen Zhu")
I80129 = p.create_item(R1__has_label="Shaochuan Chen")
I55623 = p.create_item(R1__has_label="Fei Hui")
I27380 = p.create_item(R1__has_label="Yuanyuan Shi")
I6779 = p.create_item(R1__has_label="publication: Recommended Methods to Study Resistive Switching Devices")
I89114 = p.create_item(R1__has_label="H. Y. Lee")
I85415 = p.create_item(R1__has_label="Y. S. Chen")
I71318 = p.create_item(R1__has_label="P. S. Chen")
I40045 = p.create_item(R1__has_label="P. Y. Gu")
I78072 = p.create_item(R1__has_label="Y. Y. Hsu")
I17406 = p.create_item(R1__has_label="S. M. Wang")
I70034 = p.create_item(R1__has_label="W. H. Liu")
I82691 = p.create_item(R1__has_label="C. H. Tsai")
I67208 = p.create_item(R1__has_label="S. S. Sheu")
I29245 = p.create_item(R1__has_label="P. C. Chiang")
I84274 = p.create_item(R1__has_label="W. P. Lin")
I97898 = p.create_item(R1__has_label="C. H. Lin")
I55841 = p.create_item(R1__has_label="W. S. Chen")
I63187 = p.create_item(R1__has_label="F. T. Chen")
I50200 = p.create_item(R1__has_label="C. H. Lien")
I97039 = p.create_item(R1__has_label="M. J. Tsai")
I26917 = p.create_item(R1__has_label="publication: IEEE Int. Electron Devices Meet.")
I15997 = p.create_item(R1__has_label="B. Govoreanu")
I85412 = p.create_item(R1__has_label="G. S. Kar")
I77477 = p.create_item(R1__has_label="Y-Y. Chen")
I73058 = p.create_item(R1__has_label="V. Paraschiv")
I32600 = p.create_item(R1__has_label="S. Kubicek")
I49732 = p.create_item(R1__has_label="A. Fantini")
I16948 = p.create_item(R1__has_label="I. P. Radu")
I22825 = p.create_item(R1__has_label="L. Goux")
I6679 = p.create_item(R1__has_label="S. Clima")
I61031 = p.create_item(R1__has_label="R. Degraeve")
I35393 = p.create_item(R1__has_label="N. Jossart")
I26269 = p.create_item(R1__has_label="O. Richard")
I69444 = p.create_item(R1__has_label="T. Vandeweyer")
I20147 = p.create_item(R1__has_label="K. Seo")
I76671 = p.create_item(R1__has_label="P. Hendrickx")
I4936 = p.create_item(R1__has_label="G. Pourtois")
I26714 = p.create_item(R1__has_label="H. Bender")
I15948 = p.create_item(R1__has_label="L. Altimime")
I72220 = p.create_item(R1__has_label="D. J. Wouters")
I68261 = p.create_item(R1__has_label="J. A. Kittl")
I51128 = p.create_item(R1__has_label="M. Jurczak")
I22086 = p.create_item(R1__has_label="publication: No title given 25631219101")
I77371 = p.create_item(R1__has_label="J. J. Yang")
I20407 = p.create_item(R1__has_label="M.-X. Zhang")
I43423 = p.create_item(R1__has_label="J. P. Strachan")
I13119 = p.create_item(R1__has_label="F. Miao")
I17638 = p.create_item(R1__has_label="M. D. Pickett")
I74490 = p.create_item(R1__has_label="R. D. Kelley")
I42047 = p.create_item(R1__has_label="G. Medeiros-Ribeiro")
I26624 = p.create_item(R1__has_label="R. S. Williams")
I50709 = p.create_item(R1__has_label="publication: Appl. Phys. Lett.")
I31489 = p.create_item(R1__has_label="M. J. Lee")
I4668 = p.create_item(R1__has_label="C. B. Lee")
I97883 = p.create_item(R1__has_label="D. S. Lee")
I35402 = p.create_item(R1__has_label="S. R. Lee")
I33313 = p.create_item(R1__has_label="M. Chang")
I83787 = p.create_item(R1__has_label="J. H. Hur")
I39495 = p.create_item(R1__has_label="Y. B. Kim")
I91911 = p.create_item(R1__has_label="C. J. Kim")
I48432 = p.create_item(R1__has_label="D. H. Seo")
I3263 = p.create_item(R1__has_label="S. Seo")
I40069 = p.create_item(R1__has_label="U. I. Chung")
I11297 = p.create_item(R1__has_label="I. K. Yoo")
I35953 = p.create_item(R1__has_label="K. Kim")
I83289 = p.create_item(R1__has_label="publication: Nat. Mater.")
I81467 = p.create_item(R1__has_label="I G. Baek")
I78347 = p.create_item(R1__has_label="M. S. Lee")
I2120 = p.create_item(R1__has_label="D. S. Suh")
I32499 = p.create_item(R1__has_label="J. C. Park")
I12382 = p.create_item(R1__has_label="S. O. Park")
I91222 = p.create_item(R1__has_label="H. S. Kim")
I8497 = p.create_item(R1__has_label="J. T. Moon")
I19447 = p.create_item(R1__has_label="publication: presented at *IEEE Int. Electron Device Meet.*")
I8318 = p.create_item(R1__has_label="C. H. Cheng")
I19405 = p.create_item(R1__has_label="A. Chin")
I76726 = p.create_item(R1__has_label="F. S. Yeh")
I1159 = p.create_item(R1__has_label="publication: Symp. VLSI Technol.")
I79242 = p.create_item(R1__has_label="Z. Wei")
I37274 = p.create_item(R1__has_label="Y. Kanzawa")
I23890 = p.create_item(R1__has_label="K. Arita")
I66877 = p.create_item(R1__has_label="Y. Katoh")
I1523 = p.create_item(R1__has_label="K. Kawai")
I28497 = p.create_item(R1__has_label="S. Muraoka")
I32191 = p.create_item(R1__has_label="S. Mitani")
I29406 = p.create_item(R1__has_label="S. Fujii")
I30039 = p.create_item(R1__has_label="K. Katayama")
I95692 = p.create_item(R1__has_label="M. Iijima")
I90836 = p.create_item(R1__has_label="T. Mikawa")
I69967 = p.create_item(R1__has_label="T. Ninomiya")
I85895 = p.create_item(R1__has_label="R. Miyanaga")
I71924 = p.create_item(R1__has_label="Y. Kawashima")
I97779 = p.create_item(R1__has_label="K. Tsuji")
I50815 = p.create_item(R1__has_label="A. Himeno")
I35590 = p.create_item(R1__has_label="T. Okada")
I2968 = p.create_item(R1__has_label="R. Azuma")
I75800 = p.create_item(R1__has_label="K. Shimakawa")
I26378 = p.create_item(R1__has_label="H. Sugaya")
I59962 = p.create_item(R1__has_label="T. Takagi")
I93041 = p.create_item(R1__has_label="R. Yasuhara")
I39016 = p.create_item(R1__has_label="K. Horiba")
I42747 = p.create_item(R1__has_label="H. Kumigashira")
I34150 = p.create_item(R1__has_label="M. Oshima")
I69142 = p.create_item(R1__has_label="publication: presented at *IEEE IEDM*")
I60173 = p.create_item(R1__has_label="L. G. Wang")
I31595 = p.create_item(R1__has_label="X. Qian")
I85919 = p.create_item(R1__has_label="Y. Q. Cao")
I38439 = p.create_item(R1__has_label="Z. Y. Cao")
I79583 = p.create_item(R1__has_label="G. Y. Fang")
I92231 = p.create_item(R1__has_label="A. D. Li")
I47075 = p.create_item(R1__has_label="D. Wu")
I36455 = p.create_item(R1__has_label="publication: No title given 41246013015")
I64442 = p.create_item(R1__has_label="H.-S. P. Wong")
I46737 = p.create_item(R1__has_label="S. Yu")
I55336 = p.create_item(R1__has_label="Y. Wu")
I74558 = p.create_item(R1__has_label="B. Lee")
I88157 = p.create_item(R1__has_label="publication: No title given 28138552030")
I76467 = p.create_item(R1__has_label="M. C. Wu")
I32160 = p.create_item(R1__has_label="Y. W. Lin")
I59566 = p.create_item(R1__has_label="W. Y. Jang")
I42835 = p.create_item(R1__has_label="T. Y. Tseng")
I3972 = p.create_item(R1__has_label="publication: IEEE Electron Device Lett.")
I99897 = p.create_item(R1__has_label="C. Ahn")
I3777 = p.create_item(R1__has_label="Z. Jiang")
I42701 = p.create_item(R1__has_label="C. S. Lee")
I70477 = p.create_item(R1__has_label="H. Y. Chen")
I8841 = p.create_item(R1__has_label="J. Liang")
I34548 = p.create_item(R1__has_label="L. S. Liyanage")
I8157 = p.create_item(R1__has_label="H. S. P. Wong")
I26216 = p.create_item(R1__has_label="publication: IEEE Trans. Electron Devices")
I2784 = p.create_item(R1__has_label="D. Lee")
I11276 = p.create_item(R1__has_label="G. S. Park")
I91141 = p.create_item(R1__has_label="U. Chung")
I20930 = p.create_item(R1__has_label="publication: 2011 Symp. on VLSI Technology - Digest of Technical Papers")
I30609 = p.create_item(R1__has_label="V. K. Nagareddy")
I89040 = p.create_item(R1__has_label="A. K. Ott")
I46623 = p.create_item(R1__has_label="C. Dou")
I59209 = p.create_item(R1__has_label="T. Tsvetkova")
I48506 = p.create_item(R1__has_label="M. Sandulov")
I49412 = p.create_item(R1__has_label="M. F. Craciun")
I66355 = p.create_item(R1__has_label="A. C. Ferrari")
I47721 = p.create_item(R1__has_label="C. D. Wright")
I65519 = p.create_item(R1__has_label="publication: No title given 26048021673")
I7018 = p.create_item(R1__has_label="X. Cao")
I58662 = p.create_item(R1__has_label="X. M. Li")
I83250 = p.create_item(R1__has_label="X. D. Gao")
I3155 = p.create_item(R1__has_label="W. D. Yu")
I47458 = p.create_item(R1__has_label="X. J. Liu")
I77727 = p.create_item(R1__has_label="Y. W. Zhang")
I62007 = p.create_item(R1__has_label="L. D. Chen")
I32629 = p.create_item(R1__has_label="X. H. Cheng")
I43431 = p.create_item(R1__has_label="publication: No title given 86846326096")
I70632 = p.create_item(R1__has_label="TiN/TiOx/HfOx/TiN")
I51049 = p.create_item(R1__has_label="Ti/ZrO2/Pt")
I78439 = p.create_item(R1__has_label="ZrO2")
I66262 = p.create_item(R1__has_label="TiN/Hf/HfOx/TiN")
I93962 = p.create_item(R1__has_label="Al/Ti/Al2O3/s-CNT")
I1292 = p.create_item(R1__has_label="s-CNT")
I19279 = p.create_item(R1__has_label="Pt/Ta2O5-x/TaO2-x/Pt")
I64653 = p.create_item(R1__has_label="Ta2O5-x")
I75462 = p.create_item(R1__has_label="TaO2-x")
I69260 = p.create_item(R1__has_label="Pt/TaOx/Pt")
I11158 = p.create_item(R1__has_label="Ta/TaOx/TiO2/Ti")
I11140 = p.create_item(R1__has_label="Pt/TaOx/Ta")
I54529 = p.create_item(R1__has_label="W/AlO/TaOx/ZrOx/Ru")
I13510 = p.create_item(R1__has_label="AlO")
I83785 = p.create_item(R1__has_label="ZrOx")
I68625 = p.create_item(R1__has_label="Pt/Al2O3/HfO2/Al2O3/TiN/Si")
I85511 = p.create_item(R1__has_label="TaN/TiN/Zr/HfO2/CAFM tip")
I30387 = p.create_item(R1__has_label="CAFM tip")
I71049 = p.create_item(R1__has_label="Ni/GeO/STO/TaN")
I28797 = p.create_item(R1__has_label="GeO")
I46363 = p.create_item(R1__has_label="STO")
I13696 = p.create_item(R1__has_label="Pt/Gd2O3/Pt")
I67113 = p.create_item(R1__has_label="Gd2O3")
I26235 = p.create_item(R1__has_label="Qiangfei Xia")
I95037 = p.create_item(R1__has_label="publication: Memristive crossbar arrays for brain-inspired computing")
I60603 = p.create_item(R1__has_label="Wang, Z.")
I21705 = p.create_item(R1__has_label="publication: Memristors with difusive dynamics as synaptic emulators for neuromorphic computing")
I71085 = p.create_item(R1__has_label="Li, C.")
I1628 = p.create_item(R1__has_label="publication: Tree-dimensional crossbar arrays of self-rectifying Si/SiO2/Si memristors")
I69074 = p.create_item(R1__has_label="Midya, R.")
I73950 = p.create_item(R1__has_label="publication: Anatomy of Ag/Hafnia-based selectors with 1010 nonlinearity")
I81200 = p.create_item(R1__has_label="Huang, J.-J.")
I15872 = p.create_item(R1__has_label="Tseng, Y.-M.")
I61127 = p.create_item(R1__has_label="Hsu, C.-W.")
I10492 = p.create_item(R1__has_label="Hou, T.-H.")
I75618 = p.create_item(R1__has_label="publication: Bipolar nonlinear Ni/ TiO2/Ni selector for 1S1R crossbar array applications")
I85787 = p.create_item(R1__has_label="Shin, J.")
I89338 = p.create_item(R1__has_label="publication: TiO2-based metal–insulator–metal selection device for bipolar resistive random access memory cross-point application")
I99774 = p.create_item(R1__has_label="Govoreanu, B.")
I73331 = p.create_item(R1__has_label="publication: High-performance metal–insulator–metal tunnel diode selectors")
I70578 = p.create_item(R1__has_label="Woo, J.")
I13672 = p.create_item(R1__has_label="publication: Electrical and reliability characteristics of a scaled (∼30nm) tunnel barrier selector (W/Ta2O5/TaOx/TiO2/TiN) with excellent performance (JMAX>107A/cm2)")
I98352 = p.create_item(R1__has_label="Lee, W.")
I82962 = p.create_item(R1__has_label="publication: Varistor-type bidirectional switch (JMAX>107A/cm2 , selectivity ∼104 ) for 3D bipolar resistive memory arrays")
I35052 = p.create_item(R1__has_label="Choi, B. J.")
I17370 = p.create_item(R1__has_label="publication: Trilayer tunnel selectors for memristor memory cells")
I34753 = p.create_item(R1__has_label="Kawahara, A.")
I97500 = p.create_item(R1__has_label="publication: An 8 Mb multi-layered cross-point ReRAM macro with 443 MB/s write throughput")
I13780 = p.create_item(R1__has_label="publication: Termally stable integrated Se-based OTS selectors with >20MA/cm2 current drive, >3.103 half-bias nonlinearity, tunable threshold voltage and excellent endurance")
I67979 = p.create_item(R1__has_label="Kim, S. G.")
I28644 = p.create_item(R1__has_label="publication: Breakthrough of selector technology for cross-point 25-nm ReRAM")
I89226 = p.create_item(R1__has_label="Son, M.")
I73977 = p.create_item(R1__has_label="publication: Excellent selector characteristics of nanoscale VO2 for high-density bipolar ReRAM applications")
I86966 = p.create_item(R1__has_label="Kim, W. G.")
I35602 = p.create_item(R1__has_label="publication: NbO2-based low power and cost efective 1S1R switching for high density cross point ReRAM application")
I48336 = p.create_item(R1__has_label="Cha, E.")
I67839 = p.create_item(R1__has_label="publication: Nanoscale (∼10nm) 3D vertical ReRAM and NbO2 threshold selector with TiN electrode")
I71990 = p.create_item(R1__has_label="Lee, M.-J.")
I49726 = p.create_item(R1__has_label="publication: Highly-scalable threshold switching select device based on chalcogenide glasses for 3D nanoscaled memory arrays")
I42524 = p.create_item(R1__has_label="Sun, J.")
I85749 = p.create_item(R1__has_label="publication: Physically transient threshold switching device based on magnesium oxide for security application")
I57207 = p.create_item(R1__has_label="Wang, G.")
I27754 = p.create_item(R1__has_label="publication: High‐performance and low‐power rewritable SiO*x* 1 kbit one diode–one resistor crossbar memory array")
I46324 = p.create_item(R1__has_label="publication: Vacancy-modulated conductive oxide resistive RAM (VMCO-RRAM): an area-scalable switching current, self-compliant, highly nonlinear and wide on/of-window resistive switching cell")
I10365 = p.create_item(R1__has_label="Song, M.")
I20852 = p.create_item(R1__has_label="publication: Self-selective characteristics of nanoscale VOx devices for high-density ReRAM applications")
I88598 = p.create_item(R1__has_label="Lu, D.")
I53525 = p.create_item(R1__has_label="publication: Investigations of conduction mechanisms of the self-rectifying n<sup>+</sup>Si-HfO2-Ni RRAM devices")
I67488 = p.create_item(R1__has_label="Wang, M. J.")
I30209 = p.create_item(R1__has_label="Gao, S.")
I92507 = p.create_item(R1__has_label="Zeng, F.")
I92352 = p.create_item(R1__has_label="Song, C.")
I87241 = p.create_item(R1__has_label="Pan, F.")
I4356 = p.create_item(R1__has_label="publication: Unipolar resistive switching with forming-free and self-rectifying efects in Cu/HfO2/n-Si devices")
I77819 = p.create_item(R1__has_label="Kim, K.-H.")
I39850 = p.create_item(R1__has_label="Jo, S. H.")
I58824 = p.create_item(R1__has_label="Gaba, S.")
I2160 = p.create_item(R1__has_label="Lu, W.")
I45125 = p.create_item(R1__has_label="publication: Nanoscale resistive memory with intrinsic diode characteristics and long endurance")
I2579 = p.create_item(R1__has_label="Ni/TiO2/Ni")
I25766 = p.create_item(R1__has_label="Pt/TiO2/TiN")
I53423 = p.create_item(R1__has_label="TiN/Ta2O5/TiN")
I16044 = p.create_item(R1__has_label="W/Ta2O5/TaOx/TiO2/TiN")
I89412 = p.create_item(R1__has_label="Pt/TaOx/TiO2/TaOx/Pt")
I37641 = p.create_item(R1__has_label="Pt/TaN1+x/Ta2O5/TaN1+x/Pt")
I14062 = p.create_item(R1__has_label="TaN/SiNx/TaN")
I20402 = p.create_item(R1__has_label="TiN/GexSe1-x/TiN")
I6089 = p.create_item(R1__has_label="TiN/As:SiO2/TiN")
I74560 = p.create_item(R1__has_label="Pt/VO2/Pt")
I48450 = p.create_item(R1__has_label="TiN/NbO2/TiN")
I35200 = p.create_item(R1__has_label="TiN/NbO2/W")
I10099 = p.create_item(R1__has_label="TiN/AsTeGeSiN/TiN")
I93835 = p.create_item(R1__has_label="W/Ag/MgO/Ag/W")
I71427 = p.create_item(R1__has_label="Pt/Ag:SiOxNy/Pt")
I77342 = p.create_item(R1__has_label="Pd/Ag/HfO2/Ag/Pd")
I40761 = p.create_item(R1__has_label="TiN/Al2O3/TiO2/TiN")
I53237 = p.create_item(R1__has_label="W/VOx/Pt")
I26254 = p.create_item(R1__has_label="p-Si/SiO2/n-Si")
I70091 = p.create_item(R1__has_label="Ni/HfO2/n-Si")
I88150 = p.create_item(R1__has_label="Cu/HfO2/n-Si")
I30588 = p.create_item(R1__has_label="Ag/a-Si/p-poly-Si")
I3720 = p.create_item(R1__has_label="Fernando Aguirre")
I22285 = p.create_item(R1__has_label="Abu Sebastian")
I37624 = p.create_item(R1__has_label="publication: Hardware implementation of memristorbased artificial neural networks")
I51553 = p.create_item(R1__has_label="Yao, P.")
I31560 = p.create_item(R1__has_label="publication: Fully hardware-implemented memristor convolutional neural network")
I20607 = p.create_item(R1__has_label="Cai, F.")
I93515 = p.create_item(R1__has_label="publication: A fully integrated reprogrammable memristor-CMOS system for efficient multiply-accumulate operations")
I70002 = p.create_item(R1__has_label="Wan, W.")
I80832 = p.create_item(R1__has_label="publication: A compute-in-memory chip based on resistive random-access memory")
I18561 = p.create_item(R1__has_label="Mochida, R.")
I54461 = p.create_item(R1__has_label="publication: A 4M synapses integrated analog ReRAM based 66.5 TOPS/W neural-network processor with cell current controlled writing and flexible network architecture")
I58610 = p.create_item(R1__has_label="Su, F.")
I39407 = p.create_item(R1__has_label="publication: A 462GOPs/J RRAM-based nonvolatile intelligent processor for energy harvesting IoE system featuring nonvolatile logics and processing-in-memory")
I21668 = p.create_item(R1__has_label="Kiani, F.")
I25569 = p.create_item(R1__has_label="Yin, J.")
I26493 = p.create_item(R1__has_label="Joshua Yang, J.")
I84601 = p.create_item(R1__has_label="Xia, Q.")
I91491 = p.create_item(R1__has_label="publication: A fully hardware-based memristive multilayer neural network")
I4359 = p.create_item(R1__has_label="publication: CMOS-integrated nanoscale memristive crossbars for CNN and optimization acceleration")
I78655 = p.create_item(R1__has_label="Pedretti, G.")
I98302 = p.create_item(R1__has_label="publication: Redundancy and analog slicing for precise inmemory machine learning - Part I: Programming techniques")
I23498 = p.create_item(R1__has_label="publication: Redundancy and analog slicing for precise inmemory machine learning - Part II: Applications and benchmark")
I4363 = p.create_item(R1__has_label="publication: Fully memristive neural networks for pattern classification with unsupervised learning")
I75344 = p.create_item(R1__has_label="Bocquet, M.")
I63365 = p.create_item(R1__has_label="publication: In-memory and error-immune differential RRAM implementation of binarized deep neural networks")
I70153 = p.create_item(R1__has_label="Chen, W. H.")
I40375 = p.create_item(R1__has_label="publication: CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors")
I7400 = p.create_item(R1__has_label="Hirtzlin, T.")
I68972 = p.create_item(R1__has_label="publication: Digital biologically plausible implementation of binarized neural networks with differential hafnium oxide resistive memory arrays")
I54872 = p.create_item(R1__has_label="Wu, T. F.")
I88419 = p.create_item(R1__has_label="publication: A 43pJ/Cycle Non-Volatile Microcontroller with 4.7μs Shutdown/Wake-up Integrating 2.3-bit/Cell Resistive RAM and Resilience Techniques")
I4397 = p.create_item(R1__has_label="Au/Pd/WOx/Au")
I13120 = p.create_item(R1__has_label="TiN/TaOx/HfOx/TiN")
I93517 = p.create_item(R1__has_label="Pt/Ta/Ta2O5/Pt/Ti")
I44506 = p.create_item(R1__has_label="Ta/TaOx/Pt")
I86897 = p.create_item(R1__has_label="W/TiN/TiON")
I58973 = p.create_item(R1__has_label="Pt/SiOxAg/Pt/Ti")
I62232 = p.create_item(R1__has_label="Ta/Pd/HfO2/Pt/Ti")
I1438 = p.create_item(R1__has_label="TiN/HfO2/Ti/TiN")
I7666 = p.create_item(R1__has_label="W/Ta2O5/TaOx/W")
I51409 = p.create_item(R1__has_label="AlCu/TiN/Ti/HfO2/TiN")
I72536 = p.create_item(R1__has_label="TiN/HfO2/TaOx/TiN")


########################################################################################################################
# content:
########################################################################################################################






I1623["memristor stack"].update_relations(
    R4__is_instance_of=p.I2["Metaclass"],
    
)



I86037["stack component"].update_relations(
    R4__is_instance_of=p.I2["Metaclass"],
    
)











R66928["has stack component"].update_relations(
    R8__has_domain_of_argument_1=I1623["memristor stack"],
    R11__has_range_of_result=I86037["stack component"],
    
)



R61856["has memristor stack"].update_relations(
    R8__has_domain_of_argument_1=ag.I6591["source document"],
    R11__has_range_of_result=I1623["memristor stack"],
    
)



R34871["has position"].update_relations(
    R11__has_range_of_result=p.I37["integer number"],
    
)
has_position = p.QualifierFactory(R34871["has position"])



R17110["is at outer position"].update_relations(
    R11__has_range_of_result=p.I53["bool"],
    
)
is_at_outer_position = p.QualifierFactory(R17110["is at outer position"])




has_citation_id = p.QualifierFactory(R49997["has citation id"])






# 2019_lanza 
I98213["Mario Lanza"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Mario Lanza",
    
)


# 2019_lanza 
I9301["H.-S. Philip Wong"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="H.-S. Philip Wong",
    
)


# 2019_lanza 
I68330["Eric Pop"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Eric Pop",
    
)


# 2019_lanza 
I12749["Daniele Ielmini"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Daniele Ielmini",
    
)


# 2019_lanza 
I38831["Dimitri Strukov"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Dimitri Strukov",
    
)


# 2019_lanza 
I45494["Brian C. Regan"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Brian C. Regan",
    
)


# 2019_lanza 
I47996["Luca Larcher"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Luca Larcher",
    
)


# 2019_lanza 
I52583["Marco A. Villena"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Marco A. Villena",
    
)


# 2019_lanza 
I35079["J. Joshua Yang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="J. Joshua Yang",
    
)


# 2019_lanza 
I10148["Ludovic Goux"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Ludovic Goux",
    
)


# 2019_lanza 
I35068["Attilio Belmonte"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Attilio Belmonte",
    
)


# 2019_lanza 
I60959["Yuchao Yang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Yuchao Yang",
    
)


# 2019_lanza 
I42597["Francesco M. Puglisi"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Francesco M. Puglisi",
    
)


# 2019_lanza 
I81302["Jinfeng Kang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Jinfeng Kang",
    
)


# 2019_lanza 
I11032["Blanka Magyari-Köpe"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Blanka Magyari-Köpe",
    
)


# 2019_lanza 
I61436["Eilam Yalon"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Eilam Yalon",
    
)


# 2019_lanza 
I18300["Anthony Kenyon"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Anthony Kenyon",
    
)


# 2019_lanza 
I35023["Mark Buckwell"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Mark Buckwell",
    
)


# 2019_lanza 
I95103["Adnan Mehonic"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Adnan Mehonic",
    
)


# 2019_lanza 
I67772["Alexander Shluger"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Alexander Shluger",
    
)


# 2019_lanza 
I66816["Haitong Li"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Haitong Li",
    
)


# 2019_lanza 
I89938["Tuo-Hung Hou"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Tuo-Hung Hou",
    
)


# 2019_lanza 
I71699["Boris Hudec"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Boris Hudec",
    
)


# 2019_lanza 
I4407["Deji Akinwande"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Deji Akinwande",
    
)


# 2019_lanza 
I94278["Ruijing Ge"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Ruijing Ge",
    
)


# 2019_lanza 
I81075["Stefano Ambrogio"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Stefano Ambrogio",
    
)


# 2019_lanza 
I17336["Juan B. Roldan"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Juan B. Roldan",
    
)


# 2019_lanza 
I3089["Enrique Miranda"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Enrique Miranda",
    
)


# 2019_lanza 
I95679["Jordi Suñe"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Jordi Suñe",
    
)


# 2019_lanza 
I22719["Kin Leong Pey"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kin Leong Pey",
    
)


# 2019_lanza 
I36951["Xing Wu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Xing Wu",
    
)


# 2019_lanza 
I31551["Nagarajan Raghavan"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Nagarajan Raghavan",
    
)


# 2019_lanza 
I70878["Ernest Wu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Ernest Wu",
    
)


# 2019_lanza 
I9426["Wei D. Lu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wei D. Lu",
    
)


# 2019_lanza 
I94216["Gabriele Navarro"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Gabriele Navarro",
    
)


# 2019_lanza 
I43418["Weidong Zhang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Weidong Zhang",
    
)


# 2019_lanza 
I78330["Huaqiang Wu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Huaqiang Wu",
    
)


# 2019_lanza 
I84818["Runwei Li"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Runwei Li",
    
)


# 2019_lanza 
I31142["Alexander Holleitner"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Alexander Holleitner",
    
)


# 2019_lanza 
I74019["Ursula Wurstbauer"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Ursula Wurstbauer",
    
)


# 2019_lanza 
I83705["Max C. Lemme"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Max C. Lemme",
    
)


# 2019_lanza 
I19231["Ming Liu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Ming Liu",
    
)


# 2019_lanza 
I72904["Shibing Long"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Shibing Long",
    
)


# 2019_lanza 
I26214["Qi Liu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Qi Liu",
    
)


# 2019_lanza 
I56137["Hangbing Lv"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Hangbing Lv",
    
)


# 2019_lanza 
I15966["Andrea Padovani"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Andrea Padovani",
    
)


# 2019_lanza 
I42377["Paolo Pavan"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Paolo Pavan",
    
)


# 2019_lanza 
I88305["Ilia Valov"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Ilia Valov",
    
)


# 2019_lanza 
I41974["Xu Jing"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Xu Jing",
    
)


# 2019_lanza 
I75108["Tingting Han"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Tingting Han",
    
)


# 2019_lanza 
I18859["Kaichen Zhu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kaichen Zhu",
    
)


# 2019_lanza 
I80129["Shaochuan Chen"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Shaochuan Chen",
    
)


# 2019_lanza 
I55623["Fei Hui"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Fei Hui",
    
)


# 2019_lanza 
I27380["Yuanyuan Shi"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Yuanyuan Shi",
    
)


# 2019_lanza 
I6779["publication: Recommended Methods to Study Resistive Switching Devices"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I98213["Mario Lanza"], I9301["H.-S. Philip Wong"], I68330["Eric Pop"], I12749["Daniele Ielmini"], I38831["Dimitri Strukov"], I45494["Brian C. Regan"], I47996["Luca Larcher"], I52583["Marco A. Villena"], I35079["J. Joshua Yang"], I10148["Ludovic Goux"], I35068["Attilio Belmonte"], I60959["Yuchao Yang"], I42597["Francesco M. Puglisi"], I81302["Jinfeng Kang"], I11032["Blanka Magyari-Köpe"], I61436["Eilam Yalon"], I18300["Anthony Kenyon"], I35023["Mark Buckwell"], I95103["Adnan Mehonic"], I67772["Alexander Shluger"], I66816["Haitong Li"], I89938["Tuo-Hung Hou"], I71699["Boris Hudec"], I4407["Deji Akinwande"], I94278["Ruijing Ge"], I81075["Stefano Ambrogio"], I17336["Juan B. Roldan"], I3089["Enrique Miranda"], I95679["Jordi Suñe"], I22719["Kin Leong Pey"], I36951["Xing Wu"], I31551["Nagarajan Raghavan"], I70878["Ernest Wu"], I9426["Wei D. Lu"], I94216["Gabriele Navarro"], I43418["Weidong Zhang"], I78330["Huaqiang Wu"], I84818["Runwei Li"], I31142["Alexander Holleitner"], I74019["Ursula Wurstbauer"], I83705["Max C. Lemme"], I19231["Ming Liu"], I72904["Shibing Long"], I26214["Qi Liu"], I56137["Hangbing Lv"], I15966["Andrea Padovani"], I42377["Paolo Pavan"], I88305["Ilia Valov"], I41974["Xu Jing"], I75108["Tingting Han"], I18859["Kaichen Zhu"], I80129["Shaochuan Chen"], I55623["Fei Hui"], I27380["Yuanyuan Shi"]],
    ag__R8434__has_title="Recommended Methods to Study Resistive Switching Devices",
    ag__R8435__has_year=2019,
    R14118__has_internal_reference="2019_lanza_et_al",
    
)
I6779["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I26917["publication: IEEE Int. Electron Devices Meet."], qualifiers=[has_citation_id(24), ])
I6779["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I22086["publication: No title given 25631219101"], qualifiers=[has_citation_id(52), ])
I6779["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I50709["publication: Appl. Phys. Lett."], qualifiers=[has_citation_id(116), ])
I6779["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I83289["publication: Nat. Mater."], qualifiers=[has_citation_id(120), ])
I6779["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I19447["publication: presented at *IEEE Int. Electron Device Meet.*"], qualifiers=[has_citation_id(121), ])
I6779["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I1159["publication: Symp. VLSI Technol."], qualifiers=[has_citation_id(127), ])
I6779["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I69142["publication: presented at *IEEE IEDM*"], qualifiers=[has_citation_id(129), ])
I6779["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I36455["publication: No title given 41246013015"], qualifiers=[has_citation_id(133), ])
I6779["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I88157["publication: No title given 28138552030"], qualifiers=[has_citation_id(241), ])
I6779["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I3972["publication: IEEE Electron Device Lett."], qualifiers=[has_citation_id(242), ])
I6779["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I26216["publication: IEEE Trans. Electron Devices"], qualifiers=[has_citation_id(243), ])
I6779["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I20930["publication: 2011 Symp. on VLSI Technology - Digest of Technical Papers"], qualifiers=[has_citation_id(244), ])
I6779["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I65519["publication: No title given 26048021673"], qualifiers=[has_citation_id(245), ])
I6779["publication: Recommended Methods to Study Resistive Switching Devices"].set_relation(ag.R8440["cites"], I43431["publication: No title given 86846326096"], qualifiers=[has_citation_id(246), ])


# 2019_lanza 
I89114["H. Y. Lee"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="H. Y. Lee",
    
)


# 2019_lanza 
I85415["Y. S. Chen"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. S. Chen",
    
)


# 2019_lanza 
I71318["P. S. Chen"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="P. S. Chen",
    
)


# 2019_lanza 
I40045["P. Y. Gu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="P. Y. Gu",
    
)


# 2019_lanza 
I78072["Y. Y. Hsu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. Y. Hsu",
    
)


# 2019_lanza 
I17406["S. M. Wang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. M. Wang",
    
)


# 2019_lanza 
I70034["W. H. Liu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="W. H. Liu",
    
)


# 2019_lanza 
I82691["C. H. Tsai"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. H. Tsai",
    
)


# 2019_lanza 
I67208["S. S. Sheu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. S. Sheu",
    
)


# 2019_lanza 
I29245["P. C. Chiang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="P. C. Chiang",
    
)


# 2019_lanza 
I84274["W. P. Lin"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="W. P. Lin",
    
)


# 2019_lanza 
I97898["C. H. Lin"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. H. Lin",
    
)


# 2019_lanza 
I55841["W. S. Chen"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="W. S. Chen",
    
)


# 2019_lanza 
I63187["F. T. Chen"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="F. T. Chen",
    
)


# 2019_lanza 
I50200["C. H. Lien"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. H. Lien",
    
)


# 2019_lanza 
I97039["M. J. Tsai"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. J. Tsai",
    
)


# 2019_lanza 
I26917["publication: IEEE Int. Electron Devices Meet."].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I89114["H. Y. Lee"], I85415["Y. S. Chen"], I71318["P. S. Chen"], I40045["P. Y. Gu"], I78072["Y. Y. Hsu"], I17406["S. M. Wang"], I70034["W. H. Liu"], I82691["C. H. Tsai"], I67208["S. S. Sheu"], I29245["P. C. Chiang"], I84274["W. P. Lin"], I97898["C. H. Lin"], I55841["W. S. Chen"], I63187["F. T. Chen"], I50200["C. H. Lien"], I97039["M. J. Tsai"]],
    ag__R8434__has_title="IEEE Int. Electron Devices Meet.",
    ag__R8435__has_year=2010,
    R61856__has_memristor_stack=I70632["TiN/TiOx/HfOx/TiN"],
    
)


# 2019_lanza 
I15997["B. Govoreanu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="B. Govoreanu",
    
)


# 2019_lanza 
I85412["G. S. Kar"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="G. S. Kar",
    
)


# 2019_lanza 
I77477["Y-Y. Chen"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y-Y. Chen",
    
)


# 2019_lanza 
I73058["V. Paraschiv"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="V. Paraschiv",
    
)


# 2019_lanza 
I32600["S. Kubicek"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. Kubicek",
    
)


# 2019_lanza 
I49732["A. Fantini"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="A. Fantini",
    
)


# 2019_lanza 
I16948["I. P. Radu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="I. P. Radu",
    
)


# 2019_lanza 
I22825["L. Goux"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="L. Goux",
    
)


# 2019_lanza 
I6679["S. Clima"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. Clima",
    
)


# 2019_lanza 
I61031["R. Degraeve"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="R. Degraeve",
    
)


# 2019_lanza 
I35393["N. Jossart"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="N. Jossart",
    
)


# 2019_lanza 
I26269["O. Richard"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="O. Richard",
    
)


# 2019_lanza 
I69444["T. Vandeweyer"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="T. Vandeweyer",
    
)


# 2019_lanza 
I20147["K. Seo"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="K. Seo",
    
)


# 2019_lanza 
I76671["P. Hendrickx"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="P. Hendrickx",
    
)


# 2019_lanza 
I4936["G. Pourtois"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="G. Pourtois",
    
)


# 2019_lanza 
I26714["H. Bender"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="H. Bender",
    
)


# 2019_lanza 
I15948["L. Altimime"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="L. Altimime",
    
)


# 2019_lanza 
I72220["D. J. Wouters"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="D. J. Wouters",
    
)


# 2019_lanza 
I68261["J. A. Kittl"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="J. A. Kittl",
    
)


# 2019_lanza 
I51128["M. Jurczak"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. Jurczak",
    
)


# 2019_lanza 
I22086["publication: No title given 25631219101"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I15997["B. Govoreanu"], I85412["G. S. Kar"], I77477["Y-Y. Chen"], I73058["V. Paraschiv"], I32600["S. Kubicek"], I49732["A. Fantini"], I16948["I. P. Radu"], I22825["L. Goux"], I6679["S. Clima"], I61031["R. Degraeve"], I35393["N. Jossart"], I26269["O. Richard"], I69444["T. Vandeweyer"], I20147["K. Seo"], I76671["P. Hendrickx"], I4936["G. Pourtois"], I26714["H. Bender"], I15948["L. Altimime"], I72220["D. J. Wouters"], I68261["J. A. Kittl"], I51128["M. Jurczak"]],
    ag__R8434__has_title="No title given 25631219101",
    ag__R8435__has_year=2011,
    R61856__has_memristor_stack=I66262["TiN/Hf/HfOx/TiN"],
    
)


# 2019_lanza 
I77371["J. J. Yang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="J. J. Yang",
    
)


# 2019_lanza 
I20407["M.-X. Zhang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M.-X. Zhang",
    
)


# 2019_lanza 
I43423["J. P. Strachan"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="J. P. Strachan",
    
)


# 2019_lanza 
I13119["F. Miao"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="F. Miao",
    
)


# 2019_lanza 
I17638["M. D. Pickett"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. D. Pickett",
    
)


# 2019_lanza 
I74490["R. D. Kelley"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="R. D. Kelley",
    
)


# 2019_lanza 
I42047["G. Medeiros-Ribeiro"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="G. Medeiros-Ribeiro",
    
)


# 2019_lanza 
I26624["R. S. Williams"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="R. S. Williams",
    
)


# 2019_lanza 
I50709["publication: Appl. Phys. Lett."].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I77371["J. J. Yang"], I20407["M.-X. Zhang"], I43423["J. P. Strachan"], I13119["F. Miao"], I17638["M. D. Pickett"], I74490["R. D. Kelley"], I42047["G. Medeiros-Ribeiro"], I26624["R. S. Williams"]],
    ag__R8434__has_title="Appl. Phys. Lett.",
    ag__R8435__has_year=2010,
    R61856__has_memristor_stack=I11140["Pt/TaOx/Ta"],
    
)


# 2019_lanza 
I31489["M. J. Lee"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. J. Lee",
    
)


# 2019_lanza 
I4668["C. B. Lee"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. B. Lee",
    
)


# 2019_lanza 
I97883["D. S. Lee"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="D. S. Lee",
    
)


# 2019_lanza 
I35402["S. R. Lee"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. R. Lee",
    
)


# 2019_lanza 
I33313["M. Chang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. Chang",
    
)


# 2019_lanza 
I83787["J. H. Hur"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="J. H. Hur",
    
)


# 2019_lanza 
I39495["Y. B. Kim"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. B. Kim",
    
)


# 2019_lanza 
I91911["C. J. Kim"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. J. Kim",
    
)


# 2019_lanza 
I48432["D. H. Seo"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="D. H. Seo",
    
)


# 2019_lanza 
I3263["S. Seo"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. Seo",
    
)


# 2019_lanza 
I40069["U. I. Chung"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="U. I. Chung",
    
)


# 2019_lanza 
I11297["I. K. Yoo"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="I. K. Yoo",
    
)


# 2019_lanza 
I35953["K. Kim"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="K. Kim",
    
)


# 2019_lanza 
I83289["publication: Nat. Mater."].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I31489["M. J. Lee"], I4668["C. B. Lee"], I97883["D. S. Lee"], I35402["S. R. Lee"], I33313["M. Chang"], I83787["J. H. Hur"], I39495["Y. B. Kim"], I91911["C. J. Kim"], I48432["D. H. Seo"], I3263["S. Seo"], I40069["U. I. Chung"], I11297["I. K. Yoo"], I35953["K. Kim"]],
    ag__R8434__has_title="Nat. Mater.",
    ag__R8435__has_year=2011,
    R61856__has_memristor_stack=I19279["Pt/Ta2O5-x/TaO2-x/Pt"],
    
)


# 2019_lanza 
I81467["I G. Baek"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="I G. Baek",
    
)


# 2019_lanza 
I78347["M. S. Lee"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. S. Lee",
    
)


# 2019_lanza 
I2120["D. S. Suh"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="D. S. Suh",
    
)


# 2019_lanza 
I32499["J. C. Park"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="J. C. Park",
    
)


# 2019_lanza 
I12382["S. O. Park"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. O. Park",
    
)


# 2019_lanza 
I91222["H. S. Kim"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="H. S. Kim",
    
)


# 2019_lanza 
I8497["J. T. Moon"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="J. T. Moon",
    
)


# 2019_lanza 
I19447["publication: presented at *IEEE Int. Electron Device Meet.*"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I81467["I G. Baek"], I78347["M. S. Lee"], I3263["S. Seo"], I31489["M. J. Lee"], I48432["D. H. Seo"], I2120["D. S. Suh"], I32499["J. C. Park"], I12382["S. O. Park"], I91222["H. S. Kim"], I11297["I. K. Yoo"], I40069["U. I. Chung"], I8497["J. T. Moon"]],
    ag__R8434__has_title="presented at *IEEE Int. Electron Device Meet.*",
    ag__R8435__has_year=2004,
    R61856__has_memristor_stack=I11158["Ta/TaOx/TiO2/Ti"],
    
)


# 2019_lanza 
I8318["C. H. Cheng"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. H. Cheng",
    
)


# 2019_lanza 
I19405["A. Chin"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="A. Chin",
    
)


# 2019_lanza 
I76726["F. S. Yeh"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="F. S. Yeh",
    
)


# 2019_lanza 
I1159["publication: Symp. VLSI Technol."].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I8318["C. H. Cheng"], I19405["A. Chin"], I76726["F. S. Yeh"]],
    ag__R8434__has_title="Symp. VLSI Technol.",
    ag__R8435__has_year=2010,
    R61856__has_memristor_stack=I71049["Ni/GeO/STO/TaN"],
    
)


# 2019_lanza 
I79242["Z. Wei"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Z. Wei",
    
)


# 2019_lanza 
I37274["Y. Kanzawa"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. Kanzawa",
    
)


# 2019_lanza 
I23890["K. Arita"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="K. Arita",
    
)


# 2019_lanza 
I66877["Y. Katoh"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. Katoh",
    
)


# 2019_lanza 
I1523["K. Kawai"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="K. Kawai",
    
)


# 2019_lanza 
I28497["S. Muraoka"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. Muraoka",
    
)


# 2019_lanza 
I32191["S. Mitani"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. Mitani",
    
)


# 2019_lanza 
I29406["S. Fujii"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. Fujii",
    
)


# 2019_lanza 
I30039["K. Katayama"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="K. Katayama",
    
)


# 2019_lanza 
I95692["M. Iijima"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. Iijima",
    
)


# 2019_lanza 
I90836["T. Mikawa"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="T. Mikawa",
    
)


# 2019_lanza 
I69967["T. Ninomiya"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="T. Ninomiya",
    
)


# 2019_lanza 
I85895["R. Miyanaga"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="R. Miyanaga",
    
)


# 2019_lanza 
I71924["Y. Kawashima"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. Kawashima",
    
)


# 2019_lanza 
I97779["K. Tsuji"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="K. Tsuji",
    
)


# 2019_lanza 
I50815["A. Himeno"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="A. Himeno",
    
)


# 2019_lanza 
I35590["T. Okada"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="T. Okada",
    
)


# 2019_lanza 
I2968["R. Azuma"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="R. Azuma",
    
)


# 2019_lanza 
I75800["K. Shimakawa"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="K. Shimakawa",
    
)


# 2019_lanza 
I26378["H. Sugaya"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="H. Sugaya",
    
)


# 2019_lanza 
I59962["T. Takagi"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="T. Takagi",
    
)


# 2019_lanza 
I93041["R. Yasuhara"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="R. Yasuhara",
    
)


# 2019_lanza 
I39016["K. Horiba"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="K. Horiba",
    
)


# 2019_lanza 
I42747["H. Kumigashira"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="H. Kumigashira",
    
)


# 2019_lanza 
I34150["M. Oshima"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. Oshima",
    
)


# 2019_lanza 
I69142["publication: presented at *IEEE IEDM*"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I79242["Z. Wei"], I37274["Y. Kanzawa"], I23890["K. Arita"], I66877["Y. Katoh"], I1523["K. Kawai"], I28497["S. Muraoka"], I32191["S. Mitani"], I29406["S. Fujii"], I30039["K. Katayama"], I95692["M. Iijima"], I90836["T. Mikawa"], I69967["T. Ninomiya"], I85895["R. Miyanaga"], I71924["Y. Kawashima"], I97779["K. Tsuji"], I50815["A. Himeno"], I35590["T. Okada"], I2968["R. Azuma"], I75800["K. Shimakawa"], I26378["H. Sugaya"], I59962["T. Takagi"], I93041["R. Yasuhara"], I39016["K. Horiba"], I42747["H. Kumigashira"], I34150["M. Oshima"]],
    ag__R8434__has_title="presented at *IEEE IEDM*",
    ag__R8435__has_year=2008,
    R61856__has_memristor_stack=I69260["Pt/TaOx/Pt"],
    
)


# 2019_lanza 
I60173["L. G. Wang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="L. G. Wang",
    
)


# 2019_lanza 
I31595["X. Qian"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="X. Qian",
    
)


# 2019_lanza 
I85919["Y. Q. Cao"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. Q. Cao",
    
)


# 2019_lanza 
I38439["Z. Y. Cao"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Z. Y. Cao",
    
)


# 2019_lanza 
I79583["G. Y. Fang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="G. Y. Fang",
    
)


# 2019_lanza 
I92231["A. D. Li"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="A. D. Li",
    
)


# 2019_lanza 
I47075["D. Wu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="D. Wu",
    
)


# 2019_lanza 
I36455["publication: No title given 41246013015"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I60173["L. G. Wang"], I31595["X. Qian"], I85919["Y. Q. Cao"], I38439["Z. Y. Cao"], I79583["G. Y. Fang"], I92231["A. D. Li"], I47075["D. Wu"]],
    ag__R8434__has_title="No title given 41246013015",
    ag__R8435__has_year=2015,
    R61856__has_memristor_stack=I68625["Pt/Al2O3/HfO2/Al2O3/TiN/Si"],
    
)


# 2019_lanza 
I64442["H.-S. P. Wong"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="H.-S. P. Wong",
    
)


# 2019_lanza 
I46737["S. Yu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="S. Yu",
    
)


# 2019_lanza 
I55336["Y. Wu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. Wu",
    
)


# 2019_lanza 
I74558["B. Lee"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="B. Lee",
    
)


# 2019_lanza 
I88157["publication: No title given 28138552030"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I64442["H.-S. P. Wong"], I89114["H. Y. Lee"], I46737["S. Yu"], I85415["Y. S. Chen"], I55336["Y. Wu"], I71318["P. S. Chen"], I74558["B. Lee"], I63187["F. T. Chen"], I97039["M. J. Tsai"]],
    ag__R8434__has_title="No title given 28138552030",
    ag__R8435__has_year=2012,
    R61856__has_memristor_stack=I70632["TiN/TiOx/HfOx/TiN"],
    
)


# 2019_lanza 
I76467["M. C. Wu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. C. Wu",
    
)


# 2019_lanza 
I32160["Y. W. Lin"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. W. Lin",
    
)


# 2019_lanza 
I59566["W. Y. Jang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="W. Y. Jang",
    
)


# 2019_lanza 
I42835["T. Y. Tseng"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="T. Y. Tseng",
    
)


# 2019_lanza 
I3972["publication: IEEE Electron Device Lett."].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I76467["M. C. Wu"], I32160["Y. W. Lin"], I59566["W. Y. Jang"], I97898["C. H. Lin"], I42835["T. Y. Tseng"]],
    ag__R8434__has_title="IEEE Electron Device Lett.",
    ag__R8435__has_year=2011,
    R61856__has_memristor_stack=I51049["Ti/ZrO2/Pt"],
    
)


# 2019_lanza 
I99897["C. Ahn"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. Ahn",
    
)


# 2019_lanza 
I3777["Z. Jiang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Z. Jiang",
    
)


# 2019_lanza 
I42701["C. S. Lee"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. S. Lee",
    
)


# 2019_lanza 
I70477["H. Y. Chen"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="H. Y. Chen",
    
)


# 2019_lanza 
I8841["J. Liang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="J. Liang",
    
)


# 2019_lanza 
I34548["L. S. Liyanage"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="L. S. Liyanage",
    
)


# 2019_lanza 
I8157["H. S. P. Wong"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="H. S. P. Wong",
    
)


# 2019_lanza 
I26216["publication: IEEE Trans. Electron Devices"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I99897["C. Ahn"], I3777["Z. Jiang"], I42701["C. S. Lee"], I70477["H. Y. Chen"], I8841["J. Liang"], I34548["L. S. Liyanage"], I8157["H. S. P. Wong"]],
    ag__R8434__has_title="IEEE Trans. Electron Devices",
    ag__R8435__has_year=2015,
    R61856__has_memristor_stack=I93962["Al/Ti/Al2O3/s-CNT"],
    
)


# 2019_lanza 
I2784["D. Lee"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="D. Lee",
    
)


# 2019_lanza 
I11276["G. S. Park"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="G. S. Park",
    
)


# 2019_lanza 
I91141["U. Chung"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="U. Chung",
    
)


# 2019_lanza 
I20930["publication: 2011 Symp. on VLSI Technology - Digest of Technical Papers"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I39495["Y. B. Kim"], I35402["S. R. Lee"], I2784["D. Lee"], I4668["C. B. Lee"], I33313["M. Chang"], I83787["J. H. Hur"], I31489["M. J. Lee"], I11276["G. S. Park"], I91911["C. J. Kim"], I91141["U. Chung"], I11297["I. K. Yoo"], I35953["K. Kim"]],
    ag__R8434__has_title="2011 Symp. on VLSI Technology - Digest of Technical Papers",
    ag__R8435__has_year=2011,
    R61856__has_memristor_stack=I54529["W/AlO/TaOx/ZrOx/Ru"],
    
)


# 2019_lanza 
I30609["V. K. Nagareddy"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="V. K. Nagareddy",
    
)


# 2019_lanza 
I89040["A. K. Ott"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="A. K. Ott",
    
)


# 2019_lanza 
I46623["C. Dou"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. Dou",
    
)


# 2019_lanza 
I59209["T. Tsvetkova"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="T. Tsvetkova",
    
)


# 2019_lanza 
I48506["M. Sandulov"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. Sandulov",
    
)


# 2019_lanza 
I49412["M. F. Craciun"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="M. F. Craciun",
    
)


# 2019_lanza 
I66355["A. C. Ferrari"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="A. C. Ferrari",
    
)


# 2019_lanza 
I47721["C. D. Wright"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="C. D. Wright",
    
)


# 2019_lanza 
I65519["publication: No title given 26048021673"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I30609["V. K. Nagareddy"], I89040["A. K. Ott"], I46623["C. Dou"], I59209["T. Tsvetkova"], I48506["M. Sandulov"], I49412["M. F. Craciun"], I66355["A. C. Ferrari"], I47721["C. D. Wright"]],
    ag__R8434__has_title="No title given 26048021673",
    R61856__has_memristor_stack=I85511["TaN/TiN/Zr/HfO2/CAFM tip"],
    
)


# 2019_lanza 
I7018["X. Cao"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="X. Cao",
    
)


# 2019_lanza 
I58662["X. M. Li"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="X. M. Li",
    
)


# 2019_lanza 
I83250["X. D. Gao"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="X. D. Gao",
    
)


# 2019_lanza 
I3155["W. D. Yu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="W. D. Yu",
    
)


# 2019_lanza 
I47458["X. J. Liu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="X. J. Liu",
    
)


# 2019_lanza 
I77727["Y. W. Zhang"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Y. W. Zhang",
    
)


# 2019_lanza 
I62007["L. D. Chen"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="L. D. Chen",
    
)


# 2019_lanza 
I32629["X. H. Cheng"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="X. H. Cheng",
    
)


# 2019_lanza 
I43431["publication: No title given 86846326096"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I7018["X. Cao"], I58662["X. M. Li"], I83250["X. D. Gao"], I3155["W. D. Yu"], I47458["X. J. Liu"], I77727["Y. W. Zhang"], I62007["L. D. Chen"], I32629["X. H. Cheng"]],
    ag__R8434__has_title="No title given 86846326096",
    ag__R8435__has_year=2009,
    R61856__has_memristor_stack=I13696["Pt/Gd2O3/Pt"],
    
)


# 2019_lanza 
I70632["TiN/TiOx/HfOx/TiN"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I70632["TiN/TiOx/HfOx/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I70632["TiN/TiOx/HfOx/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I70632["TiN/TiOx/HfOx/TiN"].set_relation(R66928["has stack component"], omt.I6120["TiOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I70632["TiN/TiOx/HfOx/TiN"].set_relation(R66928["has stack component"], omt.I6105["HfOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019_lanza 



# 2019_lanza 



# 2019_lanza 



# 2019_lanza 
I51049["Ti/ZrO2/Pt"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I51049["Ti/ZrO2/Pt"].set_relation(R66928["has stack component"], omt.I87594["titanium"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I51049["Ti/ZrO2/Pt"].set_relation(R66928["has stack component"], I78439["ZrO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I51049["Ti/ZrO2/Pt"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019_lanza 



# 2019_lanza 
I78439["ZrO2"].update_relations(
    R4__is_instance_of=I86037["stack component"],
    
)


# 2019_lanza 



# 2019_lanza 
I66262["TiN/Hf/HfOx/TiN"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I66262["TiN/Hf/HfOx/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I66262["TiN/Hf/HfOx/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I66262["TiN/Hf/HfOx/TiN"].set_relation(R66928["has stack component"], omt.I79894["hafnium"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I66262["TiN/Hf/HfOx/TiN"].set_relation(R66928["has stack component"], omt.I6105["HfOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019_lanza 



# 2019_lanza 
I93962["Al/Ti/Al2O3/s-CNT"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I93962["Al/Ti/Al2O3/s-CNT"].set_relation(R66928["has stack component"], omt.I85583["aluminum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I93962["Al/Ti/Al2O3/s-CNT"].set_relation(R66928["has stack component"], omt.I87594["titanium"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I93962["Al/Ti/Al2O3/s-CNT"].set_relation(R66928["has stack component"], omt.I6100["Al2O3"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I93962["Al/Ti/Al2O3/s-CNT"].set_relation(R66928["has stack component"], I1292["s-CNT"], qualifiers=[has_position(3), is_at_outer_position(True), ])


# 2019_lanza 



# 2019_lanza 



# 2019_lanza 
I1292["s-CNT"].update_relations(
    R4__is_instance_of=I86037["stack component"],
    
)


# 2019_lanza 
I19279["Pt/Ta2O5-x/TaO2-x/Pt"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I19279["Pt/Ta2O5-x/TaO2-x/Pt"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I19279["Pt/Ta2O5-x/TaO2-x/Pt"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I19279["Pt/Ta2O5-x/TaO2-x/Pt"].set_relation(R66928["has stack component"], I64653["Ta2O5-x"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I19279["Pt/Ta2O5-x/TaO2-x/Pt"].set_relation(R66928["has stack component"], I75462["TaO2-x"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019_lanza 
I64653["Ta2O5-x"].update_relations(
    R4__is_instance_of=I86037["stack component"],
    
)


# 2019_lanza 
I75462["TaO2-x"].update_relations(
    R4__is_instance_of=I86037["stack component"],
    
)


# 2019_lanza 
I69260["Pt/TaOx/Pt"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I69260["Pt/TaOx/Pt"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I69260["Pt/TaOx/Pt"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I69260["Pt/TaOx/Pt"].set_relation(R66928["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_lanza 



# 2019_lanza 
I11158["Ta/TaOx/TiO2/Ti"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I11158["Ta/TaOx/TiO2/Ti"].set_relation(R66928["has stack component"], omt.I38968["tantalum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I11158["Ta/TaOx/TiO2/Ti"].set_relation(R66928["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I11158["Ta/TaOx/TiO2/Ti"].set_relation(R66928["has stack component"], omt.I6119["TiO2"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I11158["Ta/TaOx/TiO2/Ti"].set_relation(R66928["has stack component"], omt.I87594["titanium"], qualifiers=[has_position(3), is_at_outer_position(True), ])


# 2019_lanza 



# 2019_lanza 



# 2019_lanza 
I11140["Pt/TaOx/Ta"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I11140["Pt/TaOx/Ta"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I11140["Pt/TaOx/Ta"].set_relation(R66928["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I11140["Pt/TaOx/Ta"].set_relation(R66928["has stack component"], omt.I38968["tantalum"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019_lanza 
I54529["W/AlO/TaOx/ZrOx/Ru"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I54529["W/AlO/TaOx/ZrOx/Ru"].set_relation(R66928["has stack component"], omt.I41958["tungsten"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I54529["W/AlO/TaOx/ZrOx/Ru"].set_relation(R66928["has stack component"], I13510["AlO"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I54529["W/AlO/TaOx/ZrOx/Ru"].set_relation(R66928["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I54529["W/AlO/TaOx/ZrOx/Ru"].set_relation(R66928["has stack component"], I83785["ZrOx"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I54529["W/AlO/TaOx/ZrOx/Ru"].set_relation(R66928["has stack component"], omt.I97157["ruthenium"], qualifiers=[has_position(4), is_at_outer_position(True), ])


# 2019_lanza 



# 2019_lanza 
I13510["AlO"].update_relations(
    R4__is_instance_of=I86037["stack component"],
    
)


# 2019_lanza 
I83785["ZrOx"].update_relations(
    R4__is_instance_of=I86037["stack component"],
    
)


# 2019_lanza 



# 2019_lanza 
I68625["Pt/Al2O3/HfO2/Al2O3/TiN/Si"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I68625["Pt/Al2O3/HfO2/Al2O3/TiN/Si"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I68625["Pt/Al2O3/HfO2/Al2O3/TiN/Si"].set_relation(R66928["has stack component"], omt.I6100["Al2O3"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I68625["Pt/Al2O3/HfO2/Al2O3/TiN/Si"].set_relation(R66928["has stack component"], omt.I6100["Al2O3"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I68625["Pt/Al2O3/HfO2/Al2O3/TiN/Si"].set_relation(R66928["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I68625["Pt/Al2O3/HfO2/Al2O3/TiN/Si"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(4), is_at_outer_position(False), ])
I68625["Pt/Al2O3/HfO2/Al2O3/TiN/Si"].set_relation(R66928["has stack component"], omt.I70616["silicon"], qualifiers=[has_position(5), is_at_outer_position(True), ])


# 2019_lanza 



# 2019_lanza 



# 2019_lanza 
I85511["TaN/TiN/Zr/HfO2/CAFM tip"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I85511["TaN/TiN/Zr/HfO2/CAFM tip"].set_relation(R66928["has stack component"], omt.I6125["TaN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I85511["TaN/TiN/Zr/HfO2/CAFM tip"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I85511["TaN/TiN/Zr/HfO2/CAFM tip"].set_relation(R66928["has stack component"], omt.I61164["zirconium"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I85511["TaN/TiN/Zr/HfO2/CAFM tip"].set_relation(R66928["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I85511["TaN/TiN/Zr/HfO2/CAFM tip"].set_relation(R66928["has stack component"], I30387["CAFM tip"], qualifiers=[has_position(4), is_at_outer_position(True), ])


# 2019_lanza 



# 2019_lanza 



# 2019_lanza 
I30387["CAFM tip"].update_relations(
    R4__is_instance_of=I86037["stack component"],
    
)


# 2019_lanza 
I71049["Ni/GeO/STO/TaN"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I71049["Ni/GeO/STO/TaN"].set_relation(R66928["has stack component"], omt.I87636["nickel"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I71049["Ni/GeO/STO/TaN"].set_relation(R66928["has stack component"], I28797["GeO"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I71049["Ni/GeO/STO/TaN"].set_relation(R66928["has stack component"], I46363["STO"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I71049["Ni/GeO/STO/TaN"].set_relation(R66928["has stack component"], omt.I6125["TaN"], qualifiers=[has_position(3), is_at_outer_position(True), ])


# 2019_lanza 



# 2019_lanza 
I28797["GeO"].update_relations(
    R4__is_instance_of=I86037["stack component"],
    
)


# 2019_lanza 
I46363["STO"].update_relations(
    R4__is_instance_of=I86037["stack component"],
    
)


# 2019_lanza 
I13696["Pt/Gd2O3/Pt"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I13696["Pt/Gd2O3/Pt"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I13696["Pt/Gd2O3/Pt"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I13696["Pt/Gd2O3/Pt"].set_relation(R66928["has stack component"], I67113["Gd2O3"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_lanza 
I67113["Gd2O3"].update_relations(
    R4__is_instance_of=I86037["stack component"],
    
)


# 2019_xia 
I26235["Qiangfei Xia"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Qiangfei Xia",
    
)


# 2019_xia 
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I26235["Qiangfei Xia"], I35079["J. Joshua Yang"]],
    ag__R8434__has_title="Memristive crossbar arrays for brain-inspired computing",
    ag__R8435__has_year=2019,
    R14118__has_internal_reference="2019_xia_et_al",
    
)
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I21705["publication: Memristors with difusive dynamics as synaptic emulators for neuromorphic computing"], qualifiers=[has_citation_id(33), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I1628["publication: Tree-dimensional crossbar arrays of self-rectifying Si/SiO2/Si memristors"], qualifiers=[has_citation_id(54), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I73950["publication: Anatomy of Ag/Hafnia-based selectors with 1010 nonlinearity"], qualifiers=[has_citation_id(92), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I75618["publication: Bipolar nonlinear Ni/ TiO2/Ni selector for 1S1R crossbar array applications"], qualifiers=[has_citation_id(94), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I89338["publication: TiO2-based metal–insulator–metal selection device for bipolar resistive random access memory cross-point application"], qualifiers=[has_citation_id(95), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I73331["publication: High-performance metal–insulator–metal tunnel diode selectors"], qualifiers=[has_citation_id(96), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I13672["publication: Electrical and reliability characteristics of a scaled (∼30nm) tunnel barrier selector (W/Ta2O5/TaOx/TiO2/TiN) with excellent performance (JMAX>107A/cm2)"], qualifiers=[has_citation_id(97), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I82962["publication: Varistor-type bidirectional switch (JMAX>107A/cm2 , selectivity ∼104 ) for 3D bipolar resistive memory arrays"], qualifiers=[has_citation_id(98), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I17370["publication: Trilayer tunnel selectors for memristor memory cells"], qualifiers=[has_citation_id(99), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I97500["publication: An 8 Mb multi-layered cross-point ReRAM macro with 443 MB/s write throughput"], qualifiers=[has_citation_id(100), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I13780["publication: Termally stable integrated Se-based OTS selectors with >20MA/cm2 current drive, >3.103 half-bias nonlinearity, tunable threshold voltage and excellent endurance"], qualifiers=[has_citation_id(102), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I28644["publication: Breakthrough of selector technology for cross-point 25-nm ReRAM"], qualifiers=[has_citation_id(106), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I73977["publication: Excellent selector characteristics of nanoscale VO2 for high-density bipolar ReRAM applications"], qualifiers=[has_citation_id(107), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I35602["publication: NbO2-based low power and cost efective 1S1R switching for high density cross point ReRAM application"], qualifiers=[has_citation_id(108), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I67839["publication: Nanoscale (∼10nm) 3D vertical ReRAM and NbO2 threshold selector with TiN electrode"], qualifiers=[has_citation_id(109), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I49726["publication: Highly-scalable threshold switching select device based on chalcogenide glasses for 3D nanoscaled memory arrays"], qualifiers=[has_citation_id(110), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I85749["publication: Physically transient threshold switching device based on magnesium oxide for security application"], qualifiers=[has_citation_id(111), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I27754["publication: High‐performance and low‐power rewritable SiO*x* 1 kbit one diode–one resistor crossbar memory array"], qualifiers=[has_citation_id(114), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I46324["publication: Vacancy-modulated conductive oxide resistive RAM (VMCO-RRAM): an area-scalable switching current, self-compliant, highly nonlinear and wide on/of-window resistive switching cell"], qualifiers=[has_citation_id(115), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I20852["publication: Self-selective characteristics of nanoscale VOx devices for high-density ReRAM applications"], qualifiers=[has_citation_id(116), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I53525["publication: Investigations of conduction mechanisms of the self-rectifying n<sup>+</sup>Si-HfO2-Ni RRAM devices"], qualifiers=[has_citation_id(117), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I4356["publication: Unipolar resistive switching with forming-free and self-rectifying efects in Cu/HfO2/n-Si devices"], qualifiers=[has_citation_id(118), ])
I95037["publication: Memristive crossbar arrays for brain-inspired computing"].set_relation(ag.R8440["cites"], I45125["publication: Nanoscale resistive memory with intrinsic diode characteristics and long endurance"], qualifiers=[has_citation_id(119), ])


# 2019_xia 
I60603["Wang, Z."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wang, Z.",
    
)


# 2019_xia 
I21705["publication: Memristors with difusive dynamics as synaptic emulators for neuromorphic computing"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I60603["Wang, Z."],
    ag__R8434__has_title="Memristors with difusive dynamics as synaptic emulators for neuromorphic computing",
    ag__R8435__has_year=2017,
    R61856__has_memristor_stack=I71427["Pt/Ag:SiOxNy/Pt"],
    
)


# 2019_xia 
I71085["Li, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Li, C.",
    
)


# 2019_xia 
I1628["publication: Tree-dimensional crossbar arrays of self-rectifying Si/SiO2/Si memristors"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I71085["Li, C."],
    ag__R8434__has_title="Tree-dimensional crossbar arrays of self-rectifying Si/SiO2/Si memristors",
    ag__R8435__has_year=2017,
    R61856__has_memristor_stack=I26254["p-Si/SiO2/n-Si"],
    
)


# 2019_xia 
I69074["Midya, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Midya, R.",
    
)


# 2019_xia 
I73950["publication: Anatomy of Ag/Hafnia-based selectors with 1010 nonlinearity"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I69074["Midya, R."],
    ag__R8434__has_title="Anatomy of Ag/Hafnia-based selectors with 1010 nonlinearity",
    ag__R8435__has_year=2017,
    R61856__has_memristor_stack=I77342["Pd/Ag/HfO2/Ag/Pd"],
    
)


# 2019_xia 
I81200["Huang, J.-J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Huang, J.-J.",
    
)


# 2019_xia 
I15872["Tseng, Y.-M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Tseng, Y.-M.",
    
)


# 2019_xia 
I61127["Hsu, C.-W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Hsu, C.-W.",
    
)


# 2019_xia 
I10492["Hou, T.-H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Hou, T.-H.",
    
)


# 2019_xia 
I75618["publication: Bipolar nonlinear Ni/ TiO2/Ni selector for 1S1R crossbar array applications"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I81200["Huang, J.-J."], I15872["Tseng, Y.-M."], I61127["Hsu, C.-W."], I10492["Hou, T.-H."]],
    ag__R8434__has_title="Bipolar nonlinear Ni/ TiO2/Ni selector for 1S1R crossbar array applications",
    ag__R8435__has_year=2011,
    R61856__has_memristor_stack=I2579["Ni/TiO2/Ni"],
    
)


# 2019_xia 
I85787["Shin, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Shin, J.",
    
)


# 2019_xia 
I89338["publication: TiO2-based metal–insulator–metal selection device for bipolar resistive random access memory cross-point application"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I85787["Shin, J."],
    ag__R8434__has_title="TiO2-based metal–insulator–metal selection device for bipolar resistive random access memory cross-point application",
    ag__R8435__has_year=2011,
    R61856__has_memristor_stack=I25766["Pt/TiO2/TiN"],
    
)


# 2019_xia 
I99774["Govoreanu, B."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Govoreanu, B.",
    
)


# 2019_xia 
I73331["publication: High-performance metal–insulator–metal tunnel diode selectors"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I99774["Govoreanu, B."],
    ag__R8434__has_title="High-performance metal–insulator–metal tunnel diode selectors",
    ag__R8435__has_year=2014,
    R61856__has_memristor_stack=I53423["TiN/Ta2O5/TiN"],
    
)


# 2019_xia 
I70578["Woo, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Woo, J.",
    
)


# 2019_xia 
I13672["publication: Electrical and reliability characteristics of a scaled (∼30nm) tunnel barrier selector (W/Ta2O5/TaOx/TiO2/TiN) with excellent performance (JMAX>107A/cm2)"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I70578["Woo, J."],
    ag__R8434__has_title="Electrical and reliability characteristics of a scaled (∼30nm) tunnel barrier selector (W/Ta2O5/TaOx/TiO2/TiN) with excellent performance (JMAX>107A/cm2)",
    ag__R8435__has_year=2014,
    R61856__has_memristor_stack=I16044["W/Ta2O5/TaOx/TiO2/TiN"],
    
)


# 2019_xia 
I98352["Lee, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Lee, W.",
    
)


# 2019_xia 
I82962["publication: Varistor-type bidirectional switch (JMAX>107A/cm2 , selectivity ∼104 ) for 3D bipolar resistive memory arrays"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I98352["Lee, W."],
    ag__R8434__has_title="Varistor-type bidirectional switch (JMAX>107A/cm2 , selectivity ∼104 ) for 3D bipolar resistive memory arrays",
    ag__R8435__has_year=2012,
    R61856__has_memristor_stack=I89412["Pt/TaOx/TiO2/TaOx/Pt"],
    
)


# 2019_xia 
I35052["Choi, B. J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Choi, B. J.",
    
)


# 2019_xia 
I17370["publication: Trilayer tunnel selectors for memristor memory cells"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I35052["Choi, B. J."],
    ag__R8434__has_title="Trilayer tunnel selectors for memristor memory cells",
    ag__R8435__has_year=2016,
    R61856__has_memristor_stack=I37641["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"],
    
)


# 2019_xia 
I34753["Kawahara, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kawahara, A.",
    
)


# 2019_xia 
I97500["publication: An 8 Mb multi-layered cross-point ReRAM macro with 443 MB/s write throughput"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I34753["Kawahara, A."],
    ag__R8434__has_title="An 8 Mb multi-layered cross-point ReRAM macro with 443 MB/s write throughput",
    ag__R8435__has_year=2013,
    R61856__has_memristor_stack=I14062["TaN/SiNx/TaN"],
    
)


# 2019_xia 
I13780["publication: Termally stable integrated Se-based OTS selectors with >20MA/cm2 current drive, >3.103 half-bias nonlinearity, tunable threshold voltage and excellent endurance"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I99774["Govoreanu, B."],
    ag__R8434__has_title="Termally stable integrated Se-based OTS selectors with >20MA/cm2 current drive, >3.103 half-bias nonlinearity, tunable threshold voltage and excellent endurance",
    ag__R8435__has_year=2017,
    R61856__has_memristor_stack=I20402["TiN/GexSe1-x/TiN"],
    
)


# 2019_xia 
I67979["Kim, S. G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kim, S. G.",
    
)


# 2019_xia 
I28644["publication: Breakthrough of selector technology for cross-point 25-nm ReRAM"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I67979["Kim, S. G."],
    ag__R8434__has_title="Breakthrough of selector technology for cross-point 25-nm ReRAM",
    ag__R8435__has_year=2017,
    R61856__has_memristor_stack=I6089["TiN/As:SiO2/TiN"],
    
)


# 2019_xia 
I89226["Son, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Son, M.",
    
)


# 2019_xia 
I73977["publication: Excellent selector characteristics of nanoscale VO2 for high-density bipolar ReRAM applications"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I89226["Son, M."],
    ag__R8434__has_title="Excellent selector characteristics of nanoscale VO2 for high-density bipolar ReRAM applications",
    ag__R8435__has_year=2011,
    R61856__has_memristor_stack=I74560["Pt/VO2/Pt"],
    
)


# 2019_xia 
I86966["Kim, W. G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kim, W. G.",
    
)


# 2019_xia 
I35602["publication: NbO2-based low power and cost efective 1S1R switching for high density cross point ReRAM application"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I86966["Kim, W. G."],
    ag__R8434__has_title="NbO2-based low power and cost efective 1S1R switching for high density cross point ReRAM application",
    ag__R8435__has_year=2014,
    R61856__has_memristor_stack=I48450["TiN/NbO2/TiN"],
    
)


# 2019_xia 
I48336["Cha, E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Cha, E.",
    
)


# 2019_xia 
I67839["publication: Nanoscale (∼10nm) 3D vertical ReRAM and NbO2 threshold selector with TiN electrode"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I48336["Cha, E."],
    ag__R8434__has_title="Nanoscale (∼10nm) 3D vertical ReRAM and NbO2 threshold selector with TiN electrode",
    ag__R8435__has_year=2013,
    R61856__has_memristor_stack=I35200["TiN/NbO2/W"],
    
)


# 2019_xia 
I71990["Lee, M.-J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Lee, M.-J.",
    
)


# 2019_xia 
I49726["publication: Highly-scalable threshold switching select device based on chalcogenide glasses for 3D nanoscaled memory arrays"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I71990["Lee, M.-J."],
    ag__R8434__has_title="Highly-scalable threshold switching select device based on chalcogenide glasses for 3D nanoscaled memory arrays",
    ag__R8435__has_year=2012,
    R61856__has_memristor_stack=I10099["TiN/AsTeGeSiN/TiN"],
    
)


# 2019_xia 
I42524["Sun, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Sun, J.",
    
)


# 2019_xia 
I85749["publication: Physically transient threshold switching device based on magnesium oxide for security application"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I42524["Sun, J."],
    ag__R8434__has_title="Physically transient threshold switching device based on magnesium oxide for security application",
    ag__R8435__has_year=2018,
    R61856__has_memristor_stack=I93835["W/Ag/MgO/Ag/W"],
    
)


# 2019_xia 
I57207["Wang, G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wang, G.",
    
)


# 2019_xia 
I27754["publication: High‐performance and low‐power rewritable SiO*x* 1 kbit one diode–one resistor crossbar memory array"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I57207["Wang, G."],
    ag__R8434__has_title="High‐performance and low‐power rewritable SiO*x* 1 kbit one diode–one resistor crossbar memory array",
    ag__R8435__has_year=2013,
    
)


# 2019_xia 
I46324["publication: Vacancy-modulated conductive oxide resistive RAM (VMCO-RRAM): an area-scalable switching current, self-compliant, highly nonlinear and wide on/of-window resistive switching cell"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I99774["Govoreanu, B."],
    ag__R8434__has_title="Vacancy-modulated conductive oxide resistive RAM (VMCO-RRAM): an area-scalable switching current, self-compliant, highly nonlinear and wide on/of-window resistive switching cell",
    ag__R8435__has_year=2013,
    R61856__has_memristor_stack=I40761["TiN/Al2O3/TiO2/TiN"],
    
)


# 2019_xia 
I10365["Song, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Song, M.",
    
)


# 2019_xia 
I20852["publication: Self-selective characteristics of nanoscale VOx devices for high-density ReRAM applications"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I10365["Song, M."],
    ag__R8434__has_title="Self-selective characteristics of nanoscale VOx devices for high-density ReRAM applications",
    ag__R8435__has_year=2012,
    R61856__has_memristor_stack=I53237["W/VOx/Pt"],
    
)


# 2019_xia 
I88598["Lu, D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Lu, D.",
    
)


# 2019_xia 
I53525["publication: Investigations of conduction mechanisms of the self-rectifying n<sup>+</sup>Si-HfO2-Ni RRAM devices"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I88598["Lu, D."],
    ag__R8434__has_title="Investigations of conduction mechanisms of the self-rectifying n<sup>+</sup>Si-HfO2-Ni RRAM devices",
    ag__R8435__has_year=2014,
    R61856__has_memristor_stack=I70091["Ni/HfO2/n-Si"],
    
)


# 2019_xia 
I67488["Wang, M. J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wang, M. J.",
    
)


# 2019_xia 
I30209["Gao, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Gao, S.",
    
)


# 2019_xia 
I92507["Zeng, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Zeng, F.",
    
)


# 2019_xia 
I92352["Song, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Song, C.",
    
)


# 2019_xia 
I87241["Pan, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Pan, F.",
    
)


# 2019_xia 
I4356["publication: Unipolar resistive switching with forming-free and self-rectifying efects in Cu/HfO2/n-Si devices"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I67488["Wang, M. J."], I30209["Gao, S."], I92507["Zeng, F."], I92352["Song, C."], I87241["Pan, F."]],
    ag__R8434__has_title="Unipolar resistive switching with forming-free and self-rectifying efects in Cu/HfO2/n-Si devices",
    ag__R8435__has_year=2016,
    R61856__has_memristor_stack=I88150["Cu/HfO2/n-Si"],
    
)


# 2019_xia 
I77819["Kim, K.-H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kim, K.-H.",
    
)


# 2019_xia 
I39850["Jo, S. H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Jo, S. H.",
    
)


# 2019_xia 
I58824["Gaba, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Gaba, S.",
    
)


# 2019_xia 
I2160["Lu, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Lu, W.",
    
)


# 2019_xia 
I45125["publication: Nanoscale resistive memory with intrinsic diode characteristics and long endurance"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I77819["Kim, K.-H."], I39850["Jo, S. H."], I58824["Gaba, S."], I2160["Lu, W."]],
    ag__R8434__has_title="Nanoscale resistive memory with intrinsic diode characteristics and long endurance",
    ag__R8435__has_year=2010,
    R61856__has_memristor_stack=I30588["Ag/a-Si/p-poly-Si"],
    
)


# 2019_xia 
I2579["Ni/TiO2/Ni"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I2579["Ni/TiO2/Ni"].set_relation(R66928["has stack component"], omt.I87636["nickel"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I2579["Ni/TiO2/Ni"].set_relation(R66928["has stack component"], omt.I87636["nickel"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I2579["Ni/TiO2/Ni"].set_relation(R66928["has stack component"], omt.I6119["TiO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_xia 
I25766["Pt/TiO2/TiN"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I25766["Pt/TiO2/TiN"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I25766["Pt/TiO2/TiN"].set_relation(R66928["has stack component"], omt.I6119["TiO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I25766["Pt/TiO2/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019_xia 
I53423["TiN/Ta2O5/TiN"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I53423["TiN/Ta2O5/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I53423["TiN/Ta2O5/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I53423["TiN/Ta2O5/TiN"].set_relation(R66928["has stack component"], omt.I6123["Ta2O5"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_xia 



# 2019_xia 
I16044["W/Ta2O5/TaOx/TiO2/TiN"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I16044["W/Ta2O5/TaOx/TiO2/TiN"].set_relation(R66928["has stack component"], omt.I41958["tungsten"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I16044["W/Ta2O5/TaOx/TiO2/TiN"].set_relation(R66928["has stack component"], omt.I6123["Ta2O5"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I16044["W/Ta2O5/TaOx/TiO2/TiN"].set_relation(R66928["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I16044["W/Ta2O5/TaOx/TiO2/TiN"].set_relation(R66928["has stack component"], omt.I6119["TiO2"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I16044["W/Ta2O5/TaOx/TiO2/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(4), is_at_outer_position(True), ])


# 2019_xia 
I89412["Pt/TaOx/TiO2/TaOx/Pt"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I89412["Pt/TaOx/TiO2/TaOx/Pt"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I89412["Pt/TaOx/TiO2/TaOx/Pt"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(4), is_at_outer_position(True), ])
I89412["Pt/TaOx/TiO2/TaOx/Pt"].set_relation(R66928["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I89412["Pt/TaOx/TiO2/TaOx/Pt"].set_relation(R66928["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I89412["Pt/TaOx/TiO2/TaOx/Pt"].set_relation(R66928["has stack component"], omt.I6119["TiO2"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019_xia 
I37641["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I37641["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I37641["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(4), is_at_outer_position(True), ])
I37641["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"].set_relation(R66928["has stack component"], omt.I6124["TaN1+x"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I37641["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"].set_relation(R66928["has stack component"], omt.I6124["TaN1+x"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I37641["Pt/TaN1+x/Ta2O5/TaN1+x/Pt"].set_relation(R66928["has stack component"], omt.I6123["Ta2O5"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019_xia 



# 2019_xia 
I14062["TaN/SiNx/TaN"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I14062["TaN/SiNx/TaN"].set_relation(R66928["has stack component"], omt.I6125["TaN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I14062["TaN/SiNx/TaN"].set_relation(R66928["has stack component"], omt.I6125["TaN"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I14062["TaN/SiNx/TaN"].set_relation(R66928["has stack component"], omt.I6126["SiNx"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_xia 



# 2019_xia 
I20402["TiN/GexSe1-x/TiN"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I20402["TiN/GexSe1-x/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I20402["TiN/GexSe1-x/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I20402["TiN/GexSe1-x/TiN"].set_relation(R66928["has stack component"], omt.I6130["GexSe1-x"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_xia 
omt.I6130["GexSe1-x"].update_relations(
    R4__is_instance_of=I86037["stack component"],
    
)


# 2019_xia 
I6089["TiN/As:SiO2/TiN"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I6089["TiN/As:SiO2/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I6089["TiN/As:SiO2/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I6089["TiN/As:SiO2/TiN"].set_relation(R66928["has stack component"], omt.I6131["As:SiO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_xia 
omt.I6131["As:SiO2"].update_relations(
    R4__is_instance_of=I86037["stack component"],
    
)


# 2019_xia 
I74560["Pt/VO2/Pt"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I74560["Pt/VO2/Pt"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I74560["Pt/VO2/Pt"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I74560["Pt/VO2/Pt"].set_relation(R66928["has stack component"], omt.I6132["VO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_xia 



# 2019_xia 
I48450["TiN/NbO2/TiN"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I48450["TiN/NbO2/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I48450["TiN/NbO2/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I48450["TiN/NbO2/TiN"].set_relation(R66928["has stack component"], omt.I6133["NbO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_xia 



# 2019_xia 
I35200["TiN/NbO2/W"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I35200["TiN/NbO2/W"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I35200["TiN/NbO2/W"].set_relation(R66928["has stack component"], omt.I6133["NbO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I35200["TiN/NbO2/W"].set_relation(R66928["has stack component"], omt.I41958["tungsten"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019_xia 
I10099["TiN/AsTeGeSiN/TiN"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I10099["TiN/AsTeGeSiN/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I10099["TiN/AsTeGeSiN/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I10099["TiN/AsTeGeSiN/TiN"].set_relation(R66928["has stack component"], omt.I6149["AsTeGeSiN"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_xia 



# 2019_xia 
I93835["W/Ag/MgO/Ag/W"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I93835["W/Ag/MgO/Ag/W"].set_relation(R66928["has stack component"], omt.I41958["tungsten"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I93835["W/Ag/MgO/Ag/W"].set_relation(R66928["has stack component"], omt.I41958["tungsten"], qualifiers=[has_position(4), is_at_outer_position(True), ])
I93835["W/Ag/MgO/Ag/W"].set_relation(R66928["has stack component"], omt.I93439["silver"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I93835["W/Ag/MgO/Ag/W"].set_relation(R66928["has stack component"], omt.I93439["silver"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I93835["W/Ag/MgO/Ag/W"].set_relation(R66928["has stack component"], omt.I6135["MgO"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019_xia 



# 2019_xia 



# 2019_xia 
I71427["Pt/Ag:SiOxNy/Pt"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I71427["Pt/Ag:SiOxNy/Pt"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I71427["Pt/Ag:SiOxNy/Pt"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(2), is_at_outer_position(True), ])
I71427["Pt/Ag:SiOxNy/Pt"].set_relation(R66928["has stack component"], omt.I6150["Ag:SiOxNy"], qualifiers=[has_position(1), is_at_outer_position(False), ])


# 2019_xia 
omt.I6150["Ag:SiOxNy"].update_relations(
    R4__is_instance_of=I86037["stack component"],
    
)


# 2019_xia 
I77342["Pd/Ag/HfO2/Ag/Pd"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I77342["Pd/Ag/HfO2/Ag/Pd"].set_relation(R66928["has stack component"], omt.I60065["palladium"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I77342["Pd/Ag/HfO2/Ag/Pd"].set_relation(R66928["has stack component"], omt.I60065["palladium"], qualifiers=[has_position(4), is_at_outer_position(True), ])
I77342["Pd/Ag/HfO2/Ag/Pd"].set_relation(R66928["has stack component"], omt.I93439["silver"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I77342["Pd/Ag/HfO2/Ag/Pd"].set_relation(R66928["has stack component"], omt.I93439["silver"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I77342["Pd/Ag/HfO2/Ag/Pd"].set_relation(R66928["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019_xia 



# 2019_xia 
I40761["TiN/Al2O3/TiO2/TiN"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I40761["TiN/Al2O3/TiO2/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I40761["TiN/Al2O3/TiO2/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I40761["TiN/Al2O3/TiO2/TiN"].set_relation(R66928["has stack component"], omt.I6100["Al2O3"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I40761["TiN/Al2O3/TiO2/TiN"].set_relation(R66928["has stack component"], omt.I6119["TiO2"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2019_xia 
I53237["W/VOx/Pt"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I53237["W/VOx/Pt"].set_relation(R66928["has stack component"], omt.I41958["tungsten"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I53237["W/VOx/Pt"].set_relation(R66928["has stack component"], omt.I6140["VOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I53237["W/VOx/Pt"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019_xia 



# 2019_xia 
I26254["p-Si/SiO2/n-Si"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I26254["p-Si/SiO2/n-Si"].set_relation(R66928["has stack component"], omt.I6141["p-Si"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I26254["p-Si/SiO2/n-Si"].set_relation(R66928["has stack component"], omt.I6111["SiO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I26254["p-Si/SiO2/n-Si"].set_relation(R66928["has stack component"], omt.I6142["n-Si"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019_xia 
omt.I6141["p-Si"].update_relations(
    R4__is_instance_of=I86037["stack component"],
    
)


# 2019_xia 



# 2019_xia 
omt.I6142["n-Si"].update_relations(
    R4__is_instance_of=I86037["stack component"],
    
)


# 2019_xia 
I70091["Ni/HfO2/n-Si"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I70091["Ni/HfO2/n-Si"].set_relation(R66928["has stack component"], omt.I87636["nickel"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I70091["Ni/HfO2/n-Si"].set_relation(R66928["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I70091["Ni/HfO2/n-Si"].set_relation(R66928["has stack component"], omt.I6142["n-Si"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019_xia 
I88150["Cu/HfO2/n-Si"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I88150["Cu/HfO2/n-Si"].set_relation(R66928["has stack component"], omt.I23950["copper"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I88150["Cu/HfO2/n-Si"].set_relation(R66928["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I88150["Cu/HfO2/n-Si"].set_relation(R66928["has stack component"], omt.I6142["n-Si"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019_xia 



# 2019_xia 
I30588["Ag/a-Si/p-poly-Si"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I30588["Ag/a-Si/p-poly-Si"].set_relation(R66928["has stack component"], omt.I93439["silver"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I30588["Ag/a-Si/p-poly-Si"].set_relation(R66928["has stack component"], omt.I6143["a-Si"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I30588["Ag/a-Si/p-poly-Si"].set_relation(R66928["has stack component"], omt.I6144["p-poly-Si"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2019_xia 
omt.I6143["a-Si"].update_relations(
    R4__is_instance_of=I86037["stack component"],
    
)


# 2019_xia 
omt.I6144["p-poly-Si"].update_relations(
    R4__is_instance_of=I86037["stack component"],
    
)


# 2024_aguirre 
I3720["Fernando Aguirre"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Fernando Aguirre",
    
)


# 2024_aguirre 
I22285["Abu Sebastian"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Abu Sebastian",
    
)


# 2024_aguirre 
I37624["publication: Hardware implementation of memristorbased artificial neural networks"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I3720["Fernando Aguirre"], I22285["Abu Sebastian"]],
    ag__R8434__has_title="Hardware implementation of memristorbased artificial neural networks",
    ag__R8435__has_year=2024,
    R14118__has_internal_reference="2024_aguirre_et_al",
    
)
I37624["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I31560["publication: Fully hardware-implemented memristor convolutional neural network"], qualifiers=[has_citation_id(55), ])
I37624["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I93515["publication: A fully integrated reprogrammable memristor-CMOS system for efficient multiply-accumulate operations"], qualifiers=[has_citation_id(57), ])
I37624["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I80832["publication: A compute-in-memory chip based on resistive random-access memory"], qualifiers=[has_citation_id(60), ])
I37624["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I54461["publication: A 4M synapses integrated analog ReRAM based 66.5 TOPS/W neural-network processor with cell current controlled writing and flexible network architecture"], qualifiers=[has_citation_id(99), ])
I37624["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I39407["publication: A 462GOPs/J RRAM-based nonvolatile intelligent processor for energy harvesting IoE system featuring nonvolatile logics and processing-in-memory"], qualifiers=[has_citation_id(100), ])
I37624["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I91491["publication: A fully hardware-based memristive multilayer neural network"], qualifiers=[has_citation_id(102), ])
I37624["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I4359["publication: CMOS-integrated nanoscale memristive crossbars for CNN and optimization acceleration"], qualifiers=[has_citation_id(113), ])
I37624["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I98302["publication: Redundancy and analog slicing for precise inmemory machine learning - Part I: Programming techniques"], qualifiers=[has_citation_id(114), ])
I37624["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I23498["publication: Redundancy and analog slicing for precise inmemory machine learning - Part II: Applications and benchmark"], qualifiers=[has_citation_id(115), ])
I37624["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I4363["publication: Fully memristive neural networks for pattern classification with unsupervised learning"], qualifiers=[has_citation_id(116), ])
I37624["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I63365["publication: In-memory and error-immune differential RRAM implementation of binarized deep neural networks"], qualifiers=[has_citation_id(123), ])
I37624["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I40375["publication: CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors"], qualifiers=[has_citation_id(219), ])
I37624["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I68972["publication: Digital biologically plausible implementation of binarized neural networks with differential hafnium oxide resistive memory arrays"], qualifiers=[has_citation_id(272), ])
I37624["publication: Hardware implementation of memristorbased artificial neural networks"].set_relation(ag.R8440["cites"], I88419["publication: A 43pJ/Cycle Non-Volatile Microcontroller with 4.7μs Shutdown/Wake-up Integrating 2.3-bit/Cell Resistive RAM and Resilience Techniques"], qualifiers=[has_citation_id(274), ])


# 2024_aguirre 
I51553["Yao, P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Yao, P.",
    
)


# 2024_aguirre 
I31560["publication: Fully hardware-implemented memristor convolutional neural network"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I51553["Yao, P."],
    ag__R8434__has_title="Fully hardware-implemented memristor convolutional neural network",
    ag__R8435__has_year=2020,
    R61856__has_memristor_stack=I13120["TiN/TaOx/HfOx/TiN"],
    
)


# 2024_aguirre 
I20607["Cai, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Cai, F.",
    
)


# 2024_aguirre 
I93515["publication: A fully integrated reprogrammable memristor-CMOS system for efficient multiply-accumulate operations"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I20607["Cai, F."],
    ag__R8434__has_title="A fully integrated reprogrammable memristor-CMOS system for efficient multiply-accumulate operations",
    ag__R8435__has_year=2019,
    R61856__has_memristor_stack=I4397["Au/Pd/WOx/Au"],
    
)


# 2024_aguirre 
I70002["Wan, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wan, W.",
    
)


# 2024_aguirre 
I80832["publication: A compute-in-memory chip based on resistive random-access memory"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I70002["Wan, W."],
    ag__R8434__has_title="A compute-in-memory chip based on resistive random-access memory",
    ag__R8435__has_year=2022,
    R61856__has_memristor_stack=I72536["TiN/HfO2/TaOx/TiN"],
    
)


# 2024_aguirre 
I18561["Mochida, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Mochida, R.",
    
)


# 2024_aguirre 
I54461["publication: A 4M synapses integrated analog ReRAM based 66.5 TOPS/W neural-network processor with cell current controlled writing and flexible network architecture"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I18561["Mochida, R."],
    ag__R8434__has_title="A 4M synapses integrated analog ReRAM based 66.5 TOPS/W neural-network processor with cell current controlled writing and flexible network architecture",
    ag__R8435__has_year=2018,
    R61856__has_memristor_stack=I7666["W/Ta2O5/TaOx/W"],
    
)


# 2024_aguirre 
I58610["Su, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Su, F.",
    
)


# 2024_aguirre 
I39407["publication: A 462GOPs/J RRAM-based nonvolatile intelligent processor for energy harvesting IoE system featuring nonvolatile logics and processing-in-memory"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I58610["Su, F."],
    ag__R8434__has_title="A 462GOPs/J RRAM-based nonvolatile intelligent processor for energy harvesting IoE system featuring nonvolatile logics and processing-in-memory",
    ag__R8435__has_year=2017,
    R61856__has_memristor_stack=I51409["AlCu/TiN/Ti/HfO2/TiN"],
    
)


# 2024_aguirre 
I21668["Kiani, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kiani, F.",
    
)


# 2024_aguirre 
I25569["Yin, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Yin, J.",
    
)


# 2024_aguirre 
I26493["Joshua Yang, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Joshua Yang, J.",
    
)


# 2024_aguirre 
I84601["Xia, Q."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Xia, Q.",
    
)


# 2024_aguirre 
I91491["publication: A fully hardware-based memristive multilayer neural network"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I21668["Kiani, F."], I25569["Yin, J."], I60603["Wang, Z."], I26493["Joshua Yang, J."], I84601["Xia, Q."]],
    ag__R8434__has_title="A fully hardware-based memristive multilayer neural network",
    ag__R8435__has_year=2021,
    R61856__has_memristor_stack=I93517["Pt/Ta/Ta2O5/Pt/Ti"],
    
)


# 2024_aguirre 
I4359["publication: CMOS-integrated nanoscale memristive crossbars for CNN and optimization acceleration"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I71085["Li, C."],
    ag__R8434__has_title="CMOS-integrated nanoscale memristive crossbars for CNN and optimization acceleration",
    ag__R8435__has_year=2020,
    R61856__has_memristor_stack=I44506["Ta/TaOx/Pt"],
    
)


# 2024_aguirre 
I78655["Pedretti, G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Pedretti, G.",
    
)


# 2024_aguirre 
I98302["publication: Redundancy and analog slicing for precise inmemory machine learning - Part I: Programming techniques"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I78655["Pedretti, G."],
    ag__R8434__has_title="Redundancy and analog slicing for precise inmemory machine learning - Part I: Programming techniques",
    ag__R8435__has_year=2021,
    
)


# 2024_aguirre 
I23498["publication: Redundancy and analog slicing for precise inmemory machine learning - Part II: Applications and benchmark"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I78655["Pedretti, G."],
    ag__R8434__has_title="Redundancy and analog slicing for precise inmemory machine learning - Part II: Applications and benchmark",
    ag__R8435__has_year=2021,
    
)


# 2024_aguirre 
I4363["publication: Fully memristive neural networks for pattern classification with unsupervised learning"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I60603["Wang, Z."],
    ag__R8434__has_title="Fully memristive neural networks for pattern classification with unsupervised learning",
    ag__R8435__has_year=2018,
    R61856__has_memristor_stack=[I58973["Pt/SiOxAg/Pt/Ti"], I62232["Ta/Pd/HfO2/Pt/Ti"]],
    
)


# 2024_aguirre 
I75344["Bocquet, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Bocquet, M.",
    
)


# 2024_aguirre 
I63365["publication: In-memory and error-immune differential RRAM implementation of binarized deep neural networks"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I75344["Bocquet, M."],
    ag__R8434__has_title="In-memory and error-immune differential RRAM implementation of binarized deep neural networks",
    ag__R8435__has_year=2018,
    R61856__has_memristor_stack=I1438["TiN/HfO2/Ti/TiN"],
    
)


# 2024_aguirre 
I70153["Chen, W. H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Chen, W. H.",
    
)


# 2024_aguirre 
I40375["publication: CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I70153["Chen, W. H."],
    ag__R8434__has_title="CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors",
    ag__R8435__has_year=2019,
    R61856__has_memristor_stack=I86897["W/TiN/TiON"],
    
)


# 2024_aguirre 
I7400["Hirtzlin, T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Hirtzlin, T.",
    
)


# 2024_aguirre 
I68972["publication: Digital biologically plausible implementation of binarized neural networks with differential hafnium oxide resistive memory arrays"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I7400["Hirtzlin, T."],
    ag__R8434__has_title="Digital biologically plausible implementation of binarized neural networks with differential hafnium oxide resistive memory arrays",
    ag__R8435__has_year=2020,
    R61856__has_memristor_stack=I1438["TiN/HfO2/Ti/TiN"],
    
)


# 2024_aguirre 
I54872["Wu, T. F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wu, T. F.",
    
)


# 2024_aguirre 
I88419["publication: A 43pJ/Cycle Non-Volatile Microcontroller with 4.7μs Shutdown/Wake-up Integrating 2.3-bit/Cell Resistive RAM and Resilience Techniques"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I54872["Wu, T. F."],
    ag__R8434__has_title="A 43pJ/Cycle Non-Volatile Microcontroller with 4.7μs Shutdown/Wake-up Integrating 2.3-bit/Cell Resistive RAM and Resilience Techniques",
    ag__R8435__has_year=2019,
    R61856__has_memristor_stack=I1438["TiN/HfO2/Ti/TiN"],
    
)


# 2024_aguirre 
I4397["Au/Pd/WOx/Au"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I4397["Au/Pd/WOx/Au"].set_relation(R66928["has stack component"], omt.I54426["gold"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I4397["Au/Pd/WOx/Au"].set_relation(R66928["has stack component"], omt.I54426["gold"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I4397["Au/Pd/WOx/Au"].set_relation(R66928["has stack component"], omt.I60065["palladium"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I4397["Au/Pd/WOx/Au"].set_relation(R66928["has stack component"], omt.I6146["WOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2024_aguirre 



# 2024_aguirre 



# 2024_aguirre 
I13120["TiN/TaOx/HfOx/TiN"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I13120["TiN/TaOx/HfOx/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I13120["TiN/TaOx/HfOx/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I13120["TiN/TaOx/HfOx/TiN"].set_relation(R66928["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I13120["TiN/TaOx/HfOx/TiN"].set_relation(R66928["has stack component"], omt.I6105["HfOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2024_aguirre 
I93517["Pt/Ta/Ta2O5/Pt/Ti"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I93517["Pt/Ta/Ta2O5/Pt/Ti"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I93517["Pt/Ta/Ta2O5/Pt/Ti"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I93517["Pt/Ta/Ta2O5/Pt/Ti"].set_relation(R66928["has stack component"], omt.I38968["tantalum"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I93517["Pt/Ta/Ta2O5/Pt/Ti"].set_relation(R66928["has stack component"], omt.I6123["Ta2O5"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I93517["Pt/Ta/Ta2O5/Pt/Ti"].set_relation(R66928["has stack component"], omt.I87594["titanium"], qualifiers=[has_position(4), is_at_outer_position(True), ])


# 2024_aguirre 
I44506["Ta/TaOx/Pt"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I44506["Ta/TaOx/Pt"].set_relation(R66928["has stack component"], omt.I38968["tantalum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I44506["Ta/TaOx/Pt"].set_relation(R66928["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I44506["Ta/TaOx/Pt"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2024_aguirre 
I86897["W/TiN/TiON"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I86897["W/TiN/TiON"].set_relation(R66928["has stack component"], omt.I41958["tungsten"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I86897["W/TiN/TiON"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I86897["W/TiN/TiON"].set_relation(R66928["has stack component"], omt.I6147["TiON"], qualifiers=[has_position(2), is_at_outer_position(True), ])


# 2024_aguirre 



# 2024_aguirre 
I58973["Pt/SiOxAg/Pt/Ti"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I58973["Pt/SiOxAg/Pt/Ti"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I58973["Pt/SiOxAg/Pt/Ti"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I58973["Pt/SiOxAg/Pt/Ti"].set_relation(R66928["has stack component"], omt.I6151["SiOxAg"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I58973["Pt/SiOxAg/Pt/Ti"].set_relation(R66928["has stack component"], omt.I87594["titanium"], qualifiers=[has_position(3), is_at_outer_position(True), ])


# 2024_aguirre 
omt.I6151["SiOxAg"].update_relations(
    R4__is_instance_of=I86037["stack component"],
    
)


# 2024_aguirre 
I62232["Ta/Pd/HfO2/Pt/Ti"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I62232["Ta/Pd/HfO2/Pt/Ti"].set_relation(R66928["has stack component"], omt.I38968["tantalum"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I62232["Ta/Pd/HfO2/Pt/Ti"].set_relation(R66928["has stack component"], omt.I60065["palladium"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I62232["Ta/Pd/HfO2/Pt/Ti"].set_relation(R66928["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I62232["Ta/Pd/HfO2/Pt/Ti"].set_relation(R66928["has stack component"], omt.I4374["platinum"], qualifiers=[has_position(3), is_at_outer_position(False), ])
I62232["Ta/Pd/HfO2/Pt/Ti"].set_relation(R66928["has stack component"], omt.I87594["titanium"], qualifiers=[has_position(4), is_at_outer_position(True), ])


# 2024_aguirre 
I1438["TiN/HfO2/Ti/TiN"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I1438["TiN/HfO2/Ti/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I1438["TiN/HfO2/Ti/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I1438["TiN/HfO2/Ti/TiN"].set_relation(R66928["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I1438["TiN/HfO2/Ti/TiN"].set_relation(R66928["has stack component"], omt.I87594["titanium"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2024_aguirre 
I7666["W/Ta2O5/TaOx/W"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I7666["W/Ta2O5/TaOx/W"].set_relation(R66928["has stack component"], omt.I41958["tungsten"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I7666["W/Ta2O5/TaOx/W"].set_relation(R66928["has stack component"], omt.I41958["tungsten"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I7666["W/Ta2O5/TaOx/W"].set_relation(R66928["has stack component"], omt.I6123["Ta2O5"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I7666["W/Ta2O5/TaOx/W"].set_relation(R66928["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])


# 2024_aguirre 
I51409["AlCu/TiN/Ti/HfO2/TiN"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I51409["AlCu/TiN/Ti/HfO2/TiN"].set_relation(R66928["has stack component"], omt.I6148["AlCu"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I51409["AlCu/TiN/Ti/HfO2/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I51409["AlCu/TiN/Ti/HfO2/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(4), is_at_outer_position(True), ])
I51409["AlCu/TiN/Ti/HfO2/TiN"].set_relation(R66928["has stack component"], omt.I87594["titanium"], qualifiers=[has_position(2), is_at_outer_position(False), ])
I51409["AlCu/TiN/Ti/HfO2/TiN"].set_relation(R66928["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(3), is_at_outer_position(False), ])


# 2024_aguirre 



# 2024_aguirre 
I72536["TiN/HfO2/TaOx/TiN"].update_relations(
    R4__is_instance_of=I1623["memristor stack"],
    
)
I72536["TiN/HfO2/TaOx/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(0), is_at_outer_position(True), ])
I72536["TiN/HfO2/TaOx/TiN"].set_relation(R66928["has stack component"], omt.I6118["TiN"], qualifiers=[has_position(3), is_at_outer_position(True), ])
I72536["TiN/HfO2/TaOx/TiN"].set_relation(R66928["has stack component"], omt.I6104["HfO2"], qualifiers=[has_position(1), is_at_outer_position(False), ])
I72536["TiN/HfO2/TaOx/TiN"].set_relation(R66928["has stack component"], omt.I6115["TaOx"], qualifiers=[has_position(2), is_at_outer_position(False), ])




p.end_mod()