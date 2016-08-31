#!/bin/bash
#
# Wed Aug 31 21:27:46 CST 2016

PWD=`pwd`

echo $PWD
echo ${PWD#/*/}
echo ${PWD##/*/}
echo ${PWD%/*}
# Attention: It is null below
echo ${PWD%%/*}

