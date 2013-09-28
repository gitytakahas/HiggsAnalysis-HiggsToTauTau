sqlite             := sqlite
ALL_TOOLS      += sqlite
sqlite_LOC_INCLUDE := /afs/cern.ch/cms/slc5_amd64_gcc472/external/sqlite/3.7.10/include
sqlite_EX_INCLUDE  := $(sqlite_LOC_INCLUDE)
sqlite_LOC_LIB := sqlite3
sqlite_EX_LIB  := $(sqlite_LOC_LIB)
sqlite_INIT_FUNC := $$(eval $$(call ProductCommonVars,sqlite,,,sqlite))

