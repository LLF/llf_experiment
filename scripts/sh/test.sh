#!/bin/bash
if [ $# -lt 3 ];then
cat << HELP
as;dfa;ljdf
HELP
    exit 0
fi

a="hello world" #shell 默认赋值为字符串
echo "aaa is!" $a  #$+变量为变量的值
num=2
echo "this is num ${num}nd"
echo `ls -l`
if [ "$a" = "hello world" ] 
then
    echo "ffafaf"
else
    echo "aadad"
fi


name=("Ton" "Mary" "Tim")
for i in 0,1,2
do
    echo ${name[$i]}
done

echo `dirname $0`
echo $1 $#

echo ${name[1]}

MY="abcdefg"
echo ${MY%%de*}
echo ${MY##*de}
