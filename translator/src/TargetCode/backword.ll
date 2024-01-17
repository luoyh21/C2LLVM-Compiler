; ModuleID = "clong prog"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

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
  %".49" = zext i1 %".47" to i32
  %".50" = and i32 %".49", %".48"
  %".51" = icmp ne i32 %".50", 1
  br i1 %".51", label %".40", label %".41"
.40:
  br label %".53"
.41:
  br label %".78"
.53:
  %".56" = load i32, i32* %".6"
  %".57" = sub i32 %".56", 1
  %".58" = load i32, i32* %".8"
  %".59" = sub i32 %".57", %".58"
  %".60" = getelementptr inbounds [1001 x i8], [1001 x i8]* %"StringGet", i32 0, i32 %".59"
  %".61" = load i8, i8* %".60"
  %".62" = load i32, i32* %".8"
  %".63" = getelementptr inbounds [1001 x i8], [1001 x i8]* %"StringGet", i32 0, i32 %".62"
  %".64" = load i8, i8* %".63"
  %".65" = zext i8 %".61" to i32
  %".66" = zext i8 %".64" to i32
  %".67" = icmp ne i8 %".61", %".64"
  br i1 %".67", label %"if.true.2", label %"if.false.2"
.54:
  %".74" = load i32, i32* %".8"
  %".75" = add i32 %".74", 1
  store i32 %".75", i32* %".8"
  br label %".39"
if.true.2:
  %".69" = getelementptr inbounds [7 x i8], [7 x i8]* @".str3", i32 0, i32 0
  %".70" = call i32 (i8*, ...) @"printf"(i8* %".69")
  store i32 1, i32* %".36"
  br label %".54"
if.false.2:
  br label %".54"
.78:
  %".81" = load i32, i32* %".36"
  %".82" = icmp ne i32 %".81", 1
  br i1 %".82", label %"if.true.3", label %"if.false.3"
.79:
  br label %".26"
if.true.3:
  %".84" = getelementptr inbounds [6 x i8], [6 x i8]* @".str4", i32 0, i32 0
  %".85" = call i32 (i8*, ...) @"printf"(i8* %".84")
  br label %".79"
if.false.3:
  br label %".79"
}

declare i32 @"printf"(i8* %".1", ...)

@".str0" = constant [47 x i8] c"Please input Char Array Under 1000 characters\0a\00"
declare i8* @"gets"(i8* %".1")

declare i32 @"strlen"(i8* %".1")

@".str1" = constant [36 x i8] c"Input Error, only one more chance:\0a\00"
@".str2" = constant [36 x i8] c"Input Error, only one more chance:\0a\00"
@".str3" = constant [7 x i8] c"False\0a\00"
@".str4" = constant [6 x i8] c"True\0a\00"