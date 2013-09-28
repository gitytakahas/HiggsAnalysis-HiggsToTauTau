valgrind             := valgrind
ALL_TOOLS      += valgrind
valgrind_LOC_INCLUDE := /afs/cern.ch/cms/slc5_amd64_gcc472/external/valgrind/3.8.0/include
valgrind_EX_INCLUDE  := $(valgrind_LOC_INCLUDE)
valgrind_INIT_FUNC := $$(eval $$(call ProductCommonVars,valgrind,,,valgrind))

