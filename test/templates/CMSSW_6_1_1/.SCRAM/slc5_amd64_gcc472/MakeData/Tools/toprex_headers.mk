toprex_headers             := toprex_headers
ALL_TOOLS      += toprex_headers
toprex_headers_LOC_INCLUDE := /afs/cern.ch/cms/slc5_amd64_gcc472/external/toprex/4.23/include
toprex_headers_EX_INCLUDE  := $(toprex_headers_LOC_INCLUDE)
toprex_headers_INIT_FUNC := $$(eval $$(call ProductCommonVars,toprex_headers,,,toprex_headers))

