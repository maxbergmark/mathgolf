import math
import datetime, time
import random

UNITTEST = False

def set_unittest():
	global UNITTEST
	UNITTEST = True

def push_16(arg):
	yield 16
def push_32(arg):
	yield 32
def push_64(arg):
	yield 64
def push_128(arg):
	yield 128
def push_256(arg):
	yield 256
def push_512(arg):
	yield 512
def push_1024(arg):
	yield 1024
def push_2048(arg):
	yield 2048
def push_4096(arg):
	yield 4096
def push_10(arg):
	yield 10
def push_100(arg):
	yield 100
def push_1000(arg):
	yield 1000
def push_10000(arg):
	yield 10000
def push_100000(arg):
	yield 100000
def push_1000000(arg):
	yield 1000000
def push_10000000(arg):
	yield 10000000
def push_100000000(arg):
	yield 100000000
def push_0(arg):
	yield 0
def push_1(arg):
	yield 1
def push_2(arg):
	yield 2
def push_3(arg):
	yield 3
def push_4(arg):
	yield 4
def push_5(arg):
	yield 5
def push_6(arg):
	yield 6
def push_7(arg):
	yield 7
def push_8(arg):
	yield 8
def push_9(arg):
	yield 9
def push_neg1(arg):
	yield -1
def push_neg2(arg):
	yield -2
def push_neg3(arg):
	yield -3
def push_e(arg):
	yield math.e
def push_unixtime(arg):
	if UNITTEST:
		yield 1500000000000
	else:
		now = datetime.datetime.now()
		yield int(time.mktime(now.timetuple())*1e3 + now.microsecond//1e3)
def push_random_int(arg):
	yield random.randint(-2**31, 2**31-1)
def push_asterisk_yield(arg):
	yield "*"
def push_1_array(arg):
	yield [1]
def push_0_array(arg):
	yield [0]
def push_60(arg):
	yield 60
def push_3600(arg):
	yield 3600
def push_86400(arg):
	yield 86400
def push_pi(arg):
	yield math.pi
def push_tau(arg):
	yield 2*math.pi
def push_space(arg):
	yield " "
def push_11(arg):
	yield 11
def push_12(arg):
	yield 12
def push_13(arg):
	yield 13
def push_14(arg):
	yield 14
def push_15(arg):
	yield 15
def push_17(arg):
	yield 17
def push_18(arg):
	yield 18
def push_19(arg):
	yield 19
def push_20(arg):
	yield 20
def push_21(arg):
	yield 21
def push_22(arg):
	yield 22
def push_23(arg):
	yield 23
def push_24(arg):
	yield 24
def push_25(arg):
	yield 25
def push_26(arg):
	yield 26
def push_27(arg):
	yield 27
def push_28(arg):
	yield 28
def push_29(arg):
	yield 29
def push_30(arg):
	yield 30
def push_31(arg):
	yield 31
def push_33(arg):
	yield 33
def push_34(arg):
	yield 34
def push_35(arg):
	yield 35
def push_36(arg):
	yield 36
def push_37(arg):
	yield 37
def push_38(arg):
	yield 38
def golden_ratio_yield(arg):
	yield (1+math.sqrt(5))/2
