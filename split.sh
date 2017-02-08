INPUT=$1
THREAD_NUM=$2
NUMS=`cat $INPUT | wc -l`
echo "Total nums: $NUMS"
AVERAGE=`expr $NUMS / $THREAD_NUM + 1`
echo "Avarage nums: $AVERAGE"

for i in `seq $THREAD_NUM`; do
    SPLIT=`expr $AVERAGE \* $i`
    echo $SPLIT
    cat $INPUT | head -n $SPLIT | tail -n $AVERAGE > $INPUT_$i
done

cat ${INPUT}_${THREAD_NUM} | tail -n `expr $NUMS - $AVERAGE \* \( $THREAD_NUM - 1 \)` > temptemp
mv temptemp ${INPUT}_${THREAD_NUM}
