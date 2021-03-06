boost             := boost
ALL_TOOLS      += boost
boost_LOC_INCLUDE := /afs/cern.ch/cms/slc5_amd64_gcc472/external/boost/1.51.0-cms2/include
boost_EX_INCLUDE  := $(boost_LOC_INCLUDE)
boost_LOC_LIB := boost_thread boost_signals boost_date_time
boost_EX_LIB  := $(boost_LOC_LIB)
boost_LOC_USE := sockets
boost_EX_USE  := $(boost_LOC_USE)
boost_INIT_FUNC := $$(eval $$(call ProductCommonVars,boost,,,boost))

