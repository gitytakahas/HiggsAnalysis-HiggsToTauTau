curl             := curl
ALL_TOOLS      += curl
curl_LOC_INCLUDE := /afs/cern.ch/cms/slc5_amd64_gcc472/external/curl/7.28.0/include
curl_EX_INCLUDE  := $(curl_LOC_INCLUDE)
curl_LOC_LIB := curl
curl_EX_LIB  := $(curl_LOC_LIB)
curl_INIT_FUNC := $$(eval $$(call ProductCommonVars,curl,,,curl))

