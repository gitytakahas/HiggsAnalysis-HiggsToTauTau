thepeg             := thepeg
ALL_TOOLS      += thepeg
thepeg_LOC_INCLUDE := /afs/cern.ch/cms/slc5_amd64_gcc472/external/thepeg/1.7.0/include
thepeg_EX_INCLUDE  := $(thepeg_LOC_INCLUDE)
thepeg_LOC_LIB := ThePEG LesHouches
thepeg_EX_LIB  := $(thepeg_LOC_LIB)
thepeg_LOC_USE := lhapdf gsl
thepeg_EX_USE  := $(thepeg_LOC_USE)
thepeg_INIT_FUNC := $$(eval $$(call ProductCommonVars,thepeg,,,thepeg))

