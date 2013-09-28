from ROOT import TROOT, TFile, TString, TPad, TPaveText, TCanvas, TH1F, TLegend, TF1, gROOT, TLine, gStyle
from ROOT import kBlack
import math

from HttStyles import *

gStyle = HttStyle

SIGNAL_SCALE = 1.

def tfileGet(tfile, histName):
    hist = tfile.Get(histName)
    if not hist:
        print 'Object', histName, 'not found in', tfile
    return hist

'''Returns first bin with bin content of at least frac times the maximum'''
def findFirstBin(h, frac=0.1):
    maxVal = h.GetMaximum()
    bin = 0
    for iBin in range(1, h.GetNBinsX()+1):
        if h.GetBinContent(iBin) > frac * maxVal:
            bin = iBin
    return bin

'''Returns first bin with bin content of at least frac times the maximum'''
def findLastBin(h, frac=0.1):
    maxVal = h.GetMaximum()
    bin = 0
    for iBin in reversed(range(1, h.GetNBinsX()+1)):
        if h.GetBinContent(iBin) > frac * maxVal:
            bin = iBin
    return bin

''' Returns clone of the passed histogram with bin contents zeroed out'''
def getErrorBand(hist):
    h = hist.Clone(hist.GetName() + 'herrorBand')
    # Zero out bin content, including under+overflow
    for iBin in range(0, h.GetNbinsX()+2):
        h.SetBinContent(iBin, 0.)
    # Zero out under/overflow bin errors
    h.SetBinError(0, 0.)
    h.SetBinError(h.GetNbinsX()+1, 0.)
    return h

''' Finds central 68% region in signal histogram and calculates purity for that'''
def getSoB(hsplusb, hbkg):
    hs = hsplusb.Clone('HS')
    hb = hbkg.Clone('HB')
    hs.Add(hb, -1.)
    hs.Scale(SIGNAL_SCALE)

    sigString = ''
    bkgString = ''
    errString = ''

    xmin = hs.GetXaxis().GetXmin()
    xmax = hs.GetXaxis().GetXmax()


    # FIXME: This seems overly complicated
    for iBin in range(1, hs.GetNbinsX()+1):

        template = '{binContent:.6f}*({binXmin}<x&&x<{binXmax})'
        sigString += template.format(binContent=hs.GetBinContent(iBin), binXmin=hs.GetBinLowEdge(iBin), binXmax=hs.GetBinLowEdge(iBin)+hs.GetBinWidth(iBin))
        bkgString += template.format(binContent=hb.GetBinContent(iBin), binXmin=hb.GetBinLowEdge(iBin), binXmax=hb.GetBinLowEdge(iBin)+hb.GetBinWidth(iBin))
        errString += template.format(binContent=hb.GetBinError(iBin), binXmin=hb.GetBinLowEdge(iBin), binXmax=hb.GetBinLowEdge(iBin)+hb.GetBinWidth(iBin))


        if iBin < hs.GetNbinsX():
            sigString += '+'
            bkgString += '+'
            errString += '+'

    fSig = TF1('fsig', sigString, xmin, xmax)
    fBkg = TF1('fbkg', bkgString, xmin, xmax)
    fErr = TF1('fErr', errString, xmin, xmax)

    npoints = 10000.
    total = fSig.Integral(xmin, xmax)
    dx = (xmax - xmin)/npoints
    xlow = xmin
    xhigh = xmax
    lowInt = 0.
    highInt = 0.
    # So this finds the x value borders in which 68% of the
    # are contained. These may lie anywhere within a bin
    for i in range(1, int(npoints)+1):
        xl = xmin + float(i) * dx
        lowInt += fSig.Eval(xl) * dx
        if lowInt < total * 0.158:
            xlow = xl
        xh = xmax - float(i)*dx
        highInt += fSig.Eval(xh) * dx
        if highInt < total * 0.158:
            xhigh = xh

    sig = fSig.Integral(xlow, xhigh)
    bkg = fBkg.Integral(xlow, xhigh)

    return sig/bkg

    # Can introdduce other measures here:
    # sig/sqrt(sig+bkg)
    # sig/sqrt(bkgerr*bkgerr + sig + bkg)


# This scans through all files, gets the width of 
# the first bin for each 'ggH' histogram, and
# sets the rebin flag to true for the hists
# that have a smaller width
def findRebin(fileNames, rebinList):
    binW = 0.
    for fileName in fileNames:
        f = TFile(fileName+'.root')
        ggH = tfileGet(f, 'ggH')
        if ggH.GetBinWidth(1) > binW:
            binW = ggH.GetBinWidth(1)

    print 'Maximum bin 1 bin width', binW

    for i, fileName in enumerate(fileNames):
        f = TFile(fileName+'.root')
        ggH = tfileGet(f, 'ggH')
        if ggH.GetBinWidth(1) != binW:
            rebinList[i] = 1


def sobWeightedCombine(fileNames, outName, doWeight=1, muValue=1.):
    print 'WARNING: using fitted mu value', muValue, 'make sure it\'s up to date'
    isSM = outName.find('SM') != -1
    # FIXME: Dict is probably better
    rebinList = [0 for i in range(0, len(fileNames))]
    findRebin(fileNames, rebinList)

    weights = []
    weightSum = 0.
    for iFile, fileName in enumerate(fileNames):
        f = TFile(fileName+'.root')
        gROOT.cd()

        ggH = tfileGet(f, 'ggH').Clone('ggH')
        if fileName.find('emu') != -1 and isSM:
            Ztt = tfileGet(f, 'ggH_hww').Clone('Ztt') # FIXME: WOW, that looks error-prone
        else:
            Ztt = tfileGet(f, 'Ztt').Clone('Ztt')

        weights.append(getSoB(ggH, Ztt))
        weightSum += weights[iFile]

    if weightSum <= 0.:
        print 'ERROR: sum of S/B weights is bad, returning'
        return

    weights = [w/weightSum for w in weights]

    print 'Weights'

    maxW = 0.
    for i, weight in enumerate(weights):
        if weight > maxW:
            maxW = weight
        print 'Weight', weight, fileNames[i]
    print 'Maximum weight', maxW


    signalIntegral = 0.
    weightedSignalIntegral = 0.

    for i, fileName in enumerate(fileNames):
        tfile = TFile(fileName+'.root')
        gROOT.cd()
        ggH = tfile.Get('ggH')
        if fileName.find('emu') != -1 and isSM:
            Ztt = tfile.Get('ggH_hww').Clone('Ztt')
        else:
            Ztt = tfile.Get('Ztt').Clone('Ztt')

        signal = ggH.Clone('signal')
        signal.Scale(SIGNAL_SCALE * muValue)



        for b in range(1, signal.GetNbinsX()+1):
            signal.SetBinContent(b, signal.GetBinContent(b) * signal.GetBinWidth(b))

        signalIntegral += signal.Integral()

        if doWeight == 1:
            signal.Scale(weights[i])

        weightedSignalIntegral += signal.Integral()

    print 'Signal yield:', signalIntegral
    print 'Weighted signal yield:', weightedSignalIntegral
    print 'Signal yield scale factor', signalIntegral/weightedSignalIntegral

    for i, weight in enumerate(weights):
        weights[i] *= signalIntegral/weightedSignalIntegral

    file1 = TFile(fileNames[0]+'.root')
    gROOT.cd()

    samples = ['ggH', 'Ztt', 'signal', 'data_obs', 'ttbar', 'EWK', 'Fakes']

    if fileNames[0].find('emu') != -1 and isSM:
        samples.append('ggH_hww')

    histDict = {}
    # Use first file clones as base histograms

    for sample in samples:
        if fileNames[0].find('emu') != -1 and isSM and sample == 'Ztt':
            histDict[sample] = tfileGet(file1, 'ggH_hww').Clone(sample)
        elif sample == 'signal':
            histDict[sample] = tfileGet(file1, 'ggH').Clone(sample)
        else:
            print 'Getting', sample, 'from', file1
            histDict[sample] = tfileGet(file1, sample).Clone(sample)
        if doWeight == 1:
            histDict[sample].Scale(weights[0])
        if rebinList[0]:
            histDict[sample].Rebin(2)
        if sample == 'signal':
            histDict[sample].Add(histDict['Ztt'], -1.)
            histDict[sample].Scale(SIGNAL_SCALE)

    file1.Close()

    for i, fileName in enumerate(fileNames):
        if fileName == fileNames[0]: continue
        print fileName
        file2 = TFile(fileName+'.root')
        print file2
        gROOT.cd()

        localHistDict = {}
        
        for sample in samples:
            if fileName.find('emu') == -1 and sample == 'ggH_hww':
                continue
            if fileName.find('emu') != -1 and isSM and sample == 'Ztt':
                localHistDict[sample] = tfileGet(file2, 'ggH_hww').Clone(sample+str(i))
            elif sample == 'signal':
                localHistDict[sample] = tfileGet(file2, 'ggH').Clone(sample+str(i))
            else:
                localHistDict[sample] = tfileGet(file2, sample).Clone(sample+str(i))
            if doWeight == 1:
                localHistDict[sample].Scale(weights[i])
            if rebinList[i]:
                localHistDict[sample].Rebin(2)
            if sample == 'signal':
                localHistDict[sample].Add(localHistDict['Ztt'], -1.)
                localHistDict[sample].Scale(SIGNAL_SCALE)
            histDict[sample].Add(localHistDict[sample])
            if fileName.find('emu') == -1 and 'ggH_hww' in histDict and sample == 'Ztt':
                histDict['ggH_hww'].Add(localHistDict[sample])

        file2.Close()

    fullOutName = 'Plot_' + outName + '.root'
    outFile = TFile(fullOutName, 'RECREATE')
    for hist in histDict.values():
        hist.Write()

    outFile.ls()
    outFile.Close()


def CMSPrelim(dataset, channel, cat):
    lowX = 0.16
    lowY = 0.835
    color = 1
    font = 62

    cmsprel = TPaveText(lowX, lowY+0.06, lowX+0.30, lowY+0.16, "NDC")
    cmsprel.SetBorderSize(   0 )
    cmsprel.SetFillStyle(    0 )
    cmsprel.SetTextAlign(   12 )
    cmsprel.SetTextColor( color )
    cmsprel.SetTextFont ( font )
    #cmsprel.SetTextSize ( 0.035 )
    #cmsprel.SetTextSize ( 0.027 )
    cmsprel.SetTextSize ( 0.030 )
    cmsprel.AddText(dataset)
    cmsprel.Draw()

    chan = TPaveText(lowX+0.05, lowY-0.002, lowX+0.45, lowY+0.028, "NDC")
    chan.SetBorderSize(   0 )
    chan.SetFillStyle(    0 )
    chan.SetTextAlign(   12 )
    chan.SetTextSize ( 0.035 )
    chan.SetTextColor( color )
    chan.SetTextFont ( font )
    chan.AddText(channel)
    chan.Draw()

    category = TPaveText(lowX+0.05, lowY-0.002-0.06, lowX+0.45, lowY+0.028-0.06, "NDC")
    category.SetBorderSize(   0 )
    category.SetFillStyle(    0 )
    category.SetTextAlign(   12 )
    category.SetTextSize ( 0.035 )
    category.SetTextColor( color )
    category.SetTextFont ( font )
    category.AddText(cat)
    category.Draw()


def diffPlot(h1, h2, opt):
    h = h1.Clone(h1.GetName() + h2.GetName() + '_diff')
    for b in range(1, h.GetNbinsX()+1):
        h.SetBinContent(b, h1.GetBinContent(b) - h2.GetBinContent(b))
        h.SetBinError(b, 0.)
        if opt == 1:
            h.SetBinError(b, h1.GetBinError(b))
        elif opt == 2:
            h.SetBinError(b, math.sqrt(h1.GetBinError(b)*h1.GetBinError(b) + h2.GetBinError(b)*h2.GetBinError(b)))

    h.SetBinContent(0, 0.)
    h.SetBinError(0, 0.)
    h.SetBinContent(h.GetNbinsX()+1, 0.)
    h.SetBinError(h.GetNbinsX()+1, 0.)

    return h

def findMaxY(h, opt=0, lowx=-1., highx=-1.):
    if lowx == -1.:
        lowx = h.GetXaxis().GetXmin()
    if highx == -1.:
        highx = h.GetXaxis().GetXmax()

    maxVal = 0.
    for b in range(1, h.GetNbinsX()+1):
        if h.GetBinContent(b) > 0. and lowx < h.GetBinCenter(b) and h.GetBinCenter(b) < highx:
            if opt == 0:
                if h.GetBinContent(b) + h.GetBinError(b) > maxVal:
                    maxVal = h.GetBinContent(b) + h.GetBinError(b)
            elif opt == 1:
                if h.GetBinContent(b) > maxVal:
                    maxVal = h.GetBinContent(b)
    return maxVal

def findMinY(h, opt=0, lowx=-1., highx=-1.):
    if lowx == -1.:
        lowx = h.GetXaxis().GetXmin()
    if highx == -1.:
        highx = h.GetXaxis().GetXmax()

    maxVal = 0.

    maxVal = 0.
    for b in range(1, h.GetNbinsX()+1):
        if h.GetBinContent(b) < 0. and lowx < h.GetBinCenter(b) and h.GetBinCenter(b) < highx:
            if opt == 0:
                if -h.GetBinContent(b) + h.GetBinError(b) > maxVal:
                    maxVal = h.GetBinContent(b) + h.GetBinError(b)
            elif opt == 1:
                if -h.GetBinContent(b) > maxVal:
                    maxVal = h.GetBinContent(b)
    return maxVal



def sobWeightedPlot(fileName, datasetName, channel, cat, log, mass, tanb):
    c = TCanvas(fileName, '', 600, 600)
    c.cd()
    if log: c.SetLogy(1)

    f = TFile('Plot_'+fileName+'.root')
    gROOT.cd()

    samples = ['ggH', 'Ztt', 'signal', 'data_obs', 'ttbar', 'EWK', 'Fakes', 'ggH_hww']

    if fileName.find('emu') != -1 and isSM:
        samples.append('ggH_hww')

    histDict = {}
    for sample in samples:
        histDict[sample] = tfileGet(f, sample)
        if not histDict[sample]:
            print 'Missing histogram', sample, 'in file', 'Plot_'+fileName+'.root'

    xminInset = 60 # 0
    xmaxInset = 180 # 340 (for full range)

    if tanb > 0:
        xminInset = mass - 100
        xmaxInset = mass + 100

    ztt = histDict['Ztt']
    ggH = histDict['ggH']
    data = histDict['data_obs']
    signal = histDict['signal']
    ggH_hww = histDict['ggH_hww']
    tt = histDict['ttbar']
    ewk = histDict['EWK']
    fakes = histDict['Fakes']

    ztt.GetYaxis().SetRangeUser(0., 1.3*findMaxY(data, 0))
    if log: 
        ztt.GetYaxis().SetRangeUser(0.001, 50.*findMaxY(data, 0))

    ztt.GetXaxis().SetTitle('#bf{m_{#tau#tau}  [GeV]}')
    ztt.GetYaxis().SetTitle('#bf{S/B Weighted dN/dm_{#tau#tau} [1/GeV]}')
    if tanb > 0. and not log:
        ztt.GetXaxis().SetRangeUser(0., mass+200.)

    ztt.SetTitleOffset(1.3, 'Y')
    ztt.SetTitleOffset(1., 'X')
    ztt.SetNdivisions(505)

    for b in range(0, signal.GetNbinsX()+2):
        if signal.GetBinCenter(b) < xminInset or xmaxInset < signal.GetBinCenter(b):
            signal.SetBinContent(b, 0.)
            signal.SetBinError(b, 0.)

    signal.SetName('sig')
    signal.SetFillStyle(3353) # 1001=solid , 3004,3005=diagonal
    signal.SetFillColor(2)
    signal.SetLineColor(2)
    signal.SetLineStyle(1)
    signal.SetLineWidth(0)

    ggH.SetBinContent(0,0) # remove red line on top of y axis in plot
    ggH.SetBinContent(ggH.GetNbinsX()+1,0)
    ggH.SetBinError(0,0)
    ggH.SetBinError(ggH.GetNbinsX()+1,0)
    ggH.SetName('ggH')
    ggH.SetFillStyle(3353) # 1001=solid , 3004,3005=diagonal
    ggH.SetFillColor(2)
    ggH.SetLineColor(2)
    ggH.SetLineStyle(1)
    ggH.SetLineWidth(0)

    if ggH_hww:
        errorBand = ggH_hww.Clone("errorBand")
    else:
        errorBand = ztt.Clone("errorBand")
    errorBand.SetMarkerSize(0)
    errorBand.SetFillColor(1)
    errorBand.SetFillStyle(3013)
    errorBand.SetLineWidth(1)

    legend = TLegend()
    mssmLabel = ''
    if tanb > 0:
        mssmLabel = "tan#beta={tanb}".format(tanb=tanb)
    higgsLabel = "H(125 GeV)#rightarrow#tau#tau"
    if tanb > 0:
        higgsLabel="H(125 GeV)#rightarrow#tau#tau"

    legend.SetFillStyle(0)
    legend.SetFillColor(0)
    legend.SetBorderSize(0)
    legend.AddEntry(ggH,higgsLabel,"F")
    if tanb>0: 
        legend.AddEntry(TObject(0), mssmLabel, "")
    legend.AddEntry(data,"observed", "LP")
    if ggH_hww:
        legend.AddEntry(ggH_hww, "H(125 GeV)#rightarrowWW", "F")
    legend.AddEntry(ztt, "Z#rightarrow#tau#tau","F")
    legend.AddEntry(tt, "t#bar{t}","F")
    legend.AddEntry(ewk, "electroweak","F")
    legend.AddEntry(fakes, "QCD","F")

    legend.SetX1NDC(0.63)
    legend.SetX2NDC(1.05)
    legend.SetY1NDC(0.27)
    legend.SetY2NDC(0.48)
    if log:
        legend.SetX1NDC(0.18)
        legend.SetX2NDC(0.60)
        legend.SetY1NDC(0.17)
        legend.SetY2NDC(0.38)
    
    legend.SetTextSize(.028)
    legend.SetTextAlign(12)

    if ggH_hww:
        dataDiff = diffPlot(data, ggH_hww, 1)
        errBand=getErrorBand(ggH_hww)
    else:
        dataDiff = diffPlot(data, ztt, 1)
        errBand=getErrorBand(ztt)

    errBand.SetFillStyle(3013) # 1001=solid , 3004,3005=diagonal, 3013=hatched official for H.tau tau
    errBand.SetFillColor(1)
    errBand.SetLineStyle(1)
    errBand.SetLineColor(1)
    errBand.SetLineWidth(1)

    errBandFrame = TH1F('errBandFrame', '', int((xmaxInset-xminInset)/dataDiff.GetBinWidth(1)),xminInset,xmaxInset)
    

    errBandFrame.GetYaxis().SetTitle("")
    errBandFrame.GetYaxis().SetRangeUser(-1.1*findMinY(dataDiff,0,xminInset,xmaxInset),2.0*findMaxY(dataDiff,0,xminInset,xmaxInset))
    errBandFrame.GetYaxis().SetNdivisions(5)
    errBandFrame.GetYaxis().SetLabelSize(0.06)
    errBandFrame.GetXaxis().SetTitle("#bf{m_{#tau#tau} [GeV]}    ")
    errBandFrame.GetXaxis().SetTitleColor(kBlack)
    errBandFrame.GetXaxis().SetTitleSize(0.07)
    errBandFrame.GetXaxis().SetTitleOffset(0.95)
    errBandFrame.GetXaxis().SetLabelSize(0.06)
    errBandFrame.SetNdivisions(505)

    legendDiff = TLegend()
    legendDiff.SetFillStyle(0)
    legendDiff.SetFillColor(0)
    legendDiff.SetBorderSize(0)
    legendDiff.AddEntry(signal,higgsLabel,"F")

    if tanb>0:
        legendDiff.AddEntry(TObject(0), mssmLabel, '') # That might not work in python
    legendDiff.AddEntry(dataDiff,"Data - Background","LP")  
    legendDiff.AddEntry(errBand,"Bkg. Uncertainty","F")
    legendDiff.SetX1NDC(0.45)
    legendDiff.SetX2NDC(0.88)
    legendDiff.SetY1NDC(0.67)
    legendDiff.SetY2NDC(0.88)
    if dataDiff.GetBinContent(dataDiff.FindBin(mass)) < 0.:
        legendDiff.SetX1NDC(0.45)
        legendDiff.SetX2NDC(0.88)
        legendDiff.SetY1NDC(0.24)
        legendDiff.SetY2NDC(0.45)

    legendDiff.SetTextSize(.045)
    legendDiff.SetTextAlign(12)

    padBack = TPad("padBack","padBack",0.57,0.58,0.975,0.956) # TPad must be created after TCanvas otherwise ROOT crashes
    padBack.SetFillColor(0)
    pad = TPad("diff","diff",0.45,0.5,0.9765,0.957) # TPad must be created after TCanvas otherwise ROOT crashes
    pad.cd()
    pad.SetFillColor(0)
    pad.SetFillStyle(0)
    errBandFrame.Draw()
    errBand.Draw("e2lsame")
    signal.Draw("histsame")
    line = TLine()
    line.DrawLine(xminInset, 0, xmaxInset, 0)
    dataDiff.Draw("pe same")
    legendDiff.Draw()
    pad.RedrawAxis()

    c.cd()
    ztt.Draw("hist")
    ggH.Draw("histsame")
    if ggH_hww:
        ggH_hww.Draw("hist same")
    ztt.Draw("hist same")
    errorBand.Draw("e2 same")
    tt.Draw("hist same")
    ewk.Draw("hist same")
    fakes.Draw("hist same")
    data.Draw("pe same")
    legend.Draw()
    c.RedrawAxis()
    padBack.Draw() # clear the background axe
    pad.Draw()

    CMSPrelim(datasetName, channel, cat)
    c.Print('Plot_'+fileName+".eps")
    c.Print('Plot_'+fileName+".png")
    c.Print('Plot_'+fileName+".pdf")
  
