ktjet             := ktjet
ALL_TOOLS      += ktjet
ktjet_LOC_INCLUDE := /afs/cern.ch/cms/slc5_amd64_gcc472/external/ktjet/1.06-cms2/include
ktjet_EX_INCLUDE  := $(ktjet_LOC_INCLUDE)
ktjet_LOC_LIB := KtEvent
ktjet_EX_LIB  := $(ktjet_LOC_LIB)
ktjet_LOC_FLAGS_CPPDEFINES  := -DKTDOUBLEPRECISION
ktjet_EX_FLAGS_CPPDEFINES   := $(ktjet_LOC_FLAGS_CPPDEFINES)
ktjet_INIT_FUNC := $$(eval $$(call ProductCommonVars,ktjet,,,ktjet))

