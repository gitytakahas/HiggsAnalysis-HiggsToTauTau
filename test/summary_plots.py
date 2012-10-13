from optparse import OptionParser, OptionGroup

## set up the option parser
parser = OptionParser(usage="usage: %prog [options]",
                      description="Script to combine 2011+2012 and high and low pt event categories. This script requires that the script run_macros.py has been executed beforehand and produced resultrs w/o issues.")
## direct options
parser.add_option("-a", "--analysis", dest="analysis", default="sm", type="choice", help="Type of analysis (sm or mssm). Lower case is required. [Default: sm]", choices=["sm", "mssm"])
parser.add_option("-t", "--type", dest="type", default="rescaled", type="string", help="Type of plots, unscaled or rescaled. [Default: \"rescaled\"]")
## check number of arguments; in case print usage
(options, args) = parser.parse_args()


## a set of pre-defined lists
channels   = [
    "emu",
    "eTau",
    "muTau",
    #"mumu",
    ]

categories_sm = [
    "0jet_low",
    "0jet_high",
    "0jet",
    "boost_low",
    "boost_high",
    "boost",
    "vbf",
    ]

categories_mssm = [
    "0jet_low",
    "0jet_high",
    "0jet",
    "boost_low",
    "boost_high",
    "boost",
    "btag_low",
    "btag_high",
    "btag",
    ] 

extra = {
    "emu"   : "#tau_{e}#tau_{#mu}",
    "eTau"  : "#tau_{e}#tau_{h}",
    "muTau" : "#tau_{#mu}#tau_{h}",
    "mumu"  : "#tau_{#mu}#tau_{#mu}",
    }

log = {
    ("emu"  , "0jet_low"  ) : "true",
    ("emu"  , "0jet_high" ) : "false",
    ("emu"  , "0jet"      ) : "true", 
    ("emu"  , "boost_low" ) : "false",
    ("emu"  , "boost_high") : "false",
    ("emu"  , "boost"     ) : "false",
    ("emu"  , "btag_low"  ) : "false",
    ("emu"  , "btag_high" ) : "false",
    ("emu"  , "btag"      ) : "false",
    ("emu"  , "vbf"       ) : "false",
    ("muTau", "0jet_low"  ) : "false",
    ("muTau", "0jet_high" ) : "false",
    ("muTau", "0jet"      ) : "false", 
    ("muTau", "boost_low" ) : "false",
    ("muTau", "boost_high") : "false",
    ("muTau", "boost"     ) : "false",
    ("muTau", "btag_low"  ) : "false",
    ("muTau", "btag_high" ) : "false",
    ("muTau", "btag"      ) : "false",    
    ("muTau", "vbf"       ) : "false",
    ("eTau" , "0jet_low"  ) : "false",
    ("eTau" , "0jet_high" ) : "false",
    ("eTau" , "0jet"      ) : "false", 
    ("eTau" , "boost_low" ) : "false",
    ("eTau" , "boost_high") : "false",
    ("eTau" , "boost"     ) : "false",
    ("eTau" , "btag_low"  ) : "false",
    ("eTau" , "btag_high" ) : "false",
    ("eTau" , "btag"      ) : "false",
    ("eTau" , "vbf"       ) : "false",
    ("mumu" , "0jet_low"  ) : "true",
    ("mumu" , "0jet_high" ) : "true",
    ("mumu" , "0jet"      ) : "true", 
    ("mumu" , "boost_low" ) : "true",
    ("mumu" , "boost_high") : "true",
    ("mumu" , "boost"     ) : "true",
    ("mumu" , "btag_low"  ) : "true",
    ("mumu" , "btag_high" ) : "true",
    ("mumu" , "btag"      ) : "true",
    ("mumu" , "vbf"       ) : "false",    
    }

max = {
    ("emu"  , "0jet_low"  ) : "-1",
    ("emu"  , "0jet_high" ) : "-1",
    ("emu"  , "0jet"      ) : "-1",
    ("emu"  , "boost_low" ) : "-1",
    ("emu"  , "boost_high") : "-1",
    ("emu"  , "boost"     ) : "-1",
    ("emu"  , "btag_low"  ) : "-1",
    ("emu"  , "btag_high" ) : "-1",
    ("emu"  , "btag"      ) : "-1",
    ("emu"  , "vbf"       ) : "-1",
    ("muTau", "0jet_low"  ) : "-1",
    ("muTau", "0jet_high" ) : "-1",
    ("muTau", "0jet"      ) : "-1",
    ("muTau", "boost_low" ) : "-1",
    ("muTau", "boost_high") : "-1",
    ("muTau", "boost"     ) : "-1",
    ("muTau", "btag_low"  ) : "-1",
    ("muTau", "btag_high" ) : "-1",
    ("muTau", "btag"      ) : "-1",
    ("muTau", "vbf"       ) : "-1", 
    ("eTau" , "0jet_low"  ) : "-1",
    ("eTau" , "0jet_high" ) : "-1",
    ("eTau" , "0jet"      ) : "-1",
    ("eTau" , "boost_low" ) : "-1",
    ("eTau" , "boost_high") : "-1",
    ("eTau" , "boost"     ) : "-1",
    ("eTau" , "btag_low"  ) : "-1",
    ("eTau" , "btag_high" ) : "-1",
    ("eTau" , "btag"      ) : "-1",
    ("eTau" , "vbf"       ) : "-1",
    ("mumu" , "0jet_low"  ) : "-1",
    ("mumu" , "0jet_high" ) : "-1",
    ("mumu" , "0jet"      ) : "-1",
    ("mumu" , "boost_low" ) : "-1",
    ("mumu" , "boost_high") : "-1",
    ("mumu" , "boost"     ) : "-1",
    ("mumu" , "btag_low"  ) : "-1",
    ("mumu" , "btag_high" ) : "-1",
    ("mumu" , "btag"      ) : "-1",
    ("mumu" , "vbf"       ) : "-1",
    }

min = {
    ("emu"  , "0jet_low"  ) : "0.1",
    ("emu"  , "0jet_high" ) : "0",
    ("emu"  , "0jet"      ) : "0.3", 
    ("emu"  , "boost_low" ) : "0",
    ("emu"  , "boost_high") : "0",
    ("emu"  , "boost"     ) : "0",
    ("emu"  , "btag_low"  ) : "0",
    ("emu"  , "btag_high" ) : "0",
    ("emu"  , "btag"      ) : "0",
    ("emu"  , "vbf"       ) : "0",
    ("muTau", "0jet_low"  ) : "0",
    ("muTau", "0jet_high" ) : "0",
    ("muTau", "0jet"      ) : "0", 
    ("muTau", "boost_low" ) : "0",
    ("muTau", "boost_high") : "0",
    ("muTau", "boost"     ) : "0",
    ("muTau", "btag_low"  ) : "0",
    ("muTau", "btag_high" ) : "0",
    ("muTau", "btag"      ) : "0",
    ("muTau", "vbf"       ) : "0",
    ("eTau" , "0jet_low"  ) : "0",
    ("eTau" , "0jet_high" ) : "0",
    ("eTau" , "0jet"      ) : "0", 
    ("eTau" , "boost_low" ) : "0",
    ("eTau" , "boost_high") : "0",
    ("eTau" , "boost"     ) : "0",
    ("eTau" , "btag_low"  ) : "0",
    ("eTau" , "btag_high" ) : "0",
    ("eTau" , "btag"      ) : "0",
    ("eTau" , "vbf"       ) : "0",
    ("mumu" , "0jet_low"  ) : "0.1",
    ("mumu" , "0jet_high" ) : "0",
    ("mumu" , "0jet"      ) : "0.3", 
    ("mumu" , "boost_low" ) : "0",
    ("mumu" , "boost_high") : "0",
    ("mumu" , "boost"     ) : "0",
    ("mumu" , "btag_low"  ) : "0",
    ("mumu" , "btag_high" ) : "0",
    ("mumu" , "btag"      ) : "0",
    ("mumu" , "vbf"       ) : "0",    
    }

import os

type = options.type
categories = categories_mssm if options.analysis == "mssm" else categories_mssm

## combine 2011+2012
for chn in channels :
    for cat in categories :
        ## combine high and low pt categories, make sure in your 
        ## list that {CAT}_low and {CAT}_high are run beforehand
        if cat == "0jet" or cat == "boost" or cat == "btag":
            #print "hadd {CHN}_{CAT}_{TYPE}_7+8TeV.root {CHN}_{CAT}_low_{TYPE}_7+8TeV.root {CHN}_{CAT}_high_{TYPE}_7+8TeV.root".format(CHN=chn, CAT=cat, TYPE=type)
            os.system("hadd -f {CHN}_{CAT}_{TYPE}_7+8TeV.root {CHN}_{CAT}_low_{TYPE}_7+8TeV.root {CHN}_{CAT}_high_{TYPE}_7+8TeV.root".format(CHN=chn, CAT=cat, TYPE=type))
        else :
            ## patch until Josh fixes his naming conventions
            if chn == "eTau" :
                #print "hadd {CHN}_{CAT}_{TYPE}_7+8TeV.root {CHN}_{CAT}_{TYPE}_7TeV_{LOG}.root eleTau_{CAT}_{TYPE}_8TeV_{LOG}.root".format(
                #    CHN=chn, CAT=cat, TYPE=type, LOG="" if log[(chn, cat)] else "") 
                os.system("hadd -f {CHN}_{CAT}_{TYPE}_7+8TeV.root {CHN}_{CAT}_{TYPE}_7TeV_*.root eleTau_{CAT}_{TYPE}_8TeV_*.root".format(
                    CHN=chn, CAT=cat, TYPE=type))#, LOG="LOG" if log[(chn, cat)]==True else ""))
            else:
                #print "hadd {CHN}_{CAT}_{TYPE}_7+8TeV.root {CHN}_{CAT}_{TYPE}_7TeV_{LOG}.root {CHN}_{CAT}_{TYPE}_8TeV_{LOG}.root".format(
                #    CHN=chn, CAT=cat, TYPE=type, LOG="LOG" if log[(chn, cat)] else "")
                os.system("hadd -f {CHN}_{CAT}_{TYPE}_7+8TeV.root {CHN}_{CAT}_{TYPE}_7TeV_*.root {CHN}_{CAT}_{TYPE}_8TeV_*.root".format(
                    CHN=chn, CAT=cat, TYPE=type))#, LOG="LOG" if log[(chn, cat)]==True else ""))
## make plots
for chn in channels :
    for cat in categories :
        print chn, cat
        os.system("root -l -q -b {CMSSW_BASE}/src/HiggsAnalysis/HiggsToTauTau/macros/postfit.C+\\(\\\"{CHN}_{CAT}_{TYPE}_7+8TeV.root\\\",\\\"{ANA}\\\",\\\"{LABEL}\\\",\\\"{EXTRA}\\\",{MIN},{MAX},{LOG}\)".format(CMSSW_BASE=os.environ['CMSSW_BASE'], CHN=chn, CAT=cat, TYPE=type, ANA=options.analysis.upper(), LABEL="2011+2012", EXTRA=extra[chn], MIN=min[chn,cat], MAX=max[chn,cat], LOG=log[chn,cat]))
        