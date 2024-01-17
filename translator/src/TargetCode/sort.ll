; ModuleID = "clong prog"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:o-i64:64-f80:128-n8:16:32:64-S128"

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
  %".32" = icmp eq i32 %".30", %".31"
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
  %".50" = icmp eq i32 %".48", %".49"
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
  br label %".139"
.88:
  %".92" = load i32, i32* %"j"
  %".93" = load i32, i32* %".2"
  %".94" = load i32, i32* %"i.1"
  %".95" = sub i32 %".93", %".94"
  %".96" = sub i32 %".95", 1
  %".97" = icmp slt i32 %".92", %".96"
  br i1 %".97", label %".89", label %".90"
.89:
  br label %".99"
.90:
  %".134" = load i32, i32* %"i.1"
  %".135" = add i32 %".134", 1
  store i32 %".135", i32* %"i.1"
  br label %".79"
.99:
  %".102" = load i32, i32* %"j"
  %".103" = getelementptr inbounds [5000 x i32], [5000 x i32]* %"numbers", i32 0, i32 %".102"
  %".104" = load i32, i32* %".103"
  %".105" = load i32, i32* %"j"
  %".106" = add i32 %".105", 1
  %".107" = getelementptr inbounds [5000 x i32], [5000 x i32]* %"numbers", i32 0, i32 %".106"
  %".108" = load i32, i32* %".107"
  %".109" = icmp sgt i32 %".104", %".108"
  br i1 %".109", label %"if.true.1", label %"if.false.1"
.100:
  %".130" = load i32, i32* %"j"
  %".131" = add i32 %".130", 1
  store i32 %".131", i32* %"j"
  br label %".88"
if.true.1:
  %".111" = alloca i32
  %".112" = load i32, i32* %"j"
  %".113" = getelementptr inbounds [5000 x i32], [5000 x i32]* %"numbers", i32 0, i32 %".112"
  %".114" = load i32, i32* %".113"
  store i32 %".114", i32* %".111"
  %".116" = load i32, i32* %"j"
  %".117" = add i32 %".116", 1
  %".118" = getelementptr inbounds [5000 x i32], [5000 x i32]* %"numbers", i32 0, i32 %".117"
  %".119" = load i32, i32* %".118"
  %".120" = load i32, i32* %"j"
  %".121" = getelementptr inbounds [5000 x i32], [5000 x i32]* %"numbers", i32 0, i32 %".120"
  store i32 %".119", i32* %".121"
  %".123" = load i32, i32* %".111"
  %".124" = load i32, i32* %"j"
  %".125" = add i32 %".124", 1
  %".126" = getelementptr inbounds [5000 x i32], [5000 x i32]* %"numbers", i32 0, i32 %".125"
  store i32 %".123", i32* %".126"
  br label %".100"
if.false.1:
  br label %".100"
.139:
  %".143" = load i32, i32* %"i.2"
  %".144" = load i32, i32* %".2"
  %".145" = sub i32 %".144", 1
  %".146" = icmp slt i32 %".143", %".145"
  br i1 %".146", label %".140", label %".141"
.140:
  %".148" = getelementptr inbounds [4 x i8], [4 x i8]* @".str1", i32 0, i32 0
  %".149" = load i32, i32* %"i.2"
  %".150" = getelementptr inbounds [5000 x i32], [5000 x i32]* %"numbers", i32 0, i32 %".149"
  %".151" = load i32, i32* %".150"
  %".152" = call i32 (i8*, ...) @"printf"(i8* %".148", i32 %".151")
  %".153" = load i32, i32* %"i.2"
  %".154" = add i32 %".153", 1
  store i32 %".154", i32* %"i.2"
  br label %".139"
.141:
  %".157" = getelementptr inbounds [4 x i8], [4 x i8]* @".str2", i32 0, i32 0
  %".158" = load i32, i32* %".2"
  %".159" = sub i32 %".158", 1
  %".160" = getelementptr inbounds [5000 x i32], [5000 x i32]* %"numbers", i32 0, i32 %".159"
  %".161" = load i32, i32* %".160"
  %".162" = call i32 (i8*, ...) @"printf"(i8* %".157", i32 %".161")
}

declare i32 @"printf"(i8* %".1", ...)

@".str0" = constant [47 x i8] c"Please input Char Array Under 1000 characters\0a\00"
declare i8* @"gets"(i8* %".1")

declare i32 @"strlen"(i8* %".1")

@".str1" = constant [4 x i8] c"%d,\00"
@".str2" = constant [4 x i8] c"%d\0a\00"