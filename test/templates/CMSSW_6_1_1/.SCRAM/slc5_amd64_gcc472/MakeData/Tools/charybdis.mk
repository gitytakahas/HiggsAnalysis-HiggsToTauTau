charybdis             := charybdis
ALL_TOOLS      += charybdis
charybdis_LOC_INCLUDE := /afs/cern.ch/cms/slc5_amd64_gcc472/external/charybdis/1.003/include
charybdis_EX_INCLUDE  := $(charybdis_LOC_INCLUDE)
charybdis_LOC_LIB := charybdis
charybdis_EX_LIB  := $(charybdis_LOC_LIB)
charybdis_LOC_USE := f77compiler herwig pythia6
charybdis_EX_USE  := $(charybdis_LOC_USE)
charybdis_INIT_FUNC := $$(eval $$(call ProductCommonVars,charybdis,,,charybdis))

