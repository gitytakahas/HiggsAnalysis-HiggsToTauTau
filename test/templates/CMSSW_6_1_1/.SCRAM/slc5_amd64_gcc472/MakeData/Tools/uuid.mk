uuid             := uuid
ALL_TOOLS      += uuid
uuid_LOC_INCLUDE := /afs/cern.ch/cms/slc5_amd64_gcc472/external/uuid/1.38-cms/include
uuid_EX_INCLUDE  := $(uuid_LOC_INCLUDE)
uuid_LOC_LIB := uuid
uuid_EX_LIB  := $(uuid_LOC_LIB)
uuid_LOC_USE := sockets
uuid_EX_USE  := $(uuid_LOC_USE)
uuid_INIT_FUNC := $$(eval $$(call ProductCommonVars,uuid,,,uuid))

