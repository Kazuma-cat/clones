PyDir=~kazuma/clones/py
cd $PyDir
ImplTypePM=incore
OnTheFly=True
ChargeType="Loewdin"
LocMet="PMNR"
Tj=1e-5
Tl=1e-5
Tr=1e-5

for file in *; do
    sed -i -e "s/hint.ImplTypePM =.*/hint.ImplTypePM = {ImplTypePM}/g" $file
    sed -i -e 's/hint.isOnTheFly =.*/hint.isOnTheFly = {OnTheFly}/g' $file
    sed -i -e 's/hint.ChargeType =.*/hint.ChargeType = {ChargeType}/g' $file
    sed -i -e 's/lct.LocMet =.*/lct.LocMet = {LocMet}/g' $file
