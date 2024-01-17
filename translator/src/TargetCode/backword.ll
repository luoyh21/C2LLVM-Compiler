; ModuleID = "clong prog"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:o-i64:64-f80:128-n8:16:32:64-S128"

define i32 @"main"()
{
main.entry:
  %".2" = getelementptr inbounds [47 x i8], [47 x i8]* @".str0", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  %"StringGet" = alloca [1001 x i8]
  %".4" = getelementptr inbounds [1001 x i8], [1001 x i8]* %"StringGet", i32 0, i32 0
  %".5" = call i8* @"gets"(i8* %".4")
  %".6" = alloca i32
  store i32 0, i32* %".6"
  %".8" = alloca i32
  store i32 0, i32* %".8"
  %".10" = getelementptr [1001 x i8], [1001 x i8]* %"StringGet", i32 0, i32 0
  %".11" = call i32 @"strlen"(i8* %".10")
  store i32 %".11", i32* %".6"
  br label %".13"
.13:
  %".16" = load i32, i32* %".6"
  %".17" = icmp slt i32 %".16", 0
  br i1 %".17", label %"if.true", label %"if.false"
.14:
  br label %".25"
if.true:
  %".19" = getelementptr inbounds [36 x i8], [36 x i8]* @".str1", i32 0, i32 0
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".19")
  %".21" = getelementptr inbounds [1001 x i8], [1001 x i8]* %"StringGet", i32 0, i32 0
  %".22" = call i8* @"gets"(i8* %".21")
  br label %".14"
if.false:
  br label %".14"
.25:
  %".28" = load i32, i32* %".6"
  %".29" = icmp sgt i32 %".28", 1000
  br i1 %".29", label %"if.true.1", label %"if.false.1"
.26:
  ret i32 0
if.true.1:
  %".31" = getelementptr inbounds [36 x i8], [36 x i8]* @".str2", i32 0, i32 0
  %".32" = call i32 (i8*, ...) @"printf"(i8* %".31")
  %".33" = getelementptr inbounds [1001 x i8], [1001 x i8]* %"StringGet", i32 0, i32 0
  %".34" = call i8* @"gets"(i8* %".33")
  br label %".26"
if.false.1:
  %".36" = alloca i32
  store i32 -1, i32* %".36"
  store i32 0, i32* %".8"
  br label %".39"
.39:
  %".43" = load i32, i32* %".8"
  %".44" = load i32, i32* %".8"
  %".45" = add i32 %".43", %".44"
  %".46" = load i32, i32* %".6"
  %".47" = icmp slt i32 %".45", %".46"
  %".48" = load i32, i32* %".36"
  %".49" = icmp ne i32 %".48", 1
  %".50" = and i1 %".47", %".49"
  br i1 %".50", label %".40", label %".41"
.40:
  br label %".52"
.41:
  br label %".77"
.52:
  %".55" = load i32, i32* %".6"
  %".56" = sub i32 %".55", 1
  %".57" = load i32, i32* %".8"
  %".58" = sub i32 %".56", %".57"
  %".59" = getelementptr inbounds [1001 x i8], [1001 x i8]* %"StringGet", i32 0, i32 %".58"
  %".60" = load i8, i8* %".59"
  %".61" = load i32, i32* %".8"
  %".62" = getelementptr inbounds [1001 x i8], [1001 x i8]* %"StringGet", i32 0, i32 %".61"
  %".63" = load i8, i8* %".62"
  %".64" = zext i8 %".60" to i32
  %".65" = zext i8 %".63" to i32
  %".66" = icmp ne i32 %".64", %".65"
  br i1 %".66", label %"if.true.2", label %"if.false.2"
.53:
  %".73" = load i32, i32* %".8"
  %".74" = add i32 %".73", 1
  store i32 %".74", i32* %".8"
  br label %".39"
if.true.2:
  %".68" = getelementptr inbounds [7 x i8], [7 x i8]* @".str3", i32 0, i32 0
  %".69" = call i32 (i8*, ...) @"printf"(i8* %".68")
  store i32 1, i32* %".36"
  br label %".53"
if.false.2:
  br label %".53"
.77:
  %".80" = load i32, i32* %".36"
  %".81" = icmp ne i32 %".80", 1
  br i1 %".81", label %"if.true.3", label %"if.false.3"
.78:
  br label %".26"
if.true.3:
  %".83" = getelementptr inbounds [6 x i8], [6 x i8]* @".str4", i32 0, i32 0
  %".84" = call i32 (i8*, ...) @"printf"(i8* %".83")
  br label %".78"
if.false.3:
  br label %".78"
}

declare i32 @"printf"(i8* %".1", ...)

@".str0" = constant [47 x i8] c"Please input Char Array Under 1000 characters\0a\00"
declare i8* @"gets"(i8* %".1")

declare i32 @"strlen"(i8* %".1")

@".str1" = constant [36 x i8] c"Input Error, only one more chance:\0a\00"
@".str2" = constant [36 x i8] c"Input Error, only one more chance:\0a\00"
@".str3" = constant [7 x i8] c"False\0a\00"
@".str4" = constant [6 x i8] c"True\0a\00"