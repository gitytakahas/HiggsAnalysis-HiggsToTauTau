#
# Execute from HiggsAnalysis/HiggsToTauTau/test
# 
# PyROOT Style macro for S/B plot
# Last update : 26 Sep 2013
#
# Instructions
#
# - Run the following commands to generate root files containing the postfit histograms:
#   -- python produce_macros.py  -a sm -c 'tt' -u 1 -p "8TeV"
#   -- python run_macros.py  -a sm -c 'mt, et, em'  -p "7TeV 8TeV"
#
# - Run this macro by python sobWeightedCombineAll.py
#   --it relies on another macro sobWeightedCombine.py being at the same PATH
#


sep_line = '-'*70
fmt = '%-20s %-4s %-10s'

from ROOT import gROOT
from HttStyles import *
#from sobWeightedCombine.py import *
from optparse import OptionParser, OptionGroup
import ConfigParser


parser = OptionParser(usage='usage: %prog [options] ARGs',
                      description='S/B plot macro')
parser.add_option('-c', '--channel', dest='channel', default='mt et tt em ee mm mt_soft vhtt', action='store',
                  help='channels to be considered for the plot. Default : mt et tt em ee mm mt_soft vhtt')

parser.add_option('-p', '--period', dest='period', default='7TeV 8TeV', action='store',
                  help='period used for the S/B plots. Default : 7TeV 8TeV')

parser.add_option('-g', '--category', dest='category', default='0jet 1jet vbf', action='store',
                  help='categories used for the S/B plots. Default : 0jet 1jet vbf')


(options, args) = parser.parse_args()

init = ConfigParser.SafeConfigParser()
init.read('./config.ini')


def sobCombine(Plotname, # TauTau_MSSM
               ListOfHistogram, # TauTau_MSSM
               Datasetname, # CMS Preliminary,  H#rightarrow#tau#tau,  4.9 fb^{-1} at 7 TeV, 19.8 fb^{-1} at 8 TeV"
               Channelname, # #tau_{h}#tau_{h}
               Categoryname, # 
               Weight,
               muValue,
               Log=False,
               Mass=125,
               Tanb=0):

    # ListOfHistogram : array of input postfit root files 
    # Plotname : name for this plot
    # Wieghts : option to apply or not apply weights

    print 'S/B combine:'
    print sep_line
    print fmt % ('Plotname', ':', Plotname)
    print fmt % ('Datasetname', ':', Datasetname)
    print fmt % ('Channelname', ':', Channelname)
    print fmt % ('Categoryname', ':', Categoryname)
    print fmt % ('Weight', ':', Weight)
    print fmt % ('mu-Value', ':', muValue)
    print fmt % ('Log-scale', ':', Log)
    print fmt % ('Mass', ':', Mass)
    print fmt % ('tan-beta', ':', Tanb)
    print fmt % ('# of files', ':', len(ListOfHistogram))
    print

    
#    sobWeightedCombine(ListOfHistogram, Plotname, Weight, muValue);  
#    sobWeightedPlot(Plotname, Datasetname, Channelname, Categoryname, Log, Mass, Tanb)
    

dict = {}
list_all = []


for ichn in options.channel.split():

    list = []
    
    for icat in options.category.split():
        for iperiod in options.period.split():
            list.extend(init.get(ichn, icat+'_'+iperiod).split())

    dict[ichn] = list
    list_all.extend(list)

#    print fmt % (ichn, ':', str(len(dict[ichn])) + ' files are found')


    
#print sep_line
print
print fmt % ('Total # of files', ':', len(list_all))
#print sep_line


# Individual channel
for ichn in options.channel.split():
    pname = ichn + '_SM'
    sobCombine(pname, dict[ichn], init.get('naming', 'caption'), init.get('naming',ichn), '', 1, init.get('muvalue',ichn))


# Combine
sobCombine('All_SM', list_all, init.get('naming', 'caption'), init.get('naming','all'), '', 1, init.get('muvalue','all'))


gROOT.ProcessLine(".q");
