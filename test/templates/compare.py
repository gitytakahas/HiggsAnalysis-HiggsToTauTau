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

import sys
from optparse import OptionParser, OptionGroup
import ConfigParser
from ROOT import TFile, TH1F, TCanvas, TH2F, TLegend, gStyle

fmt = '%.0f %.0f %.1f'
fmt_str = '%-60s'

parser = OptionParser(usage='usage: %prog [options] ARGs',
                      description='S/B plot macro')
parser.add_option('-c', '--channel', dest='channel', default='mt et tt em', action='store',
                  help='channels to be considered for the plot. Default : mt et tt em')

parser.add_option('-p', '--period', dest='period', default='8TeV', action='store',
                  help='period used for the S/B plots. Default : 8TeV')

parser.add_option('-g', '--category', dest='category', default='0jet 1jet vbf', action='store',
                  help='categories used for the S/B plots. Default : 1jet vbf')

(options, args) = parser.parse_args()


h=[0 for ii in range(100)]
hb=[0 for ii in range(100)]


init = ConfigParser.SafeConfigParser()
init.read('./compare.ini')

dict = {}
list_all = []


for ichn in options.channel.split():
    
    list = []
    
    for icat in options.category.split():
        for iperiod in options.period.split():
            list.extend(init.get(ichn, icat+'_'+iperiod).split())
            
    dict[ichn] = list
    list_all.extend(list)


print len(list_all), 'files'


canvas = TCanvas('c')

gStyle.SetOptStat(0)

leg = TLegend(0.5,0.6,0.7,0.8)

for ii in range(len(list_all)):
    file = TFile(list_all[ii]+'.root')
    h[ii] = file.Get('ggH')
    hb[ii] = file.Get('Ztt')
    file.cd()
    if h[ii]==0: print 'No hisotgram found for', list_all[ii]

    h[ii].SetLineColor(ii+1)

    for ibin in range(1, h[ii].GetXaxis().GetNbins() + 1):
        h[ii].SetBinError(ibin,0)
        
    if ii==0:
        h[ii].DrawNormalized('h')
    else:
        h[ii].DrawNormalized('hsame')            

    leg.AddEntry(h[ii], list_all[ii].replace('_LIN','').replace('postfit_',''),'lep')

    print fmt_str % (list_all[ii]), ':', fmt % (h[ii].GetRMS(), hb[ii].GetMean(), h[ii].GetSumOfWeights())
#    print fmt_str % (list_all[ii]), ':', fmt % (hb[ii].GetSumOfWeights(), h[ii].GetSumOfWeights(), h[ii].GetSumOfWeights()/hb[ii].GetSumOfWeights())


#canvas.cd()
#leg.Draw()
#canvas.SaveAs('dist.png')
