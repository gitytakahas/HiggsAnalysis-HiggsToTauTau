xrootd             := xrootd
ALL_TOOLS      += xrootd
xrootd_LOC_INCLUDE := /afs/cern.ch/cms/slc5_amd64_gcc472/external/xrootd/3.2.4-cms2/include/xrootd
xrootd_EX_INCLUDE  := $(xrootd_LOC_INCLUDE)
xrootd_LOC_LIB := XrdUtils XrdClient
xrootd_EX_LIB  := $(xrootd_LOC_LIB)
xrootd_INIT_FUNC := $$(eval $$(call ProductCommonVars,xrootd,,,xrootd))

