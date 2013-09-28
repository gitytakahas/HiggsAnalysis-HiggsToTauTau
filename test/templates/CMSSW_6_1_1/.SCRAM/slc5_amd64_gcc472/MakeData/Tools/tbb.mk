tbb             := tbb
ALL_TOOLS      += tbb
tbb_LOC_INCLUDE := /afs/cern.ch/cms/slc5_amd64_gcc472/external/tbb/41_20120718oss/include
tbb_EX_INCLUDE  := $(tbb_LOC_INCLUDE)
tbb_LOC_LIB := tbb
tbb_EX_LIB  := $(tbb_LOC_LIB)
tbb_INIT_FUNC := $$(eval $$(call ProductCommonVars,tbb,,,tbb))

