#!/bin/bash
#第一个参数为源数据
#第二个参数为目标文件
for i in `seq 1 9999`
do
	cpu0Temp=`cat $1|awk '{print $1}'|sed -n $i'p'`
	cpu1Temp=`cat $1|awk '{print $2}'|sed -n $i'p'`
	cpu0MarginTemp=`cat $1|awk '{print $3}'|sed -n $i'p'`
	cpu1MarginTemp=`cat $1|awk '{print $4}'|sed -n $i'p'`


	cpu0TempSed=`cat $2|grep 'CPU0_Temp'`
	cpu1TempSed=`cat $2|grep 'CPU1_Temp'`
	cpu0MarginTempSed=`cat $2|grep 'CPU0_Margin_Temp'`
	cpu1MarginTempSed=`cat $2|grep 'CPU1_Margin_Temp'`


	a='CPU0_Temp|'$cpu0Temp'degreesC|ok'
	b='CPU1_Temp|'$cpu1Temp'degreesC|ok'
	c='CPU0_Margin_Temp|'$cpu0MarginTemp'degreesC|ok'
	d='CPU1_Margin_Temp|'$cpu1MarginTemp'degreesC|ok'
	
	echo $a
	echo $b
	echo $c
	echo $d

	sed -i 's/'$cpu0TempSed'/'$a'/g' $2
	sed -i 's/'$cpu1TempSed'/'$b'/g' $2
	sed -i 's/'$cpu0MarginTempSed'/'$c'/g' $2
	sed -i 's/'$cpu1MarginTempSed'/'$d'/g' $2

	

	sleep 1
done
