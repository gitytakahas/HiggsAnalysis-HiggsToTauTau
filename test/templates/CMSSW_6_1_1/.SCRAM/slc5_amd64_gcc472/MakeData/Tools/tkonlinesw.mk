tkonlinesw             := tkonlinesw
ALL_TOOLS      += tkonlinesw
tkonlinesw_LOC_INCLUDE := /afs/cern.ch/cms/slc5_amd64_gcc472/external/tkonlinesw/2.7.0-cms4/include
tkonlinesw_EX_INCLUDE  := $(tkonlinesw_LOC_INCLUDE)
tkonlinesw_LOC_LIB := ICUtils Fed9UUtils
tkonlinesw_EX_LIB  := $(tkonlinesw_LOC_LIB)
tkonlinesw_LOC_USE := xerces-c
tkonlinesw_EX_USE  := $(tkonlinesw_LOC_USE)
tkonlinesw_INIT_FUNC := $$(eval $$(call ProductCommonVars,tkonlinesw,,,tkonlinesw))

