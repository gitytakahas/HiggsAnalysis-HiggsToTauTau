jemalloc             := jemalloc
ALL_TOOLS      += jemalloc
jemalloc_LOC_INCLUDE := /afs/cern.ch/cms/slc5_amd64_gcc472/external/jemalloc/2.2.2/include
jemalloc_EX_INCLUDE  := $(jemalloc_LOC_INCLUDE)
jemalloc_LOC_LIB := jemalloc
jemalloc_EX_LIB  := $(jemalloc_LOC_LIB)
jemalloc_INIT_FUNC := $$(eval $$(call ProductCommonVars,jemalloc,,,jemalloc))

