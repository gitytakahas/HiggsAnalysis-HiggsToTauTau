hepmc_headers             := hepmc_headers
ALL_TOOLS      += hepmc_headers
hepmc_headers_LOC_INCLUDE := /afs/cern.ch/cms/slc5_amd64_gcc472/external/hepmc/2.06.07/include
hepmc_headers_EX_INCLUDE  := $(hepmc_headers_LOC_INCLUDE)
hepmc_headers_INIT_FUNC := $$(eval $$(call ProductCommonVars,hepmc_headers,,,hepmc_headers))

