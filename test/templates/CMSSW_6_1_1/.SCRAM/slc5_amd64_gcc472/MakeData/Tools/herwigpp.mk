herwigpp             := herwigpp
ALL_TOOLS      += herwigpp
herwigpp_LOC_INCLUDE := /afs/cern.ch/cms/slc5_amd64_gcc472/external/herwigpp/2.5.0/include
herwigpp_EX_INCLUDE  := $(herwigpp_LOC_INCLUDE)
herwigpp_INIT_FUNC := $$(eval $$(call ProductCommonVars,herwigpp,,,herwigpp))

