; ModuleID = "clong prog"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

define i32 @"main"()
{
main.entry:
  %"input_str" = alloca [1000 x i8]
  %".2" = alloca i32
  store i32 0, i32* %".2"
  %"numbers" = alloca [5000 x i32]
  %".4" = getelementptr inbounds [47 x i8], [47 x i8]* @".str0", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4")
  %".6" = getelementptr inbounds [1000 x i8], [1000 x i8]* %"input_str", i32 0, i32 0
  %".7" = call i8* @"gets"(i8* %".6")
  %".8" = alloca i32
  %".9" = getelementptr [1000 x i8], [1000 x i8]* %"input_str", i32 0, i32 0
  %".10" = call i32 @"strlen"(i8* %".9")
  store i32 %".10", i32* %".8"
  %".12" = alloca i32
  store i32 0, i32* %".12"
  %"i" = alloca i32
  %".14" = load i32, i32* %".8"
  %".15" = sub i32 %".14", 1
  store i32 %".15", i32* %"i"
  br label %".17"
.17:
  %".21" = load i32, i32* %"i"
  %".22" = icmp sge i32 %".21", 0
  br i1 %".22", label %".18", label %".19"
.18:
  br label %".24"
.19:
  %".71" = load i32, i32* %".12"
  %".72" = load i32, i32* %".2"
  %".73" = getelementptr inbounds [5000 x i32], [5000 x i32]* %"numbers", i32 0, i32 %".72"
  store i32 %".71", i32* %".73"
  %".75" = load i32, i32* %".2"
  %".76" = add i32 %".75", 1
  store i32 %".76", i32* %".2"
  %"i.1" = alloca i32
  store i32 0, i32* %"i.1"
  br label %".79"
.24:
  %".27" = load i32, i32* %"i"
  %".28" = getelementptr inbounds [1000 x i8], [1000 x i8]* %"input_str", i32 0, i32 %".27"
  %".29" = load i8, i8* %".28"
  %".30" = zext i8 %".29" to i32
  %".31" = zext i8 44 to i32
  %".32" = icmp eq i8 %".29", 44
  br i1 %".32", label %"if.true", label %"if.false"
.25:
  %".67" = load i32, i32* %"i"
  %".68" = sub i32 %".67", 1
  store i32 %".68", i32* %"i"
  br label %".17"
if.true:
  %".34" = load i32, i32* %".12"
  %".35" = load i32, i32* %".2"
  %".36" = getelementptr inbounds [5000 x i32], [5000 x i32]* %"numbers", i32 0, i32 %".35"
  store i32 %".34", i32* %".36"
  store i32 0, i32* %".12"
  %".39" = load i32, i32* %".2"
  %".40" = add i32 %".39", 1
  store i32 %".40", i32* %".2"
  br label %".25"
if.false:
  %".45" = load i32, i32* %"i"
  %".46" = getelementptr inbounds [1000 x i8], [1000 x i8]* %"input_str", i32 0, i32 %".45"
  %".47" = load i8, i8* %".46"
  %".48" = zext i8 %".47" to i32
  %".49" = zext i8 45 to i32
  %".50" = icmp eq i8 %".47", 45
  br i1 %".50", label %".43", label %".44"
.43:
  %".52" = load i32, i32* %".12"
  %".53" = sub i32 0, %".52"
  store i32 %".53", i32* %".12"
  br label %".25"
.44:
  %".56" = load i32, i32* %".12"
  %".57" = mul i32 %".56", 10
  %".58" = load i32, i32* %"i"
  %".59" = getelementptr inbounds [1000 x i8], [1000 x i8]* %"input_str", i32 0, i32 %".58"
  %".60" = load i8, i8* %".59"
  %".61" = zext i8 %".60" to i32
  %".62" = add i32 %".57", %".61"
  %".63" = zext i8 48 to i32
  %".64" = sub i32 %".62", %".63"
  store i32 %".64", i32* %".12"
  br label %".25"
.79:
  %".83" = load i32, i32* %"i.1"
  %".84" = load i32, i32* %".2"
  %".85" = icmp slt i32 %".83", %".84"
  br i1 %".85", label %".80", label %".81"
.80:
  %"j" = alloca i32
  store i32 0, i32* %"j"
  br label %".88"
.81:
  %"i.2" = alloca i32
  store i32 0, i32* %"i.2"
  br label %".140"
.88:
  %".92" = load i32, i32* %"j"
  %".93" = load i32, i32* %".2"
  %".94" = icmp slt i32 %".92", %".93"
  %".95" = load i32, i32* %"i.1"
  %".96" = zext i1 %".94" to i32
  %".97" = sub i32 %".96", %".95"
  %".98" = sub i32 %".97", 1
  br i32 %".98", label %".89", label %".90"
.89:
  br label %".100"
.90:
  %".135" = load i32, i32* %"i.1"
  %".136" = add i32 %".135", 1
  store i32 %".136", i32* %"i.1"
  br label %".79"
.100:
  %".103" = load i32, i32* %"j"
  %".104" = getelementptr inbounds [5000 x i32], [5000 x i32]* %"numbers", i32 0, i32 %".103"
  %".105" = load i32, i32* %".104"
  %".106" = load i32, i32* %"j"
  %".107" = add i32 %".106", 1
  %".108" = getelementptr inbounds [5000 x i32], [5000 x i32]* %"numbers", i32 0, i32 %".107"
  %".109" = load i32, i32* %".108"
  %".110" = icmp sgt i32 %".105", %".109"
  br i1 %".110", label %"if.true.1", label %"if.false.1"
.101:
  %".131" = load i32, i32* %"j"
  %".132" = add i32 %".131", 1
  store i32 %".132", i32* %"j"
  br label %".88"
if.true.1:
  %".112" = alloca i32
  %".113" = load i32, i32* %"j"
  %".114" = getelementptr inbounds [5000 x i32], [5000 x i32]* %"numbers", i32 0, i32 %".113"
  %".115" = load i32, i32* %".114"
  store i32 %".115", i32* %".112"
  %".117" = load i32, i32* %"j"
  %".118" = add i32 %".117", 1
  %".119" = getelementptr inbounds [5000 x i32], [5000 x i32]* %"numbers", i32 0, i32 %".118"
  %".120" = load i32, i32* %".119"
  %".121" = load i32, i32* %"j"
  %".122" = getelementptr inbounds [5000 x i32], [5000 x i32]* %"numbers", i32 0, i32 %".121"
  store i32 %".120", i32* %".122"
  %".124" = load i32, i32* %".112"
  %".125" = load i32, i32* %"j"
  %".126" = add i32 %".125", 1
  %".127" = getelementptr inbounds [5000 x i32], [5000 x i32]* %"numbers", i32 0, i32 %".126"
  store i32 %".124", i32* %".127"
  br label %".101"
if.false.1:
  br label %".101"
.140:
  %".144" = load i32, i32* %"i.2"
  %".145" = load i32, i32* %".2"
  %".146" = icmp slt i32 %".144", %".145"
  %".147" = zext i1 %".146" to i32
  %".148" = sub i32 %".147", 1
  br i32 %".148", label %".141", label %".142"
.141:
  %".150" = getelementptr inbounds [4 x i8], [4 x i8]* @".str1", i32 0, i32 0
  %".151" = load i32, i32* %"i.2"
  %".152" = getelementptr inbounds [5000 x i32], [5000 x i32]* %"numbers", i32 0, i32 %".151"
  %".153" = load i32, i32* %".152"
  %".154" = call i32 (i8*, ...) @"printf"(i8* %".150", i32 %".153")
  %".155" = load i32, i32* %"i.2"
  %".156" = add i32 %".155", 1
  store i32 %".156", i32* %"i.2"
  br label %".140"
.142:
  %".159" = getelementptr inbounds [4 x i8], [4 x i8]* @".str2", i32 0, i32 0
  %".160" = load i32, i32* %".2"
  %".161" = sub i32 %".160", 1
  %".162" = getelementptr inbounds [5000 x i32], [5000 x i32]* %"numbers", i32 0, i32 %".161"
  %".163" = load i32, i32* %".162"
  %".164" = call i32 (i8*, ...) @"printf"(i8* %".159", i32 %".163")
}

declare i32 @"printf"(i8* %".1", ...)

@".str0" = constant [47 x i8] c"Please input Char Array Under 1000 characters\0a\00"
declare i8* @"gets"(i8* %".1")

declare i32 @"strlen"(i8* %".1")

@".str1" = constant [4 x i8] c"%d,\00"
@".str2" = constant [4 x i8] c"%d\0a\00"