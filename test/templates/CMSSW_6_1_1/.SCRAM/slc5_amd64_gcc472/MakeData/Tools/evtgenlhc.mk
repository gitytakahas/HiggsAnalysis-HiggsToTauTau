evtgenlhc             := evtgenlhc
ALL_TOOLS      += evtgenlhc
evtgenlhc_LOC_INCLUDE := /afs/cern.ch/cms/slc5_amd64_gcc472/external/evtgenlhc/9.1-cms2
evtgenlhc_EX_INCLUDE  := $(evtgenlhc_LOC_INCLUDE)
evtgenlhc_LOC_LIB := evtgenlhc
evtgenlhc_EX_LIB  := $(evtgenlhc_LOC_LIB)
evtgenlhc_LOC_USE := clhep
evtgenlhc_EX_USE  := $(evtgenlhc_LOC_USE)
evtgenlhc_INIT_FUNC := $$(eval $$(call ProductCommonVars,evtgenlhc,,,evtgenlhc))

