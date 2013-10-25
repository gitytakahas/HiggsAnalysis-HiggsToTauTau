#include "TGraph.h"

inline void
PlotLimits::HIG_12_052_lower(TGraph* graph)
{
  /* CMS-12-052 H+->tau search (2/fb-4.9/fb)
     https://twiki.cern.ch/twiki/bin/view/CMSPublic/Hig12052TWiki
  */
  graph->SetPoint(0, 59.6203547176 , 12.2664008162 );
  graph->SetPoint(1, 87.9983660013 , 15.5661876307 );
  graph->SetPoint(2, 111.996804021 , 20.8313975211 );
  graph->SetPoint(3, 119.310262834 , 33.2105532713 );
  graph->SetPoint(4, 120.714292339 , 42.9370932596 );
  //graph->SetPoint(5, 120.714292339 , 60.         );
}

inline void
PlotLimits::HIG_12_052_upper(TGraph* graph)
{
  /* CMS-12-052 H+->tau search (2/fb-4.9/fb)
     https://twiki.cern.ch/twiki/bin/view/CMSPublic/Hig12052TWiki
  */
  graph->SetPoint(0, 62.22745133   , 4.41667678486 );
  graph->SetPoint(1, 91.117399096  , 3.53032685681 );
  graph->SetPoint(2, 116.527300643 , 2.57576019994 );
  //graph->SetPoint(3, 116.527300643 , 0.          );
}


/*
GraphToTanBeta high tanb region mHp ObservedTheoryMinus
mH+,tanb,mA 100.0 9.76951241917 60.5912657523
mH+,tanb,mA 120.0 13.1064174193 88.8141166509
mH+,tanb,mA 140.0 17.8283430702 113.001183052
mH+,tanb,mA 150.0 28.519168461 121.38221419
mH+,tanb,mA 155.0 36.7885584941 123.852994657
mH+,tanb,mA 160.0 48.2620354369 124.189775835
GraphToTanBeta low tanb region mHp ObservedTheoryMinus
mH+,tanb,mA 100.0 5.55286291603 61.8840239818
mH+,tanb,mA 120.0 4.18945329917 90.9285309324
mH+,tanb,mA 140.0 3.05768363558 116.302536971
GraphToTanBeta high tanb region mHp Expected2Sigma
mH+,tanb,mA 100.0 1.0 69.24216133
mH+,tanb,mA 120.0 1.0 96.08110043
mH+,tanb,mA 140.0 12.0094355097 114.568805911
mH+,tanb,mA 150.0 18.4766992563 124.947481043
mH+,tanb,mA 155.0 24.22805314 129.084579861
mH+,tanb,mA 160.0 35.9029784393 130.438095027
mH+,tanb,mA 160.0 64.921275585 113.856613251
mH+,tanb,mA 155.0 47.691506499 118.049106848
mH+,tanb,mA 150.0 36.5541613903 117.686244022
mH+,tanb,mA 140.0 24.940098598 110.416652101
mH+,tanb,mA 120.0 18.2847574491 86.9612892565
mH+,tanb,mA 100.0 14.2771440633 58.7058083074
GraphToTanBeta low tanb region mHp Expected2Sigma
mH+,tanb,mA 100.0 1.0 69.24216133
mH+,tanb,mA 120.0 1.0 96.08110043
mH+,tanb,mA 140.0 4.57201433924 115.920469231
mH+,tanb,mA 150.0 2.88260990545 128.21718574
mH+,tanb,mA 140.0 2.04897176426 116.945012724
mH+,tanb,mA 120.0 3.00161520054 91.3250557009
mH+,tanb,mA 100.0 3.79172693493 62.4557194286
GraphToTanBeta high tanb region mHp Expected1Sigma
mH+,tanb,mA 100.0 1.0 69.24216133
mH+,tanb,mA 120.0 10.0685318094 89.6574588613
mH+,tanb,mA 140.0 13.7541555608 114.15123739
mH+,tanb,mA 150.0 20.7229896078 124.25913066
mH+,tanb,mA 155.0 25.3628979376 128.681885976
mH+,tanb,mA 160.0 35.8241366544 130.473349462
mH+,tanb,mA 160.0 51.6375498284 122.263065248
mH+,tanb,mA 155.0 38.125828324 123.201009737
mH+,tanb,mA 150.0 29.4362190199 120.996555312
mH+,tanb,mA 140.0 20.0851127689 112.25898231
mH+,tanb,mA 120.0 15.2072862661 88.1253567997
mH+,tanb,mA 100.0 11.6514142309 59.8752194956
GraphToTanBeta low tanb region mHp Expected1Sigma
mH+,tanb,mA 100.0 1.0 69.24216133
mH+,tanb,mA 120.0 5.43893019759 90.6537286913
mH+,tanb,mA 140.0 3.9892484869 116.037733228
mH+,tanb,mA 150.0 2.49591508393 128.407111118
mH+,tanb,mA 140.0 2.68505398063 116.467091277
mH+,tanb,mA 120.0 3.61369975468 91.0902087877
mH+,tanb,mA 100.0 4.64890245175 62.15242748
GraphToTanBeta high tanb region mHp Expected
mH+,tanb,mA 100.0 1.0 69.24216133
mH+,tanb,mA 120.0 12.4396440256 89.0129444762
mH+,tanb,mA 140.0 16.3173228202 113.456187276
mH+,tanb,mA 150.0 23.8313595968 123.200982674
mH+,tanb,mA 155.0 30.5352934642 126.666032588
mH+,tanb,mA 160.0 42.1096192891 127.464755577
GraphToTanBeta low tanb region mHp Expected
mH+,tanb,mA 100.0 1.0 69.24216133
mH+,tanb,mA 120.0 4.4085183414 90.8752221123
mH+,tanb,mA 140.0 3.35390663015 116.202036661
mH+,tanb,mA 150.0 1.97876094571 128.831875005
GraphToTanBeta high tanb region mHp Observed
mH+,tanb,mA 100.0 12.2664008162 59.6203547176
mH+,tanb,mA 120.0 15.5661876307 87.9983660013
mH+,tanb,mA 140.0 20.8313975211 111.996804021
mH+,tanb,mA 150.0 33.2105532713 119.310262834
mH+,tanb,mA 155.0 42.9370932596 120.714292339
mH+,tanb,mA 160.0 56.5618919992 119.295860843
GraphToTanBeta low tanb region mHp Observed
mH+,tanb,mA 100.0 4.41667678486 62.22745133
mH+,tanb,mA 120.0 3.53032685681 91.117399096
mH+,tanb,mA 140.0 2.57576019994 116.527300643
GraphToTanBeta high tanb region mHp ObservedTheoryPlus
mH+,tanb,mA 100.0 14.0945906329 58.7957085679
mH+,tanb,mA 120.0 17.598741262 87.2362829855
mH+,tanb,mA 140.0 23.4009317747 111.034911028
mH+,tanb,mA 150.0 37.3260083603 117.294863175
mH+,tanb,mA 155.0 48.3807250995 117.646296541
mH+,tanb,mA 160.0 63.9856366157 114.489969773
GraphToTanBeta low tanb region mHp ObservedTheoryPlus
mH+,tanb,mA 100.0 3.84314580294 62.4350734769
mH+,tanb,mA 120.0 3.12083784142 91.2717024884
mH+,tanb,mA 140.0 2.23510781937 116.766307126
*/
